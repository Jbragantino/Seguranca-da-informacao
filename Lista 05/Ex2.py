#João Henrique Cardoso Bragantino
def cipher(text, rails):
    matrix = [[""] * len(text) for i in range(rails)]
    rail = 0

    for i in range(len(text)):
        matrix[rail][i] = text[i]
        if rail == rails - 1:
            dir = -1
        elif rail == 0:
            dir = 1
        rail += dir

    for row in range(rails):
        for column in range(len(text)):
            if matrix[row][column] != "":
                print(matrix[row][column], end=" ")
    print()

def decipher(text, rails):
    matrix = [[""] * len(text) for i in range(rails)]
    rail = 0
    counter = 0

    for i in range(len(text)):
        matrix[rail][i] = "@"
        if rail == rails - 1:
            dir = -1
        elif rail == 0:
            dir = 1
        rail += dir

    for row in range(rails):
        for column in range(len(text)):
            if matrix[row][column] == "@":
                matrix[row][column] = text[counter]
                counter += 1

    for column in range(len(text)):
        for row in range(rails):
            if matrix[row][column] != "":
                print(matrix[row][column], end=" ")
    print()

if __name__ == "__main__":
    option      = input("Cifrar ou decifrar? [C/D] ").upper().strip()
    msg_text    = input("Texto: ").upper().replace(" ", "")
    rails     = int(input("Número de trilhos: "))

    if option == "C":
        cipher(msg_text, rails)
    elif option == "D":
        decipher(msg_text, rails)
    else:
        print("Opção inválida")
