from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Estado en memoria (por ahora)
productos = [
    {"nombre": "Leche", "categoria": "Alimentos", "stock": 1, "minimo": 2},
    {"nombre": "Fideos", "categoria": "Alimentos", "stock": 0, "minimo": 1},
    {"nombre": "Detergente", "categoria": "Limpieza", "stock": 1, "minimo": 1},
    {"nombre": "Tomate", "categoria": "Verdulería", "stock": 0, "minimo": 2}
]

@app.route("/productos", methods=["GET"])
def obtener_productos():
    return jsonify(productos)

@app.route("/productos", methods=["POST"])
def guardar_productos():
    global productos
    productos = request.get_json()
    return jsonify({"status": "ok"})

@app.route("/")
def home():
    return "Backend Stock Las Niñas funcionando 🟢"

if __name__ == "__main__":
    app.run()
