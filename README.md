# commit cli

`commit` is a CLI program used to manage your conventional commits.

## Features

- Interactive prompts for commit type, scope, description
- Enforces the Conventional Commits standard
- Built with Python and the user-friendly `questionary` prompt toolkit
- Displays your git status before committing
- Tracks your commit history locally (SQLite database)
- Prevents commits without changes

## Usage

To use `cc`, run the following file within the repository:
```bash
src/main.py
```

To view your statistics, run the following file with the `--stats` flag:
```bash
src/main.py --stats
```

Alternatively, you can use the flake provided.

## Installation

1. Clone the repository
2. Install the required dependencies (I recommend using `uv`)
3. Alias the entry point to your shell (e.g., `alias commit="python path/to/coimmit/src/main.py"`)

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any changes you'd like to make.

## Roadmap

- Add more commit types
- Implement more advanced statistics
- Add improved alias installation instructions
- Make the installation process more user-friendly (e.g., provide a setup script or binary)
