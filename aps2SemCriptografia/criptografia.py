""""
    Para realizar a criptografia baixamos a biblioteca pycryptodome
    Que irá permitir utilizar suas classes prontas
    Para baixar, abra seu terminal e digite:
        pip install pycryptodome
"""
# Importação das bibliotecas necessárias para criptografia AES
from Crypto.Cipher import AES  # Importa o algoritmo AES
from Crypto.Random import get_random_bytes  # Para geração de bytes aleatórios
from Crypto.Util.Padding import pad, unpad  # Para padding do texto


# Gera uma chave aleatória de 16 bytes (128 bits) para o AES-128
# Esta chave é gerada uma vez quando o módulo é importado e permanece constante durante a execução
CHAVE_SECRETA = get_random_bytes(16)


def criptografar(texto: str) -> str:
    """
    Criptografa um texto usando AES no modo CBC.
    Args:
        texto (str): O texto a ser criptografado (máximo 128 caracteres)
    Returns:
        str: Texto criptografado em formato hexadecimal
    """
    # Verifica se o texto não excede o limite de 128 caracteres
    if len(texto) > 128:
        return "Erro: texto não pode ter mais de 128 caracteres."

    # Converte o texto para bytes usando UTF-8
    texto_bytes = texto.encode('utf-8')
    # Cria um novo objeto AES no modo CBC com a chave secreta
    cipher = AES.new(CHAVE_SECRETA, AES.MODE_CBC)
    # Adiciona padding ao texto para garantir que tenha o tamanho correto do bloco
    texto_padded = pad(texto_bytes, AES.block_size)
    # Realiza a criptografia
    texto_cifrado = cipher.encrypt(texto_padded)

    # Concatena o IV (vetor de inicialização) com o texto cifrado e converte para hexadecimal
    return (cipher.iv + texto_cifrado).hex()


def descriptografar(texto_hex: str) -> str:
    """
    Descriptografa um texto que foi criptografado com AES no modo CBC.
    Args:
        texto_hex (str): O texto criptografado em formato hexadecimal
    Returns:
        str: Texto descriptografado ou mensagem de erro
    """
    try:
        # Converte o texto hexadecimal de volta para bytes
        dados = bytes.fromhex(texto_hex)
        # Extrai o IV dos primeiros bytes
        iv = dados[:AES.block_size]
        # Extrai o texto cifrado (o resto dos bytes após o IV)
        texto_cifrado = dados[AES.block_size:]

        # Cria um novo objeto AES para descriptografia usando o IV original
        cipher = AES.new(CHAVE_SECRETA, AES.MODE_CBC, iv)
        # Descriptografa e remove o padding
        texto_descriptografado = unpad(cipher.decrypt(texto_cifrado), AES.block_size)
        # Converte os bytes de volta para string
        return texto_descriptografado.decode('utf-8')
    except Exception:
        # Retorna mensagem de erro se algo der errado durante a descriptografia
        return "Erro ao descriptografar. Texto inválido ou chave incorreta."
