def caixa_eletronico(valor):
    cedulas = [100, 50, 20, 10, 5, 2, 1]
    resultado = {}

    for cedula in cedulas:
        quantidade, valor = divmod(valor, cedula)
        if quantidade > 0:
            resultado[cedula] = quantidade

    return resultado

if __name__ == "__main__":
    valor = int(input("Digite o valor a ser sacado: R$ "))
    resultado = caixa_eletronico(valor)

    print("Você receberá:")
    for cedula, quantidade in resultado.items():
        print(f"{quantidade} cédula(s) de R$ {cedula}")
