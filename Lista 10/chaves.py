from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa


def gerar_chaves():
    chaves_a = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048
    )

    chaves_b = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048
    )

    return chaves_a, chaves_b


def salvar_chaves_privada(par_chaves, nome):
    pem = par_chaves.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.PKCS8,
        encryption_algorithm=serialization.NoEncryption()
    )

    with open(nome, 'wb') as f:
        f.write(pem)


def salvar_chaves_publica(par_chaves, nome):
    pem = par_chaves.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo
    )

    with open(nome, 'wb') as f:
        f.write(pem)


chaves_a, chaves_b = gerar_chaves()

chave_publica_a = chaves_a.public_key()
chave_publica_b = chaves_b.public_key()


salvar_chaves_privada(chaves_a, 'chave_a.pem')
salvar_chaves_publica(chave_publica_a, 'chave_a_public.pem')
salvar_chaves_privada(chaves_b, 'chave_b.pem')
salvar_chaves_publica(chave_publica_b, 'chave_b_public.pem')
