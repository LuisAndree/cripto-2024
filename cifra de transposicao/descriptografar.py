def descriptografar_transposicao(mensagem_criptografada):
    return mensagem_criptografada[::-1]

def main():
    mensagem_criptografada = input("Digite a mensagem criptografada: ")
    mensagem_descriptografada = descriptografar_transposicao(mensagem_criptografada)
    print(f"Mensagem descriptografada: {mensagem_descriptografada}")

if __name__ == "__main__":
    main()
