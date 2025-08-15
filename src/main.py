from formatter import format_commit_message
from prompts import get_commit_type, get_description, get_scope
import questionary
import subprocess


def main():
    commit_type = get_commit_type()
    scope = get_scope()
    description = get_description()

    commit_message = format_commit_message(commit_type, scope, description)

    print(f"Generated commit message: \n{commit_message}")
    print("Showing your git status...")
    subprocess.run(["git", "status"])

    if questionary.confirm("Do you want to use this commit message?").ask():
        subprocess.run(["git", "commit", "-m", commit_message])
    else:
        print("Commit message discarded.")


if __name__ == "__main__":
    main()
