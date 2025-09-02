#Analise de Dados Mensais
def registarar_vendas():
    mes = {}
    while True:
        dia=input('Digite o dia do mês ou sair para encerrar o programa: ').lower()
        if dia == 'sair':
            break
        vendas=float(input('Digite o total de vendas do dia: '))
        mes[dia] = vendas

    print(mes)
    return mes

def calcular_venda(vendas):
    total = 0.0
    for dia in vendas:
        valor = vendas[dia]
        total += valor
    
    return total

def mais_vendas_menos_vendas(vendas):
    maior = 0
    dia_maior = ''

    for dia in vendas:
        if vendas[dia] > maior:
            maior = vendas[dia]
            dia_maior = dia

    menor = 99999999 
    dia_menor = ''

    for dia in vendas:
        if vendas[dia] < menor:
            menor = vendas[dia]
            dia_menor = dia
    return maior,dia_maior,menor,dia_menor

def calcular_media(vendas):
    total = calcular_venda(vendas)
    num_dias = len(vendas)
    media = total / num_dias
    return media

def dias_acima_media(vendas,media):
    dias_acima = []
    for dia in vendas:
        if vendas[dia] > media:
            dias_acima.append(dia)
    return dias_acima

def main():
    vendas = registarar_vendas()
    total_vendido = calcular_venda(vendas)
    maior,dia_maior,menor,dia_menor = mais_vendas_menos_vendas(vendas)
    media = calcular_media(vendas)
    dias_acima = dias_acima_media(vendas,media)

    print(f'Total de vendas do Mês {total_vendido:.2f}')
    print(f'O dia com mais vendas foi o {dia_maior} dia e  vendeu R${maior} \nO dia com menos vendas foi o {dia_menor}dia e  vendeu R${menor}')
    print(f'A média de vendas por dia é de R${media:.2f}')
    print(f'Os dias que tiveram vendas acimas da média foram os dias {dias_acima}')


main()