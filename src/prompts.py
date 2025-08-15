import questionary

from helpers import get_commit_emoji
from constants import CommitType

choices = [
    {
        "name": f"{get_commit_emoji(ct.value)} {ct.value} - {ct.description}",
        "value": ct.value,
    }
    for ct in CommitType
]


def get_commit_type() -> str:
    return questionary.select(
        "Select the type of change you want to commit:", choices=choices
    ).ask()


def get_scope() -> str | None:
    response = questionary.text("Enter the scope of the change (optional):").ask()
    return response.strip() if response else None


def get_description() -> str | None:
    response = questionary.text("Enter a description of the change:").ask()
    return response.strip() if response else None
