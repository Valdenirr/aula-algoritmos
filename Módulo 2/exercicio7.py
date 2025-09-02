def calcular_media_turma():
    alunos=[]
    notas=[]
    quantidade=int(input('Quantos alunos tem na turma? '))
    for i in range(quantidade):
        nome=str(input('Digite aqui o nome dos alunos: '))
        alunos.append(nome)
        nota_alunos=float(input('Digite a nota de cada aluno: '))
        notas.append(nota_alunos)

    media= sum(notas) / len(notas)
    
    maior_nota = max(notas)
    menor_nota = min(notas)
    
    acima_da_media = 0
    for nota in notas:
        if nota >= media:
            acima_da_media += 1
    
    percentual_acima = (acima_da_media / quantidade) * 100 
    
    print(f'A média da turma é de {media}')
    print(f' a maior nota é de {maior_nota} e a menor nota é de {menor_nota}')
    print(f'O percentual dos alunos acima da média é de {percentual_acima}')

calcular_media_turma()