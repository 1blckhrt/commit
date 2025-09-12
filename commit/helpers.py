from commit.constants import CommitType


def get_commit_emoji(commit_type):
    """Get the emoji associated with a commit type."""
    emoji_map = {
        CommitType.FEAT: "✨",
        CommitType.FIX: "🐛",
        CommitType.DOCS: "📚",
        CommitType.STYLE: "🎨",
        CommitType.REFACTOR: "🔨",
        CommitType.CHORE: "🧹",
        CommitType.TEST: "✅",
    }
    # accept either enum or string
    if isinstance(commit_type, str):
        try:
            commit_type = CommitType(commit_type)
        except ValueError:
            return "💬"
    return emoji_map.get(commit_type, "💬")
