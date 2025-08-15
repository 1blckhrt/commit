import sys
import questionary

from helpers import get_commit_emoji
from constants import CommitType

from rich.console import Console


console = Console()

choices = [
    {
        "name": f"{get_commit_emoji(ct.value)} {ct.value} - {ct.description}",
        "value": ct.value,
    }
    for ct in CommitType
]


def get_commit_type() -> str | None:
    """Prompt the user to select a commit type."""
    commit_type = questionary.select(
        "Select the type of change you want to commit:", choices=choices
    ).ask()

    if commit_type is None:
        console.print("\n[red]No commit type specified. Exiting immediately.[/red]")
        sys.exit(0)

    return commit_type


def get_scope() -> str | None:
    """Prompt the user to enter a scope for the change."""
    response = questionary.text("Enter the scope of the change (optional):").ask()
    return response.strip() if response else None


def get_description() -> str | None:
    """Prompt the user to enter a description of the change."""
    description = questionary.text("Enter a description of the change:").ask()
    if description is None:
        console.print("\n[red]No description provided. Exiting immediately.[/red]")
        sys.exit(0)
    return description.strip()
