import json
from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class Configuracion:
    input_path: Path
    output_path: Path
    importe_minimo: float


def cargar_configuracion(ruta: Path) -> Configuracion:
    """Carga una configuración JSON y resuelve rutas respecto a la raíz del proyecto."""
    contenido = json.loads(ruta.read_text(encoding="utf-8"))
    # TODO 1: valida las tres claves obligatorias antes de crear Configuracion.
    raiz = ruta.parent.parent
    return Configuracion(
        input_path=raiz / contenido["input_path"],
        output_path=raiz / contenido["output_path"],
        importe_minimo=float(contenido["importe_minimo"]),
    )
