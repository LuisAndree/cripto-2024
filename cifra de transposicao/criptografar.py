def criptografar_transposicao(mensagem):
    return mensagem[::-1]

def main():
    mensagem = input("Digite a mensagem para criptografar: ")
    mensagem_criptografada = criptografar_transposicao(mensagem)
    print(f"Mensagem criptografada: {mensagem_criptografada}")

if __name__ == "__main__":
    main()
