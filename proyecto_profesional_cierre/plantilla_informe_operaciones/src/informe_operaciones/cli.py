import argparse
from pathlib import Path

from .config import cargar_configuracion
from .pipeline import ejecutar_pipeline


def main() -> None:
    parser = argparse.ArgumentParser(description="Genera el informe de operaciones.")
    parser.add_argument("--config", type=Path, default=Path("config/config.json"))
    args = parser.parse_args()
    informe = ejecutar_pipeline(cargar_configuracion(args.config))
    print(f"Informe creado con {len(informe)} filas.")


if __name__ == "__main__":
    main()
