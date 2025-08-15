from formatter import format_commit_message
from prompts import get_commit_type, get_description, get_scope


def main():
    commit_type = get_commit_type()
    scope = get_scope()
    description = get_description()

    commit_message = format_commit_message(commit_type, scope, description)
    print(commit_message)


if __name__ == "__main__":
    main()
