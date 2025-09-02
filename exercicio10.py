
# Temperaturas da Semana
def temperatura():
    temperatura = []  
    for i in range(7):
        temperatu=int(input('Digite a temperatura de hoje: '))
        temperatura.append(temperatu)
    print(temperatura)
   
    media = sum(temperatura) / len(temperatura)
    print(f'a média das temperaturas são de {media:.2f}')
    
    temperatura_max = max(temperatura)
    temperatura_min = min(temperatura)

    posicao_max = temperatura.index(temperatura_max)
    posicao_min = temperatura.index(temperatura_min)

    dias_max = posicao_max + 1
    dias_min = posicao_min +1
    
    print(f'O dia mais quente foi o {dias_max}° dia, e o dia mais frio foi o {dias_min}°dia ')

    dias_acima_media = 0

    for i in range(len(temperatura)):
        if temperatura[i] > media:
            dias_acima_media +=1
    
    print(f'Os dias acima da média são {dias_acima_media}')
    
temperatura()

    
    # for i, temperatura in enumerate(temperatura):
    #     print(f'{i}, {temperatura}')