string = input("Digite uma string: ")
vogais = 'aeiouAEIOU'
contagem = 0

for char in string:
    if char in vogais:
        contagem += 1

print("O número de vogais na string é:", contagem)
