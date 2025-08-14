from enum import Enum


class CommitType(Enum):
    FEAT = ("feat", "Introduces a new feature")
    FIX = ("fix", "Bug fix")
    CHORE = ("chore", "Maintenance tasks")
    DOCS = ("docs", "Documentation changes")
    REFACTOR = ("refactor", "Code refactoring")
    TEST = ("test", "Adding or updating tests")
    STYLE = ("style", "Code style changes")

    def __init__(self, key, description):
        self.key = key
        self.description = description


