numeros = input("Digite uma lista de números separados por espaço: ").split()
numeros = [float(num) for num in numeros]
media = sum(numeros) / len(numeros)
print("A média é:", media)
