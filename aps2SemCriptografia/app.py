# Importação das dependências necessárias
from flask import Flask, render_template, request, jsonify  # Framework web e utilitários
from criptografia import criptografar, descriptografar  # Funções de criptografia personalizadas

# Inicialização da aplicação Flask
app = Flask(__name__)

@app.route('/')
def index():
    #Rota principal que renderiza a página inicial.
    return render_template('index.html')

@app.route('/criptografar', methods=['POST'])
def handle_criptografar():
    """
    Endpoint para criptografar texto.
    Aceita requisições POST com JSON contendo o texto a ser criptografado.
    Returns:
        JSON: Contém o resultado da criptografia ou mensagem de erro
        int: Código HTTP de status (200 para sucesso, 400 para erro)
    """
    # Obtém os dados JSON da requisição
    dados = request.get_json()
    # Extrai o texto do JSON, retorna string vazia se não existir
    texto = dados.get('texto', '')
    
    # Validação: verifica se o texto não está vazio
    if not texto:
        return jsonify({'erro': 'Nenhum texto fornecido'}), 400

    # Realiza a criptografia e retorna o resultado
    resultado = criptografar(texto)
    return jsonify({'resultado': resultado})

@app.route('/descriptografar', methods=['POST'])
def handle_descriptografar():
    """
    Endpoint para descriptografar texto.
    Aceita requisições POST com JSON contendo o texto criptografado.
    Returns:
        JSON: Contém o texto descriptografado ou mensagem de erro
        int: Código HTTP de status (200 para sucesso, 400 para erro)
    """
    # Obtém os dados JSON da requisição
    dados = request.get_json()
    # Extrai o texto do JSON, retorna string vazia se não existir
    texto = dados.get('texto', '')
    
    # Validação: verifica se o texto não está vazio
    if not texto:
        return jsonify({'erro': 'Nenhum texto fornecido'}), 400

    # Realiza a descriptografia e retorna o resultado
    resultado = descriptografar(texto)
    return jsonify({'resultado': resultado})

# Verifica se o script está sendo executado diretamente
if __name__ == '__main__':
    # Inicia o servidor Flask em modo de debug
    app.run(debug=True)
