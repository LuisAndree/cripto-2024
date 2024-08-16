def cifra_cesar(mensagem, chave, modo):
    resultado = ''
    for char in mensagem:
        if char.isalpha():
            base = ord('a') if char.islower() else ord('A')
            offset = (ord(char) - base + (chave if modo == 'cifrar' else -chave)) % 26
            resultado += chr(base + offset)
        else:
            resultado += char
    return resultado

mensagem = input("Digite a mensagem: ")
chave = int(input("Digite a chave de deslocamento: "))
modo = input("Você quer 'cifrar' ou 'decifrar' a mensagem? ")

resultado = cifra_cesar(mensagem, chave, modo)
print(f"Resultado: {resultado}")
