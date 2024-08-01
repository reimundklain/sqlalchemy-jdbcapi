{
  inputs = {
    flake-utils.url = "github:numtide/flake-utils";
    nixpkgs.url = "github:NixOS/nixpkgs/nixos-unstable";
  };

  outputs = { self, nixpkgs, flake-utils }:
    flake-utils.lib.eachDefaultSystem (system:
      let
        pythonEnv = pkgs.python312;
        poetryEnv = (pkgs.poetry.override { python3 = pythonEnv; });
        pkgs = import nixpkgs { 
          inherit system; 
          overlays = [
            (final: prev: rec {
              nodejs = prev.nodejs_20;
            })
          ];
            
        }; 
     in
      {
        devShells.default = pkgs.mkShell {
          LD_LIBRARY_PATH="${pkgs.stdenv.cc.cc.lib}/lib/";
          nativeBuildInputs = with pkgs; [
            pythonEnv
            poetryEnv
            pre-commit
          ];
        };
      });
}
