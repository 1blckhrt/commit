from enum import Enum

class CommitType(str, Enum):
    FEAT = "feat"
    FIX = "fix"
    CHORE = "chore"
    DOCS = "docs"
    REFACTOR = "refactor"
    TEST = "test"
    STYLE = "style"

    @property
    def description(self):
        descriptions = {
            CommitType.FEAT: "Introduces a new feature",
            CommitType.FIX: "Bug fix",
            CommitType.CHORE: "Maintenance tasks",
            CommitType.DOCS: "Documentation changes",
            CommitType.REFACTOR: "Code refactoring",
            CommitType.TEST: "Adding or updating tests",
            CommitType.STYLE: "Code style changes",
        }
        return descriptions[self]