# João Henrique Cardoso Bragantino

alphabet = [chr(i) for i in range(ord('A'), ord('Z') + 1)]


def cipher(text, key):
    key_number = []
    ciphed_text = []
    count = 0
    for letter in key:
        key_number.append(alphabet.index(letter))

    for letter in text:
        if count > len(key_number)-1:
            count = 0
        new_chr = ord(letter)+key_number[count]
        while new_chr > ord('Z'):
            new_chr = ord(alphabet[(new_chr - ord('Z'))-1])
        ciphed_text.append(chr(new_chr))
        count += 1

    for letter in ciphed_text:
        print(letter, end="")


def decipher(text, key):
    key_number = []
    deciphed_text = []
    count = 0
    for letter in key:
        key_number.append(alphabet.index(letter))

    for letter in text:
        if count > len(key_number)-1:
            count = 0
        new_chr = ord(letter)-key_number[count]
        while new_chr < ord('A'):
            new_chr = ord(alphabet[(new_chr - ord('A'))])
        deciphed_text.append(chr(new_chr))
        count += 1

    for letter in deciphed_text:
        print(letter, end="")


if __name__ == "__main__":
    opt = input("Cifrar/Decifrar [C/D]: ").upper().replace(" ", "")
    text = input("Texto: ").upper().replace(" ", "")
    key = input("Chave: ").upper().replace(" ", "")

    if opt == "C":
        cipher(text, key)
    elif opt == "D":
        decipher(text, key)
    else:
        pass
