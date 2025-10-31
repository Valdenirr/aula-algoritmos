pedidos = [
    {
        "cliente" : "Ana",
        "itens" : [
            {"prato" : "Lasanha", "preço" : 30},
            {"prato" : "Suco de Laranja", "preço" : 8}
        ]
    },
    {
        "cliente" : "Bruno",
        "itens" : [
            {"prato" : "Pizza", "preço" : 40},
            {"prato" : "Refrigerante", "preço" : 6},
            {"prato" : "Sobremesa", "preço" : 12}
        ]
    },
    {
        "cliente" : "Carla",
        "itens" : [
            {"prato" : "Pizza", "preço" : 40},
            {"prato" : "Suco de Laranja", "preço" : 8}
        ]
    }
]

def valor_gasto(nome_cliente, pedidos):
    soma = 0
    for pedido in pedidos:
        if pedido["cliente"] == nome_cliente:
            for item in pedido["itens"]:
                soma += item["preço"]
    return soma
print(valor_gasto("Ana", pedidos))

def pratos_mais_vendidos(pedidos):
    mais_vendidos = {}
    for pedido in pedidos:
        for item in pedido["itens"]:
            prato_atual = item["prato"]
            if prato_atual in mais_vendidos:
                mais_vendidos[prato_atual] += 1
            else:
                mais_vendidos[prato_atual] = 1
    
    prato_mais_vendido = max(mais_vendidos, key=mais_vendidos.get)
    return prato_mais_vendido
print(pratos_mais_vendidos(pedidos))

def ranking(pedidos):
    gastos = {}
    for pedido in pedidos:
        clientes = pedido["cliente"]
        total_gasto = 0
        for item in pedido["itens"]:
            total_gasto += item["preço"]
            gastos[clientes] = total_gasto
    return gastos
print(ranking(pedidos))