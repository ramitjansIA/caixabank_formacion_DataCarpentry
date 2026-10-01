import argparse
from pathlib import Path

from .config import cargar_configuracion
from .pipeline import ejecutar_pipeline


def main() -> None:
    parser = argparse.ArgumentParser(description="Genera el informe de operaciones.")
    parser.add_argument("--config", type=Path, default=Path("config/config.json"))
    parser.add_argument("--mostrar-ruta", action="store_true")
    args = parser.parse_args()
    config = cargar_configuracion(args.config)
    if args.mostrar_ruta:
        print(config.output_path)
        return
    informe = ejecutar_pipeline(config)
    print(f"Informe creado con {len(informe)} filas.")


if __name__ == "__main__":
    main()
