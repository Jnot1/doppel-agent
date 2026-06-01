# nix/overlays.nix — Expose Doppel/Hermes package aliases for external NixOS configs
{ inputs, ... }:
{
  flake.overlays.default = final: _: let
    hermesAgent = final.callPackage ./hermes-agent.nix {
      inherit (inputs) uv2nix pyproject-nix pyproject-build-systems;
      npm-lockfile-fix = inputs.npm-lockfile-fix.packages.${final.stdenv.hostPlatform.system}.default;
      rev = inputs.self.rev or null;
    };
  in {
    doppel-agent = hermesAgent;
    hermes-agent = hermesAgent;
  };
}
