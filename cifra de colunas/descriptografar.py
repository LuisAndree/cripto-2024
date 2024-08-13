def decifra_colunas(mensagem_cifrada, chave):
    comprimento_chave = len(chave)
    colunas_ordenadas = sorted(range(comprimento_chave), key=lambda x: chave[x])
    
    linhas = (len(mensagem_cifrada) + comprimento_chave - 1) // comprimento_chave
    comprimento_cifrado = len(mensagem_cifrada)
    
    grade = [''] * comprimento_chave
    indice = 0
    for coluna in colunas_ordenadas:
        comprimento_coluna = linhas
        if coluna >= comprimento_cifrado % comprimento_chave:
            comprimento_coluna -= 1
        grade[coluna] = mensagem_cifrada[indice:indice + comprimento_coluna]
        indice += comprimento_coluna
    
    mensagem_decifrada = ''
    for i in range(linhas):
        for coluna in range(comprimento_chave):
            if i < len(grade[coluna]):
                mensagem_decifrada += grade[coluna][i]
    
    return mensagem_decifrada

if __name__ == "__main__":
    mensagem_cifrada = input("Digite a mensagem cifrada para descriptografar: ")
    chave = input("Digite a chave (uma sequência de caracteres única): ")
    
    mensagem_decifrada = decifra_colunas(mensagem_cifrada, chave)
    print(f"Mensagem decifrada: {mensagem_decifrada}")
