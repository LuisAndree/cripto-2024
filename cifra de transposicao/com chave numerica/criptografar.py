def cifra_transposicao_chave_numerica(mensagem, chave):
    ordem = [int(k) for k in chave]
    colunas = len(ordem)
    tabela = [''] * colunas

    for i, char in enumerate(mensagem):
        tabela[i % colunas] += char
    
    cifrado = ''.join(tabela[i] for i in ordem)
    return cifrado

def decifra_transposicao_chave_numerica(mensagem_cifrada, chave):
    ordem = [int(k) for k in chave]
    colunas = len(ordem)
    comprimento_coluna = len(mensagem_cifrada) // colunas
    tabela = [''] * colunas
    inicio = 0

    for i in ordem:
        fim = inicio + comprimento_coluna
        tabela[i] = mensagem_cifrada[inicio:fim]
        inicio = fim

    mensagem_decifrada = ''
    for i in range(comprimento_coluna):
        for coluna in tabela:
            if i < len(coluna):
                mensagem_decifrada += coluna[i]

    return mensagem_decifrada

mensagem = input("Digite a mensagem: ")
chave = input("Digite a chave (sequência de números): ")

mensagem_cifrada = cifra_transposicao_chave_numerica(mensagem, chave)
print(f"Mensagem cifrada: {mensagem_cifrada}")

mensagem_decifrada = decifra_transposicao_chave_numerica(mensagem_cifrada, chave)
print(f"Mensagem decifrada: {mensagem_decifrada}")
