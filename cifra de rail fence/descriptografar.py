def decifra_rail_fence(mensagem_cifrada, linhas):
    if linhas == 1:
        return mensagem_cifrada

    rail = [''] * linhas
    linha_atual = 0
    descendo = True

    for char in mensagem_cifrada:
        rail[linha_atual] += '*'
        if linha_atual == 0:
            descendo = True
        elif linha_atual == linhas - 1:
            descendo = False

        linha_atual += 1 if descendo else -1

    index = 0
    for linha in range(linhas):
        for j in range(len(rail[linha])):
            if rail[linha][j] == '*' and index < len(mensagem_cifrada):
                rail[linha] = rail[linha][:j] + mensagem_cifrada[index] + rail[linha][j+1:]
                index += 1

    mensagem_decifrada = ''
    linha_atual = 0
    descendo = True

    for i in range(len(mensagem_cifrada)):
        mensagem_decifrada += rail[linha_atual][0]
        rail[linha_atual] = rail[linha_atual][1:]

        if linha_atual == 0:
            descendo = True
        elif linha_atual == linhas - 1:
            descendo = False

        linha_atual += 1 if descendo else -1

    return mensagem_decifrada

if __name__ == "__main__":
    mensagem_cifrada = input("Digite a mensagem cifrada para descriptografar: ")
    linhas = int(input("Digite o número de linhas (rails): "))

    mensagem_decifrada = decifra_rail_fence(mensagem_cifrada, linhas)
    print(f"Mensagem decifrada: {mensagem_decifrada}")
