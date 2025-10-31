matriz = []
for i in range (3) :
    time = input("Digite o Nome do Time: ")
    pontos = []
    for j in range (4) :
        pontos.append(int(input('Digite o ponto do time: ')))
    matriz.append([time,pontos])

maior=0
time_maior = ''
for linha in matriz:
    total = sum(linha[1])
    if total > maior:
        maior = total
        time_maior = linha[0]

print(f'O time com maior pontuação foi o {time_maior} com a potuação de {maior}')