import pandas as pd

from .config import Configuracion
from .validacion import validar_operaciones


def crear_informe(datos: pd.DataFrame, importe_minimo: float = 0.0) -> pd.DataFrame:
    """Crea el informe mensual de operaciones confirmadas sin modificar la entrada."""
    validar_operaciones(datos)
    # TODO 3: filtra confirmadas y aplica importe_minimo antes de agrupar.
    # TODO 4: devuelve importe total y número de operaciones por mes, región y canal.
    raise NotImplementedError


def ejecutar_pipeline(config: Configuracion) -> pd.DataFrame:
    datos = pd.read_csv(config.input_path)
    informe = crear_informe(datos, config.importe_minimo)
    config.output_path.parent.mkdir(parents=True, exist_ok=True)
    informe.to_csv(config.output_path, index=False)
    return informe
