from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa

chave_privada = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048,
    backend=default_backend()
)

chave_publica = chave_privada.public_key()

modulo = chave_privada.private_numbers().public_numbers.n
expoente_privado = chave_privada.private_numbers().d
expoente_publico = chave_publica.public_numbers().e

with open('chave_privada.pem', 'wb') as f:
    f.write(chave_privada.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.PKCS8,
        encryption_algorithm=serialization.NoEncryption()
    ))

with open('chave_publica.pem', 'wb') as f:
    f.write(chave_publica.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo
    ))

print("Módulo:", modulo)
print("Expoente privado:", expoente_privado)
print("Expoente público:", expoente_publico)