# Lista de atletas (igual ao exemplo da imagem)
atletas = [
    {
        "nome": "Lucas",
        "idade": 20,
        "modalidades": ["Natação", "Corrida"],
        "treinos": {"Natação": 12, "Corrida": 8}
    },
    {
        "nome": "Mariana",
        "idade": 25,
        "modalidades": ["Musculação", "Yoga", "Pilates"],
        "treinos": {"Musculação": 15, "Yoga": 10, "Pilates": 5}
    },
    {
        "nome": "João",
        "idade": 22,
        "modalidades": ["Corrida", "Ciclismo"],
        "treinos": {"Corrida": 20, "Ciclismo": 18}
    }
]

def media_idade(atletas, esporte):
    soma = 0
    cont = 0
    for atleta in atletas:
        if esporte in atleta["modalidades"]:
            soma += atleta["idade"]
            cont += 1
    if cont == 0:
        print("Nenhum atleta pratica", esporte)
    else:
        print("Média de idade dos que fazem", esporte, ":", soma / cont)


def esporte_mais_treinado(atleta):
    maior_treino = -1
    esporte_mais = ""
    for esporte, qtd in atleta["treinos"].items():
        if qtd > maior_treino:
            maior_treino = qtd
            esporte_mais = esporte
    print("Esporte mais treinado de", atleta["nome"], ":", esporte_mais, "-", maior_treino, "treinos")


def atletas_multimodais(atletas):
    multimodais = []
    for atleta in atletas:
        if len(atleta["modalidades"]) > 2:
            multimodais.append(atleta["nome"])
    print("Atletas com mais de 2 modalidades:", multimodais)

def main():
    media_idade(atletas, "Corrida")
    esporte_mais_treinado(atletas[2]) 
    atletas_multimodais(atletas)


main()
