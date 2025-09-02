#Calculo PA

numero = int(input('Digite um número: '))
soma = 0
contador = 0

for i in range(1, numero + 1):
    soma= soma + i
    contador = contador + 1
   
resultado = numero *(numero +1)//2

print(f'A soma dos números de 1 até {numero} é {soma}')
print(f'Foram realizadas {contador} operações') 
print(f'O resultado pela fórmula é {resultado}')