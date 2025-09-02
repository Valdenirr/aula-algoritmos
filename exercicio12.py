#Numeos pares e nnumeros impares

num_par = []
num_impar = []

for i in range(10):
    numeros=int(input('Digite aqui os seus números: '))
    if numeros %2 ==0:
        num_par.append(numeros)
    else:
        num_impar.append(numeros)

print(f'foram digitados {len(num_par)} números pares que são {num_par} e foram digitados {len(num_impar)} numeros impares que são {num_impar}!')