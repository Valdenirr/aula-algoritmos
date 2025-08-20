## Função pasa saber número primo!
def primo():
    n1= int(input('Digite o número para saber se é primo: '))
    if n1 %2 == 0:
        print(f' o número {n1} não é primo ')
    else:
        print(f'O número {n1} é primo')
primo()
