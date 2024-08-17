def eh_palindromo(palavra):
    palavra = palavra.replace(" ", "").lower()
    return palavra == palavra[::-1]

if __name__ == "__main__":
    palavra = input("Digite uma palavra ou frase: ")
    if eh_palindromo(palavra):
        print(f"'{palavra}' é um palíndromo.")
    else:
        print(f"'{palavra}' não é um palíndromo.")
