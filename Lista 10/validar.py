import hashlib
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.asymmetric import padding


def validar(caminho_doc, caminho_assinatura, caminho_chave_publica):
    with open(caminho_chave_publica, 'rb') as f:
        chave_publica = serialization.load_pem_public_key(
            f.read()
        )

    with open(caminho_doc, 'rb') as f:
        documento = f.read()

    document_hash = hashlib.sha256(documento).digest()

    with open(caminho_assinatura, 'rb') as f:
        assinatura = f.read()

    try:
        chave_publica.verify(
            assinatura,
            document_hash,
            padding.PSS(
                mgf=padding.MGF1(hashes.SHA256()),
                salt_length=padding.PSS.MAX_LENGTH
            ),
            hashes.SHA256()
        )
        print("A assinatura é válida. O arquivo é autêntico e foi assinado por A.")
    except:
        print(
            "A assinatura é inválida. O arquivo não é autêntico ou não foi assinado por A.")


caminho_doc = input("Digite o caminho do documento: ")

caminho_assinatura = input("Digite o caminho da assinatura (assinatura.bin): ")

caminho_chave_publica = input(
    "Digite o caminho da chave pública de A (chave_a_public.pem): ")

validar(caminho_doc, caminho_assinatura, caminho_chave_publica)
