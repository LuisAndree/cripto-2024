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

def hill_cipher_cifrar(mensagem, chave):
    tamanho = 2  
    matriz_chave = gerar_matriz_chave(chave, tamanho)

    mensagem = mensagem.lower().replace(" ", "")
    while len(mensagem) % tamanho != 0:
        mensagem += 'x'  

    mensagem_numerica = [[ord(char) - ord('a')] for char in mensagem]

    mensagem_cifrada = ''
    for i in range(0, len(mensagem), tamanho):
        bloco = mensagem_numerica[i:i+tamanho]
        bloco_cifrado = mod26_matrix_mult(matriz_chave, bloco)
        mensagem_cifrada += ''.join(chr(num[0] + ord('a')) for num in bloco_cifrado)

    return mensagem_cifrada

if __name__ == "__main__":
    mensagem = input("Digite a mensagem para criptografar: ")
    chave = input("Digite a chave (deve ser uma string com pelo menos 4 caracteres): ")

    mensagem_cifrada = hill_cipher_cifrar(mensagem, chave)
    print(f"Mensagem cifrada: {mensagem_cifrada}")
