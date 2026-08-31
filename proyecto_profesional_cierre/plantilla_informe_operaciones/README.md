# Informe de operaciones

Genera un informe mensual de operaciones confirmadas por región y canal.

## Instalación

```bash
python -m venv .venv
python -m pip install -e ".[dev]"
```

## Ejecución

```bash
python -m informe_operaciones.cli --config config/config.json
```

## Verificación

```bash
python -m pytest -q
python scripts/check_quality.py
```

## Contrato de salida

<!-- TODO 7: documenta columnas, ubicación de salida y comportamiento ante datos inválidos. -->
