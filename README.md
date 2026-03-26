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

To use `commit`, run the following file within the repository:
```bash
python3 -m commit.main
```

To view your statistics, run the following file with the `--stats` flag:
```bash
python3 -m commit.main --stats
```

Alternatively, you can use the flake provided and run it as a standalone CLI program. 

## Python Installation

1. Clone the repository
2. Install the required dependencies (I recommend using `uv`)
3. Alias the entry point to your shell.

## Flake Installation

```nix
# flake.nix
{
  description = "Flake with commit";
  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixos-25.11";

    commit = {
      url = "github:1blckhrt/commit";
      inputs.nixpkgs.follows = "nixpkgs";
    };
  };

  outputs = {
    self,
    nixpkgs,
    commit,
    ...
  } @ inputs: let
    system = "x86_64-linux";
    lib = nixpkgs.lib;
    forAllSystems = lib.genAttrs [system];
  in {
    homeConfigurations = {
      # replace with your info
      "user@host" = home-manager.lib.homeManagerConfiguration {
        pkgs = nixpkgs.legacyPackages.${system};
        extraSpecialArgs = {inputs = {inherit self nixpkgs commit;};};
        modules = [
          ./home.nix
          {
            home.packages = [
              commit.packages.${system}.default
            ];
          }
        ];
      };
    };
  };
}

# home.nix
{
  config,
  pkgs,
  inputs,
  lib,
  ...
}: {
  home.packages = with pkgs; [
    inputs.commit.packages.x86_64-linux.default
  ];
}
```

You can also install it via the `nix profile install` command (**NOT** recommended), but do note that any bugs you may encounter with this tool or your system are **your** responsibility, not mine.

```bash
nix profile install github:1blckhrt/commit
```

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any changes you'd like to make.

## Roadmap

- Add more commit types
- Implement more advanced statistics
- Add improved alias installation instructions
- Make the installation process more user-friendly (e.g., provide a setup script or binary)
