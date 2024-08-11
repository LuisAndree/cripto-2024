def criptografar_cesar(mensagem, chave):
    mensagem_criptografada = ""
    for char in mensagem:
        if char.isalpha():
            deslocamento = ord('a') if char.islower() else ord('A')
            mensagem_criptografada += chr((ord(char) - deslocamento + chave) % 26 + deslocamento)
        else:
            mensagem_criptografada += char
    return mensagem_criptografada

def main():
    mensagem = input("Digite a mensagem para criptografar: ")
    chave = int(input("Digite a chave (um número inteiro): "))

    mensagem_criptografada = criptografar_cesar(mensagem, chave)
    print(f"Mensagem criptografada: {mensagem_criptografada}")

if __name__ == "__main__":
    main()
