from flask import Flask, render_template, request, jsonify
from criptografia import criptografar, descriptografar

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/criptografar', methods=['POST'])
def handle_criptografar():
    dados = request.get_json()
    texto = dados.get('texto', '')
    if not texto:
        return jsonify({'erro': 'Nenhum texto fornecido'}), 400

    resultado = criptografar(texto)
    return jsonify({'resultado': resultado})

@app.route('/descriptografar', methods=['POST'])
def handle_descriptografar():
    dados = request.get_json()
    texto = dados.get('texto', '')
    if not texto:
        return jsonify({'erro': 'Nenhum texto fornecido'}), 400

    resultado = descriptografar(texto)
    return jsonify({'resultado': resultado})

if __name__ == '__main__':
    app.run(debug=True)
