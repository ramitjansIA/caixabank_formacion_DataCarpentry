import pandas as pd

from .config import Configuracion
from .validacion import validar_operaciones


def crear_informe(datos: pd.DataFrame, importe_minimo: float = 0.0) -> pd.DataFrame:
    """Crea el informe mensual de operaciones confirmadas sin modificar la entrada."""
    validar_operaciones(datos)
    salida = datos.copy()
    salida["fecha"] = pd.to_datetime(salida["fecha"], errors="raise")
    salida = salida.loc[
        salida["estado"].eq("confirmada") & salida["importe"].ge(importe_minimo)
    ].copy()
    salida["mes"] = salida["fecha"].dt.to_period("M").astype(str)
    return (
        salida.groupby(["mes", "region", "canal"], as_index=False)
        .agg(importe_total=("importe", "sum"), operaciones=("importe", "size"))
        .sort_values(["mes", "region", "canal"], ignore_index=True)
    )


def ejecutar_pipeline(config: Configuracion) -> pd.DataFrame:
    datos = pd.read_csv(config.input_path)
    informe = crear_informe(datos, config.importe_minimo)
    config.output_path.parent.mkdir(parents=True, exist_ok=True)
    informe.to_csv(config.output_path, index=False)
    return informe
