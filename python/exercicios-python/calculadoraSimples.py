def soma(a, b):
    return a + b

def subtrai(a, b):
    return a - b

def multiplica(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Erro: Divisão por zero"
    return a / b

if __name__ == "__main__":
    print("Escolha a operação:")
    print("1. Soma")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")
    
    operacao = input("Digite o número da operação: ")
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    
    if operacao == '1':
        print(f"Resultado: {soma(num1, num2)}")
    elif operacao == '2':
        print(f"Resultado: {subtrai(num1, num2)}")
    elif operacao == '3':
        print(f"Resultado: {multiplica(num1, num2)}")
    elif operacao == '4':
        print(f"Resultado: {divide(num1, num2)}")
    else:
        print("Operação inválida")
