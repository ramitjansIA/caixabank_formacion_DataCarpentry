import pandas as pd
import pytest
from pandas.testing import assert_frame_equal

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


def test_validar_operaciones_rechaza_importe_nulo(operaciones: pd.DataFrame) -> None:
    datos_invalidos = operaciones.copy()
    datos_invalidos.loc[0, "importe"] = None
    with pytest.raises(ValueError, match="importe"):
        validar_operaciones(datos_invalidos)


def test_crear_informe_conserva_el_origen(operaciones: pd.DataFrame) -> None:
    original = operaciones.copy(deep=True)
    crear_informe(operaciones)
    assert_frame_equal(operaciones, original)


def test_crear_informe_agrega_confirmadas(operaciones: pd.DataFrame) -> None:
    esperado = pd.DataFrame(
        {
            "mes": ["2025-01", "2025-02"],
            "region": ["norte", "sur"],
            "canal": ["app", "app"],
            "importe_total": [120.0, 200.0],
            "operaciones": [1, 1],
        }
    )
    assert_frame_equal(crear_informe(operaciones), esperado)


def test_crear_informe_incluye_el_umbral(operaciones: pd.DataFrame) -> None:
    datos = operaciones.iloc[[0]].copy()
    datos.loc[:, "importe"] = 120.0
    informe = crear_informe(datos, importe_minimo=120.0)
    assert informe.loc[0, "operaciones"] == 1
