#Verificador de Cpf

cpf=(input('Digite o número do Cpf sem os digitos: '))

def verificardor_cpf(cpf):
    if cpf == int(cpf):
        return True
    if len(cpf) == 11:
        print('Cpf válido')
    else:
        print('Cpf inválido')

verificardor_cpf(cpf)