def cifra_scytale(mensagem, diametro):
    mensagem = mensagem.replace(" ", "")
    comprimento = len(mensagem)
    linhas = (comprimento + diametro - 1) // diametro
    mensagem += 'x' * (linhas * diametro - comprimento)
    mensagem_cifrada = ''.join(mensagem[i::diametro] for i in range(diametro))
    return mensagem_cifrada

if __name__ == "__main__":
    mensagem = input("Digite a mensagem para criptografar: ")
    diametro = int(input("Digite o diâmetro: "))

    mensagem_cifrada = cifra_scytale(mensagem, diametro)
    print(f"Mensagem cifrada: {mensagem_cifrada}")
