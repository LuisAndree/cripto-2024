def substituicao_simples(mensagem, chave):
    alfabeto = "abcdefghijklmnopqrstuvwxyz"
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
    chave = input("Digite a chave de substituição (26 letras): ")
    
    if len(chave) != 26 or not chave.isalpha():
        print("A chave deve conter 26 letras e apenas letras.")
    else:
        mensagem_cifrada = substituicao_simples(mensagem, chave)
        print(f"Mensagem cifrada: {mensagem_cifrada}")
