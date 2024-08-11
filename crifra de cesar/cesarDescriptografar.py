def descriptografar_cesar(mensagem_criptografada, chave):
    return criptografar_cesar(mensagem_criptografada, -chave)

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
    mensagem_criptografada = input("Digite a mensagem criptografada: ")
    chave = int(input("Digite a chave (um número inteiro): "))

    mensagem_descriptografada = descriptografar_cesar(mensagem_criptografada, chave)
    print(f"Mensagem descriptografada: {mensagem_descriptografada}")

if __name__ == "__main__":
    main()
