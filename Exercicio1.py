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

def gastos(nome_cliente,pedidos):
    soma =0 
    for pedido in pedidos:
        if pedido["cliente"] == nome_cliente:
            for item in pedido["itens"]:
                preco = item["preço"]
                soma += preco
    return soma

def mais_vendidos(pedidos):
    contagem_pratos = {}
    for pedido in pedidos:
        for item in pedido["itens"]:
            if item["prato"] in contagem_pratos:
                contagem_pratos[item["prato"]] += 1
            else:
                contagem_pratos[item["prato"]] = 1
    maior_valor = max(contagem_pratos.values())
    for pratos,quantidae in contagem_pratos.items():
        if quantidae == maior_valor:
            print(f"Os pratos mais vendidos do dias foram: {pratos}")

def ranking(pedidos):
    totais_clientes = {}
    for pedido in pedidos:
        nome = pedido["cliente"]
        total = gastos(nome, pedidos)
        totais_clientes[nome] = total
    print("O rankig dos Clientes que mais gastaram são: ")
    
    for i in range(3):
        maior = max(totais_clientes.values())
        for nome, total in totais_clientes.items():
            if total == maior:
                print(f"{i+1}º lugar: {nome} = {total}")
                del totais_clientes[nome]
                break

def main():
    print("Total da Ana:", gastos("Ana", pedidos))
    mais_vendidos(pedidos)
    ranking(pedidos)
main()
