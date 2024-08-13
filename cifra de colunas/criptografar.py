def cifra_colunas(mensagem, chave):
    mensagem = mensagem.replace(" ", "")
    comprimento_chave = len(chave)
    
    linhas = (len(mensagem) + comprimento_chave - 1) // comprimento_chave
    
    # Preencher a grade
    grade = [''] * comprimento_chave
    for i, char in enumerate(mensagem):
        coluna = i % comprimento_chave
        grade[coluna] += char
    
    colunas_ordenadas = sorted(range(comprimento_chave), key=lambda x: chave[x])

    mensagem_cifrada = ''.join(grade[i] for i in colunas_ordenadas)
    
    return mensagem_cifrada

if __name__ == "__main__":
    mensagem = input("Digite a mensagem para criptografar: ")
    chave = input("Digite a chave (uma sequência de caracteres única): ")
    
    mensagem_cifrada = cifra_colunas(mensagem, chave)
    print(f"Mensagem cifrada: {mensagem_cifrada}")
