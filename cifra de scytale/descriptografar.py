def decifra_scytale(mensagem_cifrada, diametro):
    comprimento = len(mensagem_cifrada)
    linhas = (comprimento + diametro - 1) // diametro
    mensagem_decifrada = ''.join(mensagem_cifrada[i::linhas] for i in range(linhas))
    return mensagem_decifrada

if __name__ == "__main__":
    mensagem_cifrada = input("Digite a mensagem cifrada para descriptografar: ")
    diametro = int(input("Digite o diâmetro: "))

    mensagem_decifrada = decifra_scytale(mensagem_cifrada, diametro)
    print(f"Mensagem decifrada: {mensagem_decifrada}")
