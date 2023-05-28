#João Bragantino

import hashlib

def calcular_hash_arquivo(nome_arquivo):
    # Cria um objeto hash SHA256
    hash_obj = hashlib.sha256()

    with open(nome_arquivo, 'rb') as arquivo:
        for bloco in iter(lambda: arquivo.read(4096), b''):
            hash_obj.update(bloco)

    return hash_obj.hexdigest()

def validar_integridade_arquivo(nome_arquivo, valor_hash):
    hash_calculado = calcular_hash_arquivo(nome_arquivo)

    if hash_calculado == valor_hash:
        print("O arquivo está íntegro.")
    else:
        print("O arquivo está corrompido.")

nome_arquivo = input("Digite o nome do arquivo: ")
valor_hash = input("Digite o valor de hash: ")

validar_integridade_arquivo(nome_arquivo, valor_hash)
