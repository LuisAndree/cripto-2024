import random
import string

def gerar_chave_aleatoria():
    letras = list(string.ascii_lowercase)
    random.shuffle(letras)
    return ''.join(letras)

def substituir_aleatorio(mensagem, chave):
    alfabeto = string.ascii_lowercase
    mensagem_cifrada = ""
    for char in mensagem.lower():
        if char.isalpha():
            indice = alfabeto.index(char)
            mensagem_cifrada += chave[indice]
        else:
            mensagem_cifrada += char
    return mensagem_cifrada

if __name__ == "__main__":
    mensagem = input("Digite a mensagem para criptografar: ")
    chave = gerar_chave_aleatoria()
    print(f"Chave gerada: {chave}")

    mensagem_cifrada = substituir_aleatorio(mensagem, chave)
    print(f"Mensagem cifrada: {mensagem_cifrada}")
