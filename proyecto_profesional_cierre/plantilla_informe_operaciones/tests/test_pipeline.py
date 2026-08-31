import pandas as pd
import pytest

from informe_operaciones.pipeline import crear_informe
from informe_operaciones.validacion import validar_operaciones


@pytest.fixture
def operaciones() -> pd.DataFrame:
    return pd.DataFrame(
        {
            "fecha": ["2025-01-02", "2025-01-03", "2025-02-01"],
            "region": ["norte", "norte", "sur"],
            "canal": ["app", "oficina", "app"],
            "estado": ["confirmada", "rechazada", "confirmada"],
            "importe": [120.0, 80.0, 200.0],
        }
    )


def test_validar_operaciones_rechaza_columna_ausente() -> None:
    with pytest.raises(ValueError, match="columnas"):
        validar_operaciones(pd.DataFrame({"fecha": []}))


def test_crear_informe_conserva_el_origen(operaciones: pd.DataFrame) -> None:
    # TODO 5: guarda una copia, ejecuta crear_informe y comprueba que no hay mutación.
    pass


def test_crear_informe_agrega_confirmadas(operaciones: pd.DataFrame) -> None:
    # TODO 6: define el DataFrame esperado y compáralo con assert_frame_equal.
    pass
