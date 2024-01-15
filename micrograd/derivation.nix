{ python39Packages }:
with python39Packages;
buildPythonApplication {
  pname = "micrograd";
  version = "1.0";
  src = ./.;
}
