#Identificar número maior

def numero_maior():
    
    if n1 > n2:
        return n1
    elif n1 < n2:
        return n2
    else:
        return None

n1 = int(input('Digite Aqui um número: '))
n2 =int(input('Digite Aqui outro número: '))
    

resultado = numero_maior()
if resultado == None:
    print('Os números são iguais')
else:
    print(resultado)