matriz = []
for i in range (4) :
    linha = input("Coloque o numero da linhe e coloque o nome da linha logo a frente: ")
    horario = []
    for j in range (3) :
        horario.append((input('Digite o horário da linha: ')))
    matriz.append([linha,horario])
print(matriz)
busca = int(input('Digite o numero da linha que você deseja visualizar o horario: '))
print(f'O horario da linha selecionado : {matriz[busca]}')
