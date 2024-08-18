def calcular_digito(cpf, peso):
    soma = sum(int(cpf[i]) * (peso - i) for i in range(len(cpf)))
    resto = soma % 11
    return '0' if resto < 2 else str(11 - resto)

def validar_cpf(cpf):
    cpf = cpf.replace('.', '').replace('-', '')
    if len(cpf) != 11 or not cpf.isdigit():
        return False

    primeiro_digito = calcular_digito(cpf[:9], 10)
    segundo_digito = calcular_digito(cpf[:10], 11)
    return cpf[-2:] == primeiro_digito + segundo_digito

if __name__ == "__main__":
    cpf = input("Digite um CPF (xxx.xxx.xxx-xx): ")
    if validar_cpf(cpf):
        print("O CPF é válido.")
    else:
        print("O CPF é inválido.")
