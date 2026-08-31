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

## Configuración

`config/config.json` define las rutas de entrada y salida y el valor de `importe_minimo`. `.env.example` documenta variables locales o sensibles; el fichero `.env` real no se versiona.

## Contrato de salida

El CSV `data/processed/informe_operaciones.csv` contiene `mes`, `region`, `canal`, `importe_total` y `operaciones`. Solo incorpora operaciones confirmadas cuyo importe alcanza `importe_minimo`. Si falta una columna obligatoria o hay importes nulos, el pipeline termina con `ValueError` y no genera una salida parcial.
