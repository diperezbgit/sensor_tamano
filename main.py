from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import mysql.connector
from schemas import LecturaTamano

app = FastAPI()

origins = ['*']
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Configuración de conexión
host_name = "172.31.20.56"
port_number = "8005"
user_name = "root"
password_db = "utec"
database_name = "bd_api_iot"

# Echo test
@app.get("/")
def get_echo_test():
    return {"message": "Echo Test OK"}

# GET: Todas las lecturas de tamaño mineral
@app.get("/lecturas_tamano")
def get_all_tamano():
    db = mysql.connector.connect(host=host_name, port=port_number, user=user_name, password=password_db, database=database_name)
    cursor = db.cursor()
    cursor.execute("SELECT * FROM lecturas_tamaño_mineral")
    result = cursor.fetchall()
    cursor.close()
    db.close()
    return {"lecturas_tamano": result}

# GET: Lectura de tamaño mineral por ID
@app.get("/lecturas_tamano/{id}")
def get_tamano_by_id(id: int):
    db = mysql.connector.connect(host=host_name, port=port_number, user=user_name, password=password_db, database=database_name)
    cursor = db.cursor()
    cursor.execute("SELECT * FROM lecturas_tamaño_mineral WHERE id = %s", (id,))
    result = cursor.fetchone()
    cursor.close()
    db.close()
    return {"lectura_tamano": result}

# POST: Insertar nueva lectura de tamaño mineral
@app.post("/lecturas_tamano")
def add_tamano(item: LecturaTamano):
    db = mysql.connector.connect(host=host_name, port=port_number, user=user_name, password=password_db, database=database_name)
    cursor = db.cursor()
    sql = "INSERT INTO lecturas_tamaño_mineral (sensor_id, valor) VALUES (%s, %s)"
    val = (item.sensor_id, item.valor)
    cursor.execute(sql, val)
    db.commit()
    cursor.close()
    db.close()
    return {"message": "Lectura de tamaño mineral insertada correctamente"}

# PUT: Actualizar lectura de tamaño mineral por ID
@app.put("/lecturas_tamano/{id}")
def update_tamano(id: int, item: LecturaTamano):
    db = mysql.connector.connect(host=host_name, port=port_number, user=user_name, password=password_db, database=database_name)
    cursor = db.cursor()
    sql = "UPDATE lecturas_tamaño_mineral SET sensor_id = %s, valor = %s WHERE id = %s"
    val = (item.sensor_id, item.valor, id)
    cursor.execute(sql, val)
    db.commit()
    cursor.close()
    db.close()
    return {"message": "Lectura de tamaño mineral actualizada correctamente"}

# DELETE: Eliminar lectura de tamaño mineral por ID
@app.delete("/lecturas_tamano/{id}")
def delete_tamano(id: int):
    db = mysql.connector.connect(host=host_name, port=port_number, user=user_name, password=password_db, database=database_name)
    cursor = db.cursor()
    cursor.execute("DELETE FROM lecturas_tamaño_mineral WHERE id = %s", (id,))
    db.commit()
    cursor.close()
    db.close()
    return {"message": "Lectura de tamaño mineral eliminada correctamente"}