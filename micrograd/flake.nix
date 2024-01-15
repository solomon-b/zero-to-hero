{
  description = "Micrograd";

  inputs = {
    nixpkgs.url = "github:nixos/nixpkgs/nixos-23.11";
    flake-utils.url = "github:numtide/flake-utils";
  };

  outputs = { self, nixpkgs, flake-utils }:
    let
      overlay = import ./overlay.nix;
      overlays = [ overlay ];
    in
    flake-utils.lib.eachSystem [ "x86_64-linux" ]
      (system:
        let pkgs = import nixpkgs { inherit system overlays; };
        in {
          devShells.default = pkgs.mkShell {
            buildInputs = [
              pkgs.python39
            ];
          };
          formatter = pkgs.nixpkgs-fmt;
          packages.default = pkgs.micrograd;
        }) // {
      overlays.default = overlay;
    };
}
