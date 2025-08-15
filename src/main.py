from formatter import format_commit_message
from prompts import get_commit_type, get_description, get_scope
import questionary
import subprocess
import argparse
from database import create_database, save_commit, get_commit_stats


def main():
    create_database()

    parser = argparse.ArgumentParser(description="Generate a git commit message.")
    parser.add_argument(
        "--stats", action="store_true", help="Show your commit statistics."
    )
    args = parser.parse_args()

    if args.stats:
        print("Showing your commit statistics...")
        stats = get_commit_stats()
        if not stats:
            print("No commit statistics available.")
            return
        for stat in stats:
            print(f" - {stat[0]}: {stat[1]}")
        return

    commit_type = get_commit_type()
    scope = get_scope()
    description = get_description()

    commit_message = format_commit_message(commit_type, scope, description)

    print(f"Generated commit message: \n{commit_message}")
    print("Showing your git status...")
    subprocess.run(["git", "status"])

    if questionary.confirm("Do you want to use this commit message?").ask():
        subprocess.run(["git", "commit", "-m", commit_message])
        save_commit(commit_type, scope, description if description is not None else "")
    else:
        print("Commit message discarded.")


if __name__ == "__main__":
    main()
