#João Henrique Cardoso Bragantino
def cipher(text, columns):
    matrix = []
    size = 0
    rows = 0
    counter = 0
    while size < len(text):
        rows += 1
        size = columns * rows
    
    for _ in range(rows):
        a = []
        for _ in range(columns):
            try:
                a.append(text[counter])
            except:
                a.append("X")
            counter += 1
        matrix.append(a)
    
    for column in range(columns):
        for row in range(rows):
            print(matrix[row][column], end=" ")
    print()

def decipher(text, columns):
    matrix = []
    size = 0
    rows = 0
    counter = 0
    while size < len(text):
        rows += 1
        size = columns * rows
    
    for _ in range(columns):
        a = []
        for _ in range(rows):
            a.append(text[counter])
            counter += 1
        matrix.append(a)

    for row in range(rows):
        for column in range(columns):
            print(matrix[column][row], end=" ")
    print()

if __name__ == "__main__":
    option      = input("Cifrar ou decifrar? [C/D] ").upper().strip()
    msg_text    = input("Texto: ").upper().replace(" ", "")
    columns     = int(input("Número de colunas: "))

    if option == "C":
        cipher(msg_text, columns)
    elif option == "D":
        decipher(msg_text, columns)
    else:
        print("Opção inválida")

