def int_para_romano(numero):
    valores = [
        (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
        (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
        (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')
    ]
    resultado = ''
    for valor, simbolo in valores:
        while numero >= valor:
            resultado += simbolo
            numero -= valor
    return resultado

def romano_para_int(romano):
    valores = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    resultado = 0
    i = 0
    while i < len(romano):
        if i + 1 < len(romano) and valores[romano[i]] < valores[romano[i + 1]]:
            resultado += valores[romano[i + 1]] - valores[romano[i]]
            i += 2
        else:
            resultado += valores[romano[i]]
            i += 1
    return resultado

if __name__ == "__main__":
    escolha = input("Digite '1' para converter de inteiro para romano ou '2' para romano para inteiro: ")

    if escolha == '1':
        numero = int(input("Digite um número inteiro: "))
        print(f"{numero} em números romanos é: {int_para_romano(numero)}")
    elif escolha == '2':
        romano = input("Digite um número romano: ")
        print(f"{romano} em números inteiros é: {romano_para_int(romano)}")
    else:
        print("Escolha inválida.")
