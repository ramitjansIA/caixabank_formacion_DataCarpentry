<p align="center">
  <img src="11_proyecto_profesional_cierre/recursos/logos/upc.png" height="60" alt="UPC"/>
  &nbsp;&nbsp;&nbsp;&nbsp;
  <img src="11_proyecto_profesional_cierre/recursos/logos/caixabank.png" height="60" alt="CaixaBank"/>
</p>

<h1 align="center">Data Carpentry · Python profesional y eficiente</h1>
<h3 align="center">CaixaBank · Formación en análisis de datos</h3>
<p align="center"><strong>14, 15 y 16 de octubre de 2026</strong></p>

---

## 📌 Descripción

Este repositorio reúne los materiales del **curso de Data Carpentry**, orientado a mejorar la calidad, el rendimiento y la reproducibilidad del código Python utilizado en el análisis de datos.

El curso combina:

* Fundamentos de código limpio y organización de proyectos.
* Trabajo práctico con Pandas avanzado y comparaciones con Polars.
* Medición y optimización del rendimiento y del consumo de memoria.
* Construcción de un proyecto reproducible, con configuración, pruebas y herramientas de automatización.

El objetivo principal es aprender a **transformar un notebook exploratorio en un pipeline mantenible, verificable y eficiente**, con un enfoque aplicado a contextos de trabajo analítico.

---

## 🎯 Objetivos del curso

Al finalizar el curso, el participante será capaz de:

* Organizar un proyecto Python y estructurar sus módulos e imports.
* Diseñar funciones reutilizables, documentarlas y validar sus entradas.
* Utilizar logging y gestionar excepciones de forma coherente.
* Aplicar selección, agregaciones, transformaciones, pivots y joins en Pandas.
* Detectar costes de tiempo y memoria mediante mediciones y profiling.
* Comparar vectorización, procesamiento por bloques y técnicas de ejecución eficiente.
* Comprobar que una optimización conserva el resultado esperado.
* Preparar un repositorio reproducible con entornos, configuración y pruebas.

---

## 🧱 Estructura del curso

📋 El horario y los materiales de cada bloque se detallan a continuación.

Las carpetas están numeradas por **orden temático**. Algunos temas comparten una misma franja horaria; la numeración no representa once sesiones con horarios independientes.

### 📅 Día 1 · Miércoles 14 de octubre · Código Python profesional

**Docentes:** Sergi Ramirez y Andrea Cardona.

* **10:00–11:00 · Presentación y paso del notebook al proyecto.**
  [Notebook guía](01_del_notebook_al_proyecto/notebook_guia.ipynb)
* **11:30–13:30 · Código limpio, estructura, nomenclatura e imports.**
  [Notebook de alumnado](02_clean_code_estructura_imports/notebook_alumnado.ipynb)
* **14:30–15:30 · Funciones reutilizables y modularización.**
  [Notebook de alumnado](03_funciones_modularizacion/notebook_alumnado.ipynb)
* **16:00–17:30 · Type hints, validación, docstrings, logging, excepciones y refactorización.**
  [Notebook de alumnado](04_calidad_refactorizacion/notebook_alumnado.ipynb) · [Soluciones](04_calidad_refactorizacion/notebook_solucion.ipynb) · [Presentación](04_calidad_refactorizacion/04_calidad_refactorizacion_presentacion.html)

💡 Los apartados de type hints, validación y docstrings se encuentran también en el notebook de la carpeta `03_funciones_modularizacion`. Se utilizan como continuación en el bloque de las 16:00.

---

### 📅 Día 2 · Jueves 15 de octubre · Pandas avanzado y optimización de pipelines

**Docentes:** Sergi Ramirez y Andrea Cardona.

* **08:30–10:00 · Estructuras, selección eficiente, GroupBy y agregaciones.**
  [Estructuras y selección](05_pandas_estructuras_seleccion/notebook_alumnado.ipynb) · [GroupBy, agg y transform](06_groupby_agg_transform/notebook_alumnado.ipynb)
* **10:30–12:00 y 12:30–13:30 · Transform, apply, MultiIndex, pivots, joins y merges.**
  [Transform y apply](06_groupby_agg_transform/notebook_alumnado.ipynb) · [MultiIndex, pivots y joins](07_multiindex_pivot_joins_merges/notebook_alumnado.ipynb)
* **14:30–15:30 · Optimización de rendimiento con Pandas: complejidad, profiling y medición de tiempos.**
  [Notebook de alumnado](08_optimizacion_rendimiento_python/notebook_alumnado.ipynb) · [Soluciones](08_optimizacion_rendimiento_python/notebook_solucion.ipynb) · [Presentación](08_optimizacion_rendimiento_python/08_optimizacion_rendimiento_python_presentacion.html)
* **16:00–17:30 · Laboratorio: memoria y optimización de un pipeline de datos.**
  [Notebook de alumnado](09_laboratorio_pipeline/notebook_alumnado.ipynb) · [Soluciones](09_laboratorio_pipeline/notebook_solucion.ipynb) · [Presentación](09_laboratorio_pipeline/09_laboratorio_pipeline_presentacion.html)

---

### 📅 Día 3 · Viernes 16 de octubre · Programación eficiente y proyecto profesional

**Docente:** Andrea Cardona.

* **08:30–10:00 · Programación eficiente para analítica: iteradores, generadores, chunks y técnicas de ejecución.**
  [Notebook de alumnado](10_programacion_eficiente/notebook_alumnado.ipynb) · [Soluciones](10_programacion_eficiente/notebook_solucion.ipynb) · [Presentación](10_programacion_eficiente/10_programacion_eficiente_presentacion.html)
* **10:30–12:00 y 12:30–13:30 · Proyecto profesional y cierre del curso.**
  
  [Proyecto final: alumnado](11_proyecto_profesional_cierre/notebook_alumnado.ipynb) · [Soluciones](11_proyecto_profesional_cierre/notebook_solucion.ipynb) · [Presentación](11_proyecto_profesional_cierre/11_proyecto_profesional_cierre_presentacion.html)

Los materiales incluyen threads, Numba y Polars, además de repositorios, entornos virtuales, configuración, pruebas y automatización. El cronograma también contempla multiprocessing; su práctica debe confirmarse con el equipo docente.

---

## 📂 Contenido del repositorio

| Carpeta | Contenido |
|---|---|
| `01_del_notebook_al_proyecto/` | Del análisis exploratorio al proyecto mantenible |
| `02_clean_code_estructura_imports/` | Código limpio, estructura e imports |
| `03_funciones_modularizacion/` | Funciones, type hints, validación y docstrings |
| `04_calidad_refactorizacion/` | Calidad, logging, excepciones y refactorización |
| `05_pandas_estructuras_seleccion/` | Estructuras y selección eficiente |
| `06_groupby_agg_transform/` | Agregaciones, transform y apply |
| `07_multiindex_pivot_joins_merges/` | MultiIndex, pivots y combinación de datos |
| `08_optimizacion_rendimiento_python/` | Complejidad, medición y profiling |
| `09_laboratorio_pipeline/` | Memoria, vectorización y laboratorio práctico |
| `10_programacion_eficiente/` | Chunks, generadores, NumPy, Polars, Numba y threads |
| `11_proyecto_profesional_cierre/` | Notebooks, plantilla y solución del proyecto final |
| `archivo/old/` | Versiones anteriores conservadas para consulta |
| `documentacion/` | Cronograma, mapa de movimientos y README original |

**Tipos de material:**

* `notebook_guia.ipynb`: notebook original con explicación, ejemplos y ejercicios.
* `notebook_alumnado.ipynb`: material de trabajo con actividades por completar.
* `notebook_solucion.ipynb`: versión con soluciones para corrección y consulta.
* `presentacion.html`: presentación del bloque; abrir en un navegador.
* `README.md`: orientación específica de cada carpeta.

Las carpetas procedentes de los notebooks sueltos contienen un notebook guía. Las cinco carpetas prácticas ya preparadas conservan sus notebooks de alumnado y soluciones, presentaciones y recursos.

---

## ⚙️ Requisitos

Se recomienda **Python 3.11 o superior**: algunos notebooks utilizan `tomllib`, incluido en la biblioteca estándar desde Python 3.11.

Herramientas recomendadas:

* Visual Studio Code con las extensiones **Python** y **Jupyter**, o JupyterLab.
* Git, si se trabaja con el repositorio remoto.
* Un entorno virtual para aislar las dependencias.

Principales librerías y herramientas utilizadas:

* Pandas, NumPy y Polars.
* Matplotlib y Seaborn.
* Numba.
* Pytest, Ruff, Black y mypy en el proyecto final.
* FastAPI y Uvicorn para la extensión de API.

El repositorio no incluye un `requirements.txt` general. Para preparar el entorno de los notebooks:

```bash
python -m pip install jupyterlab ipykernel pandas numpy polars matplotlib seaborn numba
```

Estas dependencias no están fijadas a versiones concretas. Para el proyecto final, utilizar además su `pyproject.toml`, según las instrucciones de ese bloque.

---

## ▶️ Uso

### 1. Obtener y abrir el proyecto

Descargar y descomprimir los materiales, o clonar el repositorio sustituyendo los marcadores por su URL y nombre reales:

```bash
git clone <URL_DEL_REPOSITORIO>
cd <NOMBRE_DEL_REPOSITORIO>
code .
```

La carpeta raíz es la que contiene este README y las carpetas `01_…` a `11_…`.

### 2. Crear y activar un entorno virtual

```bash
python -m venv .venv
```

**Windows · PowerShell:**

```powershell
.\.venv\Scripts\Activate.ps1
```

**macOS / Linux:**

```bash
source .venv/bin/activate
```

Instalar las dependencias con el comando del apartado de requisitos.

### 3. Seleccionar el entorno en VS Code

* Instalar las extensiones **Python** y **Jupyter**.
* Seleccionar el intérprete de `.venv` mediante **Python: Select Interpreter**.
* Abrir el notebook y seleccionar ese mismo entorno como kernel.

### 4. Ejecutar los notebooks

* Seguir el orden de las carpetas y las indicaciones del docente.
* Ejecutar las celdas de forma secuencial con `Shift + Enter`.
* Trabajar con la carpeta del notebook como directorio de ejecución para resolver correctamente las rutas relativas.
* Utilizar el notebook de alumnado para las actividades y la solución durante la corrección.

Como alternativa a VS Code, iniciar JupyterLab desde la carpeta de la sesión:

```bash
python -m jupyterlab
```

### 5. Preparar el proyecto final

Desde la raíz del repositorio, con el entorno virtual activado:

```bash
cd 11_proyecto_profesional_cierre/plantilla_informe_operaciones
python -m pip install -e ".[dev,api]"
```

Después, volver a `11_proyecto_profesional_cierre/` para ejecutar su notebook. La carpeta `solucion_informe_operaciones/` conserva la implementación resuelta para consulta.

---

## 🧪 Metodología

El enfoque del curso es **práctico y guiado**:

* Partir de un problema y observar su comportamiento.
* Identificar errores, costes o dificultades de mantenimiento.
* Aplicar una mejora de forma gradual.
* Medir y comparar los resultados.
* Validar que se conserva el contrato de salida.
* Consolidar lo aprendido mediante ejercicios y un proyecto final.

---

## 📊 Filosofía del curso

Más allá de conseguir que el código se ejecute, el curso pone énfasis en:

* La **legibilidad** y el mantenimiento.
* La **reproducibilidad** del entorno y del proceso.
* La **trazabilidad** de los errores y las decisiones.
* La **eficiencia** demostrada mediante mediciones.
* La **corrección** de los resultados después de cada cambio.

> *Un pipeline debe producir resultados correctos, poder mantenerse y permitir comprobar sus mejoras.*

---

## ⚠️ Consideraciones importantes

* Seguir las instrucciones de datos y configuración de cada notebook; el curso no utiliza una única variable objetivo común.
* Algunos ejemplos provocan errores deliberadamente para estudiar su diagnóstico y corrección.
* Los benchmarks dependen del equipo, del volumen de datos y del entorno de ejecución.
* `archivo/old/` contiene versiones históricas y no forma parte del recorrido principal.
* Conservar los recursos, plantillas y soluciones junto a sus notebooks para mantener las rutas relativas.

---

## 👨‍🏫 Público objetivo

* Analistas de datos y profesionales de perfiles cuantitativos.
* Data scientists con conocimientos básicos de Python y Pandas.
* Profesionales que desean mejorar sus notebooks y pipelines.
* Equipos que necesitan compartir código mantenible y reproducible.

Se recomienda conocer previamente funciones básicas de Python, estructuras de datos y operaciones habituales con DataFrames.

---

## 📬 Contacto

Para dudas, mejoras o incidencias, utilizar los issues del repositorio o contactar con el equipo docente.

**Docentes:** Sergi Ramirez y Andrea Cardona.

**Contacto:** sergi.ramirez@upc.edu

---

## 📄 Licencia

Este material está destinado a uso formativo interno.
Para otros usos, consultar con los responsables del curso.

---

**CaixaBank · Data Carpentry · Python y análisis de datos**
