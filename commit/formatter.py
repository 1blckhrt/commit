def format_commit_message(
    commit_type: str, scope: str | None, description: str | None
) -> str:
    """Format the commit message."""
    head = commit_type
    if scope:
        head += f"({scope})"

    if description:
        return f"{head}: {description}"
    return head
