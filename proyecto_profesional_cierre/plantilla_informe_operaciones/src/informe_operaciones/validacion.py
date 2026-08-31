import pandas as pd

COLUMNAS_OBLIGATORIAS = {"fecha", "region", "canal", "estado", "importe"}


class ContratoDatosError(ValueError):
    """El origen no cumple el contrato mínimo del informe."""


def validar_operaciones(datos: pd.DataFrame) -> None:
    """Comprueba el contrato mínimo del origen antes de transformar."""
    # TODO 2: calcula columnas ausentes y lanza ValueError con un mensaje útil.
    pass
