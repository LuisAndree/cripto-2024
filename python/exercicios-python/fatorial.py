num = int(input("Digite um número para calcular o fatorial: "))
fatorial = 1

if num < 0:
    print("Não existe fatorial de número negativo.")
elif num == 0 or num == 1:
    print("O fatorial de", num, "é 1.")
else:
    for i in range(1, num + 1):
        fatorial *= i
    print("O fatorial de", num, "é", fatorial)
