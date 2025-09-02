import math

def distancias():
    km_viagens = []
    for i in range(6):
        km = float(input('Digite o total de km da sua vaigem: '))
        km_viagens.append(km)
    print(km_viagens)
    return km_viagens 

def calcular_distancia(km_viagens):
    total_km = sum(km_viagens)
    print(f'O total de kms percorridos foram de {total_km:.2f}')
    return  total_km

def maior_menor(km_viagens):
    maior = max(km_viagens)
    menor = min(km_viagens)
    print(f'A maior distância é de {maior}km')
    print(f'A menor distância é de {menor}km')
    return maior, menor

def media_distancias(km_viagens,total_km):
    media = total_km / len(km_viagens)
    media_arredondada = math.ceil(media)
    print(f'A médias das viagens são de {media:.2f}km')
    return media_arredondada


def main():
    viagens = distancias()
    total = calcular_distancia(viagens)
    menor_maior = maior_menor(viagens)
    medias = media_distancias(viagens,total)
    

main()