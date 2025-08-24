#Busca de nomes em uma lista

nomes = ["Maria", "Thiago", "Anderson", "José", "Glauber", "Felipe"]
nomes_maiusculo = [nome.upper() for nome in nomes]

def buscar_nomes(nomes):
    pesquisa = input("Digite o nome para pesquisar: ").upper().strip()
    if pesquisa in nomes:
        posicao = nomes.index(pesquisa)
        print(f"O nome {pesquisa} está na posição {posicao}.")
    else:
        print("Nome não encontrado.")


buscar_nomes(nomes_maiusculo)