def gerar_matriz(chave):
    alfabeto = "abcdefghiklmnopqrstuvwxyz" 
    matriz = []
    letras_usadas = set()

    for char in chave.lower():
        if char not in letras_usadas and char in alfabeto:
            matriz.append(char)
            letras_usadas.add(char)

    for char in alfabeto:
        if char not in letras_usadas:
            matriz.append(char)

    return [matriz[i:i + 5] for i in range(0, 25, 5)]

def encontrar_posicao(matriz, char):
    for i, linha in enumerate(matriz):
        if char in linha:
            return i, linha.index(char)
    return None

def cifra_playfair(mensagem, chave, modo='cifrar'):
    mensagem = mensagem.lower().replace("j", "i")
    matriz = gerar_matriz(chave)
    mensagem_cifrada = ""
    i = 0

    while i < len(mensagem):
        a = mensagem[i]
        b = mensagem[i + 1] if i + 1 < len(mensagem) else 'x'

        if a == b:
            b = 'x'
            i -= 1

        linha_a, coluna_a = encontrar_posicao(matriz, a)
        linha_b, coluna_b = encontrar_posicao(matriz, b)

        if linha_a == linha_b:
            coluna_a = (coluna_a + 1) % 5 if modo == 'cifrar' else (coluna_a - 1) % 5
            coluna_b = (coluna_b + 1) % 5 if modo == 'cifrar' else (coluna_b - 1) % 5
        elif coluna_a == coluna_b:
            linha_a = (linha_a + 1) % 5 if modo == 'cifrar' else (linha_a - 1) % 5
            linha_b = (linha_b + 1) % 5 if modo == 'cifrar' else (linha_b - 1) % 5
        else:
            coluna_a, coluna_b = coluna_b, coluna_a

        mensagem_cifrada += matriz[linha_a][coluna_a] + matriz[linha_b][coluna_b]
        i += 2

    return mensagem_cifrada

if __name__ == "__main__":
    mensagem = input("Digite a mensagem para criptografar: ")
    chave = input("Digite a chave: ")

    mensagem_cifrada = cifra_playfair(mensagem, chave)
    print(f"Mensagem cifrada: {mensagem_cifrada}")
