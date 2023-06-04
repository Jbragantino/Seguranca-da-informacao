from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization, padding, hashes
from cryptography.hazmat.primitives.asymmetric import padding as asymmetric_padding
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
import os

with open('chave_publica.pem', 'rb') as f:
    chave_publica = serialization.load_pem_public_key(
        f.read(),
        backend=default_backend()
    )

chave_simetrica = os.urandom(32)

encrypted_symmetric_key = chave_publica.encrypt(
    chave_simetrica,
    asymmetric_padding.OAEP(
        mgf=asymmetric_padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    )
)

arquivo = input("Digite o nome do arquivo a ser criptografado: ")

with open(arquivo, 'rb') as f:
    texto = f.read()

padder = padding.PKCS7(algorithms.AES.block_size).padder()
padded_texto = padder.update(texto) + padder.finalize()

vetor_de_iniciação = os.urandom(16)

cifra = Cipher(algorithms.AES(chave_simetrica), modes.CBC(vetor_de_iniciação), backend=default_backend())
encriptador = cifra.encryptor()
texto_cifrado = encriptador.update(padded_texto) + encriptador.finalize()

arquivo_cripto = f"cripto_{arquivo}"
with open(arquivo_cripto, 'wb') as f:
    f.write(texto_cifrado)

chave_encriptada = f"chave_cripto.bin"
with open(chave_encriptada, 'wb') as f:
    f.write(encrypted_symmetric_key)

print("Arquivo criptografado e chave simétrica criptografada foram salvos.")
