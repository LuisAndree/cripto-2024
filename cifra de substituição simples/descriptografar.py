def substituicao_simples_inversa(mensagem_cifrada, chave):
    alfabeto = "abcdefghijklmnopqrstuvwxyz"
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
    chave = input("Digite a chave de substituição (26 letras): ")
    
    if len(chave) != 26 or not chave.isalpha():
        print("A chave deve conter 26 letras e apenas letras.")
    else:
        mensagem_decifrada = substituicao_simples_inversa(mensagem_cifrada, chave)
        print(f"Mensagem decifrada: {mensagem_decifrada}")
