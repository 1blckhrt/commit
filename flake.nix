{
  description = "Flake for commit";

  inputs = {
    pyproject-nix = {
      url = "github:nix-community/pyproject.nix";
      inputs.nixpkgs.follows = "nixpkgs";
    };
  };

  outputs = {
    nixpkgs,
    pyproject-nix,
    ...
  }: let
    inherit (nixpkgs) lib;

    project = pyproject-nix.lib.project.loadPyproject {
      projectRoot = ./.;
    };

    pkgs = nixpkgs.legacyPackages.x86_64-linux;

    python = pkgs.python313;
  in {
    packages.x86_64-linux.default = let
      attrs = project.renderers.buildPythonPackage {inherit python;};
    in
      python.pkgs.buildPythonPackage attrs;
  };
}
