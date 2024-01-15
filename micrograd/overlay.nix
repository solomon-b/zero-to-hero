final: prev: {
  micrograd =
    let micrograd = final.callPackage ./derivation.nix { };
    in final.writeShellScriptBin "micrograd" ''
      ${micrograd}/bin/main.py 
    '';
}
