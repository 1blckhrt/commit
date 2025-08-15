import sqlite3
import datetime
import pathlib

db_path = pathlib.Path.home() / ".cc" / "commits.db"


def create_database():
    """Create the database and the commits table if they don't exist."""
    db_path.parent.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    c.execute(
        """
        CREATE TABLE IF NOT EXISTS commits (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            type TEXT NOT NULL,
            scope TEXT,
            description TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
        """
    )
    conn.commit()
    conn.close()


def save_commit(commit_type: str, scope: str | None, description: str):
    """Save a commit to the database."""
    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    c.execute(
        "INSERT INTO commits (type, scope, description, created_at) VALUES (?, ?, ?, ?)",
        (commit_type, scope, description, datetime.datetime.now()),
    )
    conn.commit()
    conn.close()


def get_commit_stats():
    """Get commit statistics from the database."""
    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    c.execute("SELECT type, COUNT(*) FROM commits GROUP BY type")
    stats = c.fetchall()
    conn.close()
    return stats
