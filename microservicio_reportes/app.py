from flask import Flask, jsonify, request, send_file
import mysql.connector
from pymongo import MongoClient
from datetime import datetime
import pandas as pd
from fpdf import FPDF
from datetime import datetime
import io

app = Flask(__name__)

# Conexión a MySQL (tareas)
mysql_conn = mysql.connector.connect(
    host="tareas-db",  
    user="user_tareas", 
    password="pass_tareas",
    database="tareas_db"
)

# Conexión a MongoDB (historial)
mongo_client = MongoClient("mongodb://reportes-mongo:27017/")
mongo_db = mongo_client["reportes-mongo"]
historial_collection = mongo_db["historial"]

@app.route("/reporte/tareas", methods=["GET"])
def reporte_tareas():
    estado = request.args.get("estado")
    formato = request.args.get("formato", "json")  # json, pdf, excel

    cursor = mysql_conn.cursor(dictionary=True)
    
    if estado:
        cursor.execute("SELECT * FROM tasks WHERE status = %s", (estado,))
    else:
        cursor.execute("SELECT * FROM tasks")
    
    tareas = cursor.fetchall()
    cursor.close()

    # Guardar en historial (MongoDB)
    historial_collection.insert_one({
        "tipo": "reporte_tareas",
        "filtro_estado": estado if estado else "todos",
        "cantidad": len(tareas),
        "formato": formato,
        "fecha": datetime.now()
    })

    # ---------- Formatos ----------
    if formato == "json":
        return jsonify(tareas)

    elif formato == "excel":
        df = pd.DataFrame(tareas)
        
        nombre = f"reporte_tareas_{datetime.now().strftime('%Y%m%d_%H%M%S')}.xlsx"
        ruta_archivo = rf"C:\Users\lopez\Desktop\reportes\{nombre}"
        df.to_excel(ruta_archivo, index=False)
        
        return send_file(
            ruta_archivo,
            as_attachment=True,
            download_name=nombre,  
            mimetype="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"       
        )

    elif formato == "pdf":
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)

        pdf.cell(200, 10, "Reporte de Tareas", ln=True, align="C")
        pdf.ln(10)

        for tarea in tareas:
            pdf.multi_cell(0, 10, f"ID: {tarea['id']} | Nombre: {tarea['title']} | Estado: {tarea['status']}")
            pdf.ln(2)

        nombre = f"reporte_tareas_{datetime.now().strftime('%Y%m%d_%H%M%S')}.pdf"
        ruta_archivo = f"C:\\Users\\lopez\\Desktop\\reportes\\{nombre}"
        pdf.output(ruta_archivo)

        return jsonify({"mensaje": "Reporte PDF generado", "ruta": ruta_archivo})

    else:
        return jsonify({"error": "Formato no soportado"}), 400


if __name__ == "__main__":
    app.run(debug=True, port=5001)
