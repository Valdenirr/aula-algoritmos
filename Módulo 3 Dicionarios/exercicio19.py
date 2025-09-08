    #Sistema bibliotecario
livros = {
        "Dom Casmuro" : {"usuario" : "Ana", "dias" : 5,},
        "1984": {"usuario" : "Carlos", "dias" : 12,},
        "O Hobbit": {"usuario" : "Marina", "dias" : 3},
        "Viagem ao centro da terra": {'usuario' : "Marcelo", "dias" : 8 },
        "Dom Quixote" : {"usuario" : "Jamal", "dias" : 6}
        }
def emprestado_7_dias():
    mais_7_dias = []
    for titulo, info in livros.items():
        if info['dias'] > 7:
            mais_7_dias.append(f"{titulo} - {info["dias"]} dias ")
    return mais_7_dias

def emprestado_mais_tempo():
    maior_dia = 0
    nome_livro = ""
    for livro, info in livros.items():
        if info["dias"] > maior_dia:
            maior_dia = info["dias"]
            nome_livro = livro
    return f"{nome_livro} - {maior_dia} dias"

def livros_emprestados():
    nomes = []
    for livro, info in livros.items():
        nomes.append(info["usuario"])
    return nomes

def calcular_medias():
    dias = 0
    total_livros = 0
    for livro, info in livros.items():
        dias = dias + info["dias"]
        total_livros += 1
    media = dias / total_livros
    return media

def main():
    mais_7_dias = emprestado_7_dias()
    mais_tempo = emprestado_mais_tempo()
    livros = livros_emprestados()
    media = calcular_medias()
    print(f"Os livros que estão emprestados a mais de 7 dias são : {mais_7_dias}")
    print(f"O livro emprestado a mais tempo é o: {mais_tempo}")
    print(f"Os usuários que tem livros emprestados são: {livros}")
    print(f"Á media de dias de empréstimos são de: {media}dias")

main()