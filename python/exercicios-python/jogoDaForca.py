import random

def escolher_palavra():
    palavras = ['python', 'desenvolvimento', 'algoritmo', 'programacao', 'interface']
    return random.choice(palavras)

def exibir_palavra(palavra, letras_acertadas):
    return ''.join([letra if letra in letras_acertadas else '_' for letra in palavra])

def jogo_da_forca():
    palavra_secreta = escolher_palavra()
    letras_acertadas = set()
    tentativas = 6

    print("Bem-vindo ao Jogo da Forca!")

    while tentativas > 0:
        print("\nPalavra: ", exibir_palavra(palavra_secreta, letras_acertadas))
        print(f"Tentativas restantes: {tentativas}")
        letra = input("Digite uma letra: ").lower()

        if letra in letras_acertadas:
            print("Você já tentou essa letra!")
            continue

        if letra in palavra_secreta:
            letras_acertadas.add(letra)
            print("Boa! Você acertou uma letra.")
        else:
            tentativas -= 1
            print("Você errou!")

        if set(palavra_secreta) == letras_acertadas:
            print("\nParabéns! Você ganhou. A palavra era:", palavra_secreta)
            break
    else:
        print("\nVocê perdeu! A palavra era:", palavra_secreta)

if __name__ == "__main__":
    jogo_da_forca()
