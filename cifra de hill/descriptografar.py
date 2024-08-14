def gerar_matriz_chave(chave, tamanho):
    chave = chave.lower().replace(" ", "")
    matriz_chave = []
    indice = 0
    for i in range(tamanho):
        linha = []
        for j in range(tamanho):
            if indice < len(chave):
                linha.append(ord(chave[indice]) - ord('a'))
            else:
                linha.append(0)
            indice += 1
        matriz_chave.append(linha)
    return matriz_chave

def mod26_matrix_mult(A, B):
    tamanho = len(A)
    resultado = [[0] * len(B[0]) for _ in range(tamanho)]
    for i in range(tamanho):
        for j in range(len(B[0])):
            for k in range(tamanho):
                resultado[i][j] += A[i][k] * B[k][j]
            resultado[i][j] %= 26
    return resultado

def calcular_determinante(matriz):
    if len(matriz) == 2:
        return matriz[0][0] * matriz[1][1] - matriz[0][1] * matriz[1][0]
    determinante = 0
    for c in range(len(matriz)):
        determinante += ((-1) ** c) * matriz[0][c] * calcular_determinante(gerar_matriz_submatriz(matriz, 0, c))
    return determinante

def gerar_matriz_submatriz(matriz, i, j):
    return [linha[:j] + linha[j+1:] for linha in (matriz[:i] + matriz[i+1:])]

def calcular_inversa_modular(determinante, modulo=26):
    determinante = determinante % modulo
    for i in range(1, modulo):
        if (determinante * i) % modulo == 1:
            return i
    return None

def calcular_adjugate(matriz):
    adjugate = []
    for i in range(len(matriz)):
        linha = []
        for j in range(len(matriz)):
            cofator = calcular_determinante(gerar_matriz_submatriz(matriz, i, j))
            linha.append(((-1) ** (i + j)) * cofator)
        adjugate.append(linha)
    adjugate = [list(i) for i in zip(*adjugate)]  
    return adjugate

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def verificar_chave_valida(matriz_chave):
    determinante = calcular_determinante(matriz_chave)
    if gcd(determinante, 26) != 1:
        raise ValueError("A chave não é válida: determinante e 26 não são coprimos")
    return True

def calcular_inversa_matriz(matriz):
    verificar_chave_valida(matriz)
    determinante = calcular_determinante(matriz)
    inversa_determinante = calcular_inversa_modular(determinante)
    if inversa_determinante is None:
        raise ValueError("A chave não é inversível")
    adjugate = calcular_adjugate(matriz)
    inversa = [[(inversa_determinante * adjugate[i][j]) % 26 for j in range(len(matriz))] for i in range(len(matriz))]
    return inversa

def hill_cipher_decifrar(mensagem, chave):
    tamanho = 2  
    matriz_chave = gerar_matriz_chave(chave, tamanho)
    matriz_chave = calcular_inversa_matriz(matriz_chave)

    mensagem_numerica = [[ord(char) - ord('a')] for char in mensagem]

    mensagem_decifrada = ''
    for i in range(0, len(mensagem), tamanho):
        bloco = mensagem_numerica[i:i+tamanho]
        bloco_decifrado = mod26_matrix_mult(matriz_chave, bloco)
        mensagem_decifrada += ''.join(chr(num[0] + ord('a')) for num in bloco_decifrado)

    return mensagem_decifrada

if __name__ == "__main__":
    mensagem_cifrada = input("Digite a mensagem cifrada para descriptografar: ")
    chave = input("Digite a chave (deve ser a mesma usada para criptografar): ")

    mensagem_decifrada = hill_cipher_decifrar(mensagem_cifrada, chave)
    print(f"Mensagem decifrada: {mensagem_decifrada}")
