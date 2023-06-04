from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization, padding, hashes
from cryptography.hazmat.primitives.asymmetric import padding as asymmetric_padding
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes

with open('chave_privada.pem', 'rb') as f:
    chave_privada = serialization.load_pem_private_key(
        f.read(),
        password=None,
        backend=default_backend()
    )

chave_encriptada = "chave_cripto.bin"
with open(chave_encriptada, 'rb') as f:
    chave_simetrica_cripto = f.read()

chave_simetrica = chave_privada.decrypt(
    chave_simetrica_cripto,
    asymmetric_padding.OAEP(
        mgf=asymmetric_padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    )
)

arquivo_cripto = input("Digite o nome do arquivo criptografado: ")

with open(arquivo_cripto, 'rb') as f:
    texto_cifrado = f.read()

vetor_de_iniciação = texto_cifrado[:16]
cifra = Cipher(algorithms.AES(chave_simetrica), modes.CBC(vetor_de_iniciação), backend=default_backend())
encriptador = cifra.decryptor()

decriptografado = encriptador.update(texto_cifrado[16:]) + encriptador.finalize()

unpadder = padding.PKCS7(algorithms.AES.block_size).unpadder()
texto = unpadder.update(decriptografado) + unpadder.finalize()

arquivo_decriptografado = f"decripto_{arquivo_cripto}"
with open(arquivo_decriptografado, 'wb') as f:
    f.write(texto)

print("Chave simétrica decriptografada:", chave_simetrica)

print("Arquivo decriptografado foi salvo.")


