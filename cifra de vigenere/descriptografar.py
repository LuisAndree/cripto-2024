def decifra_vigenere(mensagem_cifrada, palavra_chave):
    mensagem_decifrada = ""
    indice_chave = 0
    for char in mensagem_cifrada:
        if char.isalpha():
            deslocamento = ord(palavra_chave[indice_chave].lower()) - 97
            deslocamento_base = 65 if char.isupper() else 97
            mensagem_decifrada += chr((ord(char) - deslocamento_base - deslocamento) % 26 + deslocamento_base)
            indice_chave = (indice_chave + 1) % len(palavra_chave)
        else:
            mensagem_decifrada += char
    return mensagem_decifrada

if __name__ == "__main__":
    mensagem_cifrada = input("Digite a mensagem cifrada para descriptografar: ")
    palavra_chave = input("Digite a palavra-chave: ")
    mensagem_decifrada = decifra_vigenere(mensagem_cifrada, palavra_chave)
    print(f"Mensagem decifrada: {mensagem_decifrada}")
