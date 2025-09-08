##Controle de estoque Supermecados

def registrar_produtos():
    produtos = {}   
    while True:        
        nome = input('Digite o nome do produto ou sair para finalizar o programa: ').upper()
        if nome == 'SAIR':
            break
        quantidade = int(input('Digite a quantidade do produto: '))
        preço_unitario=float(input('Digite o preço unitario do produto: '))
        produtos[nome] = {
            'quantidade': quantidade,
            'preço_unitario':preço_unitario
        }
    return produtos

def calcular_valor_estoque(estoque):
    total = 0.0
    for nome_produto in estoque:
        quantidade= estoque[nome_produto]['quantidade']
        preco= estoque[nome_produto]['preço_unitario']
        valor_produto = quantidade * preco
        total += valor_produto
    return total

def encontrar_produto_maior_valor(estoque):
    maior_valor = 0
    produto_maior = ''
    for nome_produto in estoque:
        quantidade= estoque[nome_produto]['quantidade']
        preco= estoque[nome_produto]['preço_unitario']
        valor_total = quantidade * preco

        if valor_total > maior_valor:
            maior_valor = valor_total
            produto_maior = nome_produto
    return produto_maior, maior_valor

def produtos_estoques_abaixo5(estoque):
    produtos_baixo = []

    for nome_produto in estoque:
        quantidade = estoque[nome_produto]['quantidade']
        if quantidade <= 5:
            produtos_baixo.append(nome_produto)
    return produtos_baixo

def buscar_produtos(estoque,nome_produto):
    if nome_produto in estoque:
        return estoque[nome_produto]
    else:
        return 'Produto não encontrado'


def main():
    estoque = registrar_produtos()
    valor_total = calcular_valor_estoque(estoque)
    produto_maior, valor_maior = encontrar_produto_maior_valor(estoque)
    menor_5 = produtos_estoques_abaixo5(estoque)

    print(f'O valor total em estoque é de R${valor_total}')
    print(f'O produto com maior valor foi o {produto_maior} R${valor_maior:.2f}')
    print(f'O produto com o estoque menor que 5 é o {menor_5}')
    print('=== Buscar Produtos ===')
    nome_busca = input('Digite o nome do produto que deseja buscar: ')
    resultado = buscar_produtos(estoque, nome_busca)
    print(f'Resultado da busca {resultado}')

main()