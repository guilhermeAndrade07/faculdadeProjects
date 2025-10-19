from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad
import base64

# Gera uma chave aleatória de 16 bytes (AES-128)
CHAVE_SECRETA = get_random_bytes(16)

def criptografar(texto: str) -> str:
    if len(texto) > 128:
        return "Erro: texto não pode ter mais de 128 caracteres."

    texto_bytes = texto.encode('utf-8')
    cipher = AES.new(CHAVE_SECRETA, AES.MODE_CBC)
    texto_padded = pad(texto_bytes, AES.block_size)
    texto_cifrado = cipher.encrypt(texto_padded)

    # Junta IV + texto cifrado e retorna em HEX (sem Base64)
    return (cipher.iv + texto_cifrado).hex()

def descriptografar(texto_hex: str) -> str:
    try:
        dados = bytes.fromhex(texto_hex)
        iv = dados[:AES.block_size]
        texto_cifrado = dados[AES.block_size:]

        cipher = AES.new(CHAVE_SECRETA, AES.MODE_CBC, iv)
        texto_descriptografado = unpad(cipher.decrypt(texto_cifrado), AES.block_size)
        return texto_descriptografado.decode('utf-8')
    except Exception:
        return "Erro ao descriptografar. Texto inválido ou chave incorreta."
