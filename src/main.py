from formatter import format_commit_message
from prompts import get_commit_type, get_description, get_scope
import questionary
import subprocess
import argparse
from database import create_database, save_commit, get_commit_stats
from helpers import get_commit_emoji
from rich.console import Console
from rich.table import Table
from rich.panel import Panel


console = Console()


def main():
    create_database()

    parser = argparse.ArgumentParser(description="Generate a git commit message.")
    parser.add_argument(
        "--stats", action="store_true", help="Show your commit statistics."
    )
    args = parser.parse_args()

    if args.stats:
        console.print("[bold cyan]Showing your commit statistics...[/bold cyan]")
        stats = get_commit_stats()
        if not stats:
            console.print("[yellow]No commit statistics available.[/yellow]")
            return
        table = Table(
            title="Commit Statistics", show_header=True, header_style="bold magenta"
        )
        table.add_column("Type", style="magenta")
        table.add_column("Count", style="green")
        for stat in stats:
            emoji = get_commit_emoji(str(stat[0]))
            table.add_row(f"{emoji} {stat[0]}", str(stat[1]))
        console.print(table)
        return

    commit_type = get_commit_type()
    scope = get_scope()
    description = get_description()

    commit_message = format_commit_message(commit_type, scope, description)

    console.print("[bold blue]Showing your git status...[/bold blue]")
    subprocess.run(["git", "status"])

    emoji = get_commit_emoji(commit_type)
    panel_title = f"Commit Message {emoji}"
    console.print(
        Panel.fit(
            f"[bold]{commit_message}[/bold]", title=panel_title, border_style="green"
        )
    )

    if questionary.confirm("Do you want to use this commit message?").ask():
        subprocess.run(["git", "commit", "-m", commit_message])
        save_commit(commit_type, scope, description if description is not None else "")
        console.print(f"[green]Commit saved![/green] {emoji}")
    else:
        console.print("[red]Commit message discarded.[/red]")


if __name__ == "__main__":
    main()
