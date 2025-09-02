#Controle de Vendas  Loja
def controle_de_vendas():

    produtos = {}

    while True:
        produto = input('Digite o nome do Produto ou digite sair para encerrar o programa: ').lower()
        if produto == 'sair':
            break

        preço=float(input('Digite o preço do produto: '))
        produtos[produto] = float(preço)
    return produtos
        
def soma_total(produtos):
    preço_total = sum(produtos.values())
    print(f'O valor total do dia registrado foi de R${preço_total:.2f}')

def mais_Caro_mais_Barato(produtos):
    valor_maximo = max(produtos, key=produtos.get)
    valor_mais_caro = produtos[valor_maximo]
    
    valor_minimo = min(produtos, key=produtos.get)
    valor_mais_barato = produtos[valor_minimo]
    print(f'O produto mais caro foi {valor_maximo}, e o valor foi de R${valor_mais_caro}')
    print(f'O produto mais barato foi {valor_minimo} e o valor foi de R${valor_mais_barato}')

def pesquisa(produtos):
    
    for i in range(0,3):
        pesquisar = input('Digite o nome do item que você quer procurar nos seus produtos: ')
        if pesquisar in produtos:
            print(f'O item {pesquisar} está na sua lista de produtos!')
            break
        else:
            print(f'O item {pesquisar} não está na sua lista de produtos!')

def main():
    produtos = controle_de_vendas()
    soma = soma_total(produtos)
    diferença_valores = mais_Caro_mais_Barato(produtos)
    pesquisa(produtos)

main()