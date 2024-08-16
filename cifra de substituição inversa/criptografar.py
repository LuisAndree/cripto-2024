def criar_dicionario_inverso():
    alfabeto = 'abcdefghijklmnopqrstuvwxyz'
    inverso = alfabeto[::-1]
    return str.maketrans(alfabeto, inverso)

def substituir_inversa(mensagem):
    dicionario = criar_dicionario_inverso()
    return mensagem.translate(dicionario)

mensagem = input("Digite a mensagem: ")
mensagem_cifrada = substituir_inversa(mensagem)
print(f"Mensagem cifrada: {mensagem_cifrada}")

mensagem_decifrada = substituir_inversa(mensagem_cifrada)
print(f"Mensagem decifrada: {mensagem_decifrada}")
