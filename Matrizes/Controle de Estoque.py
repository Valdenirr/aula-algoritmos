matriz = []
soma = []
for i in range (2) :
    produto = input("Digite o nome do produto: ")
    quantidade = []
    for j in range (2) :
        quantidade.append(int(input('Quantidade do produto: ')))
        matriz.append(produto)
        matriz.append(quantidade)
for s in matriz:
    total = sum([matriz[s+1]])
print(soma)