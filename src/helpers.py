def get_commit_emoji(commit_type):
    """Get the emoji associated with a commit type."""
    emoji_map = {
        "feat": "✨",
        "fix": "🐛",
        "docs": "📚",
        "style": "🎨",
        "refactor": "🔨",
        "chore": "🧹",
    }
    return emoji_map.get(commit_type, "💬")
