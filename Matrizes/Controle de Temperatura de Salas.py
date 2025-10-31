matriz = []
for i in range ( 5 ) :
    input("Digite o nome da Sala: ")
    linha = []
    for j in range ( 3) :
        linha.append(int(input( ) ))
    matriz.append(linha)
print(matriz)

def mediaTemp(matriz):
    soma_total = 0
    numero_elementos = 0

    for linha in matriz:
        soma_total += sum(linha)
        numero_elementos += len(linha)
        media = soma_total / numero_elementos

    print(f"A média das temperturas são de {media:.2f} C°")
mediaTemp(matriz)