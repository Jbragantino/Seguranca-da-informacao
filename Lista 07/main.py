from Crypto.Cipher import Blowfish
from Crypto.Util.Padding import pad

def cipher(text):
    key = b'ABCDE'
    message = text

    cipher = Blowfish.new(key, Blowfish.MODE_CBC)

    message_bytes = message.encode('utf-8')
    padded_message_bytes = pad(message_bytes, Blowfish.block_size)

    ciphertext_bytes = cipher.encrypt(padded_message_bytes)

    ciphertext = ciphertext_bytes.hex()

    print(f'Texto cifrado: {ciphertext}')
    print(f'Extensão do texto cifrado: {len(ciphertext_bytes)} bytes')


if __name__ == "__main__":
    text = input("Digite a messagem a ser decifrada: ")
    cipher(text)

