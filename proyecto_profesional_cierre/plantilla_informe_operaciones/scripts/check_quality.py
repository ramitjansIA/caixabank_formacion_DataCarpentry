"""Alternativa multiplataforma a Makefile para las comprobaciones locales."""
import subprocess
import sys


def ejecutar(comando: list[str]) -> None:
    subprocess.run(comando, check=True)


def main() -> None:
    ejecutar([sys.executable, "-m", "pytest", "-q"])
    ejecutar([sys.executable, "-m", "ruff", "check", "."])


if __name__ == "__main__":
    main()
