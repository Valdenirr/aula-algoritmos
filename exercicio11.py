#Lista de Compras automatizada
lista_compras = []
while True:
    adicionar = (input('Digite o nome do item para adicionar a lsta de compras: ')).strip().lower()
    if adicionar == 'sair':
        break
    else:
        lista_compras.append(adicionar)

lista_compras.sort()
print(lista_compras)
