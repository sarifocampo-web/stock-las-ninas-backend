from flask import Flask, jsonify, request
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

# ===============================
# DATOS (en memoria)
# ===============================
productos = [
    {"nombre": "Leche", "categoria": "Alimentos", "stock": 1, "minimo": 2},
    {"nombre": "Fideos", "categoria": "Alimentos", "stock": 0, "minimo": 1},
    {"nombre": "Detergente", "categoria": "Limpieza", "stock": 1, "minimo": 1},
    {"nombre": "Tomate", "categoria": "Verdulería", "stock": 0, "minimo": 2}
]

# ===============================
# RUTAS
# ===============================
@app.route("/")
def home():
    return "Backend Stock Las Niñas funcionando 🟢"

@app.route("/productos", methods=["GET"])
def obtener_productos():
    return jsonify(productos)

@app.route("/productos", methods=["POST"])
def guardar_productos():
    global productos
    productos = request.json
    return jsonify({"ok": True})

# ===============================
# ARRANQUE (RENDER COMPATIBLE)
# ===============================
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(
        host="0.0.0.0",
        port=port,
        debug=False
    )

