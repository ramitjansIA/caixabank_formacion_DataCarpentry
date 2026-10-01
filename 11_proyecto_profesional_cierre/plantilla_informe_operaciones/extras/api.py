"""Extensión: una API mínima debe llamar a la lógica ya testeada, no duplicarla."""
from fastapi import FastAPI

app = FastAPI(title="Informe de operaciones")


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}
