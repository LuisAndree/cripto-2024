import string 

def substituir_aleatorio_inversa(mensagem_cifrada, chave):
    alfabeto = string.ascii_lowercase
    mensagem_decifrada = ""
    for char in mensagem_cifrada.lower():
        if char.isalpha():
            indice = chave.index(char)
            mensagem_decifrada += alfabeto[indice]
        else:
            mensagem_decifrada += char
    return mensagem_decifrada

if __name__ == "__main__":
    mensagem_cifrada = input("Digite a mensagem cifrada para descriptografar: ")
    chave = input("Digite a chave usada para criptografar: ")
    
    mensagem_decifrada = substituir_aleatorio_inversa(mensagem_cifrada, chave)
    print(f"Mensagem decifrada: {mensagem_decifrada}")
