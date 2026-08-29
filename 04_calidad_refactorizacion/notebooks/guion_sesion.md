# Guion de sesión: calidad de código y refactorización

**Duración:** 90 minutos.

## Resultado de aprendizaje

Al finalizar, el alumnado podrá transformar una etapa analítica frágil en un pipeline que:

- distingue un error estructural de un problema de calidad de filas;
- mantiene un registro útil de lo que ocurre durante la ejecución;
- separa validación, limpieza, transformación y resumen;
- conserva la entrada original;
- ofrece un resultado equivalente sobre datos válidos;
- permite justificar qué incidencias detienen el proceso y cuáles se documentan.

## Contexto profesional

Un equipo de operaciones recibe cada mañana las transacciones del día anterior. El notebook que alimenta un informe por canal y región ha producido una cifra incorrecta sin avisar con claridad. Se dispone de un extracto con filas de calidad deficiente y de un pipeline heredado que mezcla todas las responsabilidades.

La regla de operación acordada es:

| Tipo de incidencia | Tratamiento |
|---|---|
| Falta una columna obligatoria | Detener: no existe un contrato de entrada válido |
| Fecha o importe inválidos en una fila | Excluir la fila y registrar cuántas se han descartado |
| Canal no reconocido | Mantener la fila, clasificarla como `otro` y registrar una advertencia |
| Importe negativo | Excluir la fila y registrar una advertencia |

## Distribución de tiempo

| Minutos | Bloque | Resultado visible |
|---:|---|---|
| 0–10 | Incidente y diagnóstico | El alumnado identifica dependencias, `print()` y manejo de errores problemático |
| 10–25 | Contrato de datos y logging | Logger reutilizable y reglas de severidad justificadas |
| 25–45 | Refactorización guiada | Funciones de validar, limpiar, transformar y resumir |
| 45–65 | Aplicación profesional | Pipeline robusto frente a un extracto con incidencias realistas |
| 65–78 | Puesta en común | Comparación de decisiones, logs y resultados |
| 78–87 | Extensión avanzada | Duración por etapa, excepción de dominio y encadenamiento |
| 87–90 | Cierre | Checklist y puente hacia benchmarking |

## Arquitectura del notebook

### Recorrido común

1. Crear datos sintéticos representativos y un extracto defectuoso.
2. Ejecutar e inspeccionar un fragmento heredado.
3. Declarar el contrato de entrada y las políticas de error.
4. Configurar un logger repetible en un notebook.
5. Crear `ContratoDatosError`.
6. Implementar `validar_estructura`, `limpiar_operaciones`, `clasificar_revision`, `resumir_operaciones` y `ejecutar_pipeline`.
7. Validar que la entrada no se modifica y que las métricas cuadran.

### Aplicación profesional

La práctica presenta una única secuencia de ejercicios numerados sobre la recuperación de un informe diario. Las celdas de comprobación, ejecución y ayuda aparecen entre ejercicios cuando son necesarias, sin separar la práctica en partes. Cada ejercicio ofrece una celda vacía para resolver desde cero y un bloque HTML desplegable `Obtener esqueleto de ayuda` con la estructura necesaria si aparece un bloqueo. La práctica entrega una tabla de calidad y una recomendación de publicación.

### Extensión

Se carga una fuente CSV ausente o inválida, se registra el incidente en un fichero de log y se encapsula el error técnico en una excepción de dominio. Esta parte queda desarrollada para poder ejecutarla en aula o estudiar después.

### Retos opcionales

- Conservar `chat` como canal válido y seguir normalizando otros canales nuevos como `otro`.
- Convertir las métricas de calidad del log en una tabla de monitorización.

### Banco de ejercicios de consolidación

El notebook incluye cinco ejercicios adicionales inspirados en la progresión del material base: niveles de logging, contrato de datos, extracción de una función, prioridad avanzada y comprobaciones de regresión. No forman parte del mínimo de 90 minutos; permiten adaptar la práctica al ritmo del grupo sin perder contenido técnico.

## Artefactos que pasan a la siguiente sesión

- funciones puras de validación, limpieza, transformación y resumen;
- contrato de datos;
- logger y política de incidencias;
- baseline funcional y conjunto de validaciones.

La siguiente sesión medirá ese pipeline antes de optimizarlo.
