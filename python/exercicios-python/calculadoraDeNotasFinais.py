def calcular_nota_final(avaliacoes):
    nota_final = sum(nota * peso for nota, peso in avaliacoes) / sum(peso for _, peso in avaliacoes)
    return nota_final

def calcular_media_turma(alunos):
    soma_notas = sum(calcular_nota_final(avaliacoes) for avaliacoes in alunos.values())
    return soma_notas / len(alunos)

if __name__ == "__main__":
    alunos = {}
    while True:
        nome = input("Digite o nome do aluno (ou 'sair' para encerrar): ")
        if nome.lower() == 'sair':
            break
        avaliacoes = []
        while True:
            nota = float(input("Digite a nota: "))
            peso = float(input("Digite o peso da avaliação: "))
            avaliacoes.append((nota, peso))
            continuar = input("Adicionar outra avaliação para esse aluno? (s/n): ").lower()
            if continuar != 's':
                break
        alunos[nome] = avaliacoes

    for nome, avaliacoes in alunos.items():
        nota_final = calcular_nota_final(avaliacoes)
        print(f"A nota final de {nome} é: {nota_final:.2f}")

    media_turma = calcular_media_turma(alunos)
    print(f"A média da turma é: {media_turma:.2f}")

    aluno_top = max(alunos, key=lambda nome: calcular_nota_final(alunos[nome]))
    print(f"O aluno com a maior nota é {aluno_top} com nota {calcular_nota_final(alunos[aluno_top]):.2f}")
