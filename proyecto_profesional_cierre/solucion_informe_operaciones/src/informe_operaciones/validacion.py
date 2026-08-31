import pandas as pd

COLUMNAS_OBLIGATORIAS = {"fecha", "region", "canal", "estado", "importe"}


class ContratoDatosError(ValueError):
    """El origen no cumple el contrato mínimo del informe."""


def validar_operaciones(datos: pd.DataFrame) -> None:
    """Comprueba el contrato mínimo del origen antes de transformar."""
    ausentes = COLUMNAS_OBLIGATORIAS.difference(datos.columns)
    if ausentes:
        raise ContratoDatosError(f"Faltan columnas obligatorias: {sorted(ausentes)}")
    if datos["importe"].isna().any():
        raise ContratoDatosError("La columna importe no puede contener valores nulos")
