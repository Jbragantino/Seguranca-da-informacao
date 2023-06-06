import hashlib
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.asymmetric import padding


def assinar(caminho_doc, chave, caminho_assinatura):
    with open(chave, 'rb') as f:
        chave_priv = serialization.load_pem_private_key(
            f.read(),
            password=None
        )

    with open(caminho_doc, 'rb') as document_file:
        document = document_file.read()

    document_hash = hashlib.sha256(document).digest()

    assinatura = chave_priv.sign(
        document_hash,
        padding.PSS(
            mgf=padding.MGF1(hashes.SHA256()),
            salt_length=padding.PSS.MAX_LENGTH
        ),
        hashes.SHA256()
    )

    with open(caminho_assinatura, 'wb') as f:
        f.write(assinatura)


caminho_doc = input("Digite o caminho do documento a ser assinado: ")

chave = input("Digite o caminho da chave privada (chave_a.pem): ")

caminho_assinatura = 'caminho_assinatura.bin'

assinar(caminho_doc, chave, caminho_assinatura)

print("Documento assinado com sucesso. caminho_assinatura salva em", caminho_assinatura)
