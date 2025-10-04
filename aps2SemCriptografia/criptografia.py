from Crypto.Cipher import AES 
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad

def criptografia_aes(texto: bytes, chave: bytes) -> tuple[bytes, bytes]:
    cipher = AES.new(chave, AES.MODE_CBC)
    texto_padded = pad(texto, AES.block_size)
    texto_cifrado = cipher.encrypt(texto_padded)

    return cipher.iv, texto_cifrado 

def descriptografar_aes(iv: bytes, texto_cifrado: bytes, chave: bytes) -> bytes:
    cipher = AES.new(chave, AES.MODE_CBC, iv=iv)
    
    texto_descriptografado_padded = cipher.decrypt(texto_cifrado)
    texto_descriptografado = unpad(texto_descriptografado_padded, AES.block_size)

    return texto_descriptografado

if __name__ == "__main__":
    try:
        chave_secreta = get_random_bytes(16)

        print("--- INICIANDO CRIPTOGRAFIA ---")
        text_original = input("Digite uma frase para ser criptografada(No máx. 128 caracteres): \n")
        if len(text_original) > 128:
            print("ERRO!! O texto não pode ter mais de 128 caracteres.")
        else:
            text_original_bytes = text_original.encode('utf-8')

            iv_gerado, texto_criptografado = criptografia_aes(text_original_bytes, chave_secreta)

            print("\n --  CRIPTOGRAFANDO TEXTO... --")
            print(f"Texto Original: {text_original}")
            print(f"Chave Secreta: {chave_secreta.hex()}")
            print(f"Vetor de Inicialização(iv): {iv_gerado.hex()}")
            print(f"Texto Criptografado: {texto_criptografado.hex()}")

            texto_descriptografado_bytes = descriptografar_aes(iv_gerado, texto_criptografado, chave_secreta)
            texto_descriptogrado_original = texto_descriptografado_bytes.decode('utf-8')

            print("\n -- DESCRIPTOGRAFANDO TEXTO...  --")
            print(f"Texto Descriptografado: {texto_descriptogrado_original}")

    except Exception as e:
        print(f"\n Ocorreu um erro: {e}")