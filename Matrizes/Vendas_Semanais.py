matriz = []
nome = []
receitas = []
for i in range(2):
    produto = input(f'Digite o nome do produto {i+1}: ')
    nome.append(produto)
    linha = []
    print(f"Digite as vendas de {produto} durante 7 dias:")
    for j in range(2):
        venda = float(input(f"Dia {j+1}: "))
        linha.append(venda)
    matriz.append(linha)

for vendas in matriz:
    receitas.append(sum(vendas))
print("Receita total semanal de cada produto:")
for i, total in enumerate(receitas):
    print(f"Produto {nome[0+i]}: R$ {total:.2f}")


   