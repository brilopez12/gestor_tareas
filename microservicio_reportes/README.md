# 📊 Microservicio de Reportes
Este microservicio se encarga de hacer los reportes de acuerdo a al estado de la tarea tanto en pdf como en excel y guarda el historial de los reportes que se hagan.

## 🛠️ Tecnologías

* **Framework:** Flask (Python)
* **Librerías:** pandas, openpyxl, fpdf

---

## 📦 Requisitos

* Python 3.x
* Flask
* Pandas
* OpenPyXL
* FPDF
* mysql-connector-python

---

## ⚙️ Instalación

```bash
# Entrar al directorio del microservicio
cd microservicio_reportes


# Instalar dependencias necesarias
pip install flask pandas openpyxl fpdf mysql-connector-python
```

---

## 🚀 Ejecución

```bash
python app.py
```

La API quedará disponible en:

```
http://127.0.0.1:5000
```

---

## 📂 Endpoints principales

### 1. Generar reporte en Excel

```
GET /reporte/tareas?formato=excel
```

📥 Descarga un archivo Excel con las tareas.

### 2. Generar reporte en PDF

```
GET /reporte/tareas?formato=pdf
```

📥 Descarga un archivo PDF con las tareas.

---

## ⚠️ Nota sobre rutas de descarga

Los reportes se guardan en una carpeta **preconfigurada en el código**, por ejemplo:

```python
ruta_archivo = r"C:\Users\lopez\Desktop\reportes\reporte.xlsx"
```

👉 Si deseas usarlos en otro equipo, debes **modificar esta ruta en `app.py`** para que apunte a una carpeta existente en tu máquina.

---
