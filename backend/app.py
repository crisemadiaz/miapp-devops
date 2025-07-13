# backend/app.py
from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Habilita CORS para todas las rutas

@app.route('/api')
@app.route('/api/')
def home():
    return jsonify({"mensaje": "Hola desde el backend Flask usando /api/"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
