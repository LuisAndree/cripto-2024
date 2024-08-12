def cifra_vigenere(mensagem, palavra_chave):
    mensagem_cifrada = ""
    indice_chave = 0
    for char in mensagem:
        if char.isalpha():
            deslocamento = ord(palavra_chave[indice_chave].lower()) - 97
            deslocamento_base = 65 if char.isupper() else 97
            mensagem_cifrada += chr((ord(char) - deslocamento_base + deslocamento) % 26 + deslocamento_base)
            indice_chave = (indice_chave + 1) % len(palavra_chave)
        else:
            mensagem_cifrada += char
    return mensagem_cifrada

if __name__ == "__main__":
    mensagem = input("Digite a mensagem para criptografar: ")
    palavra_chave = input("Digite a palavra-chave: ")
    mensagem_cifrada = cifra_vigenere(mensagem, palavra_chave)
    print(f"Mensagem cifrada: {mensagem_cifrada}")
