matriz = []
medias = []

for i in range(4):
    aluno = input('Digite o nome do aluno: ')
    linha = []
    for j in range(3):
        linha.append(float(input(f'Digite a nota {j+1} de {aluno}: ')))
    matriz.append(linha)

for notas in matriz:
    medias.append(sum(notas) / len(notas))

print("Médias dos alunos:")
for i in range(len(medias)):
    print(f"Aluno {i+1}: {medias[i]:.2f}")