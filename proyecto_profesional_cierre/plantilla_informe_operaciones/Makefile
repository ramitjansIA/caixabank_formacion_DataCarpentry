.PHONY: pipeline test quality

pipeline:
	python -m informe_operaciones.cli --config config/config.json

test:
	python -m pytest -q

quality:
	python scripts/check_quality.py
