def format_commit_message(
    commit_type: str, scope: str | None, description: str | None
) -> str:
    parts = [commit_type]
    if scope:
        parts.append(f"({scope})")
    if description:
        parts.append(description)
    return ": ".join(parts)
