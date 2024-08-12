def cifra_rail_fence(mensagem, linhas):
    if linhas == 1:
        return mensagem

    rail = [''] * linhas
    linha_atual = 0
    descendo = True

    for char in mensagem:
        rail[linha_atual] += char
        if linha_atual == 0:
            descendo = True
        elif linha_atual == linhas - 1:
            descendo = False

        linha_atual += 1 if descendo else -1

    return ''.join(rail)

if __name__ == "__main__":
    mensagem = input("Digite a mensagem para criptografar: ")
    linhas = int(input("Digite o número de linhas (rails): "))

    mensagem_cifrada = cifra_rail_fence(mensagem, linhas)
    print(f"Mensagem cifrada: {mensagem_cifrada}")
