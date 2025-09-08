#Controle Presença

def registrar_presença():
    presenças = {}
    while True:
        dia = input('Digite o dia da semana ou Digite "sair" para finaliar o programa: ').upper()
        if dia == 'SAIR':
            break
        else:
            alunos=[]
            print(f'Presença {dia}')

            while True:
                nomes= input('Digite o nome do aluno / Digite "sair" para encerrar o programa: ').upper()
                if nomes == 'SAIR':
                    break
                else:
                    alunos.append(nomes)
            
            presenças[dia] = alunos
            print(f'Presenças de {dia} alunos: {alunos}')
    
    print(f'== Registros das Presenças ==')
    print(presenças)
    return presenças

def verificar_presenças(presenças):
    total_alunos = []
    for dia in presenças:
        total_alunos.extend(presenças[dia])
    todos_alunos = set(total_alunos)
    
    presente_todos_dias = []
    
    for aluno in todos_alunos:
        veio_todos = True

        for dia in presenças:
            if aluno not in presenças[dia]:
                veio_todos = False
                break
        if veio_todos:
            presente_todos_dias.append(aluno)    
    return presente_todos_dias

def faltas(presenças, presentes_todos_dias):
    todos_alunos = set()
    for dia in presenças:
        for aluno in presenças[dia]:
            todos_alunos.add(aluno)
    return todos_alunos - set(presentes_todos_dias)

def contar_presença(presenças):
    contagem = {}
    for dia in presenças:
        for aluno in presenças[dia]:
            if aluno in contagem:
                contagem[aluno] += 1
            else:
                contagem[aluno] = 1
    return contagem

def main():
    presença = registrar_presença()
    presente_todos_dias = verificar_presenças(presença)
    faltantes = faltas(presença, presente_todos_dias)
    contagem = contar_presença(presença)
    
    print(f'Alunos presentes todos os dias: {presente_todos_dias}')
    print(f'Alunos que faltamram pelo menos um dia: {faltantes}')
    print(f'Total de presenças por alunos: {contagem}')

main()   
