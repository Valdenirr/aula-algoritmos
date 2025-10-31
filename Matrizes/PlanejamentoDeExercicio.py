matriz = []
nmatriz = []

for i in range(4):
    linha = []
    for j in range(3):
        qtd = int(input(f"Aluno {i+1}, repetições do Exercício {j+1}: "))
        linha.append(qtd)
    matriz.append(linha)

contador = 1
for linha in matriz:
    print(f"Aluno {contador}: {linha}")
    contador += 1

totais = []
for j in range(3):
    soma_coluna = 0
    for i in range(4):
        soma_coluna += matriz[i][j]
    totais.append(soma_coluna)

exercicio = 1
for total in totais:
    print(f"Total do Exercício {exercicio}: {total}")
    exercicio += 1
