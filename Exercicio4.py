filmes = [
    {
        "titulo": "Inception",
        "diretor": "Christopher Nolan",
        "bilheteria": 830,
        "avaliacoes": [9, 10, 8, 9, 10]
    },
    {
        "titulo": "Avengers: Endgame",
        "diretor": "Anthony Russo",
        "bilheteria": 2797,
        "avaliacoes": [9, 9, 10, 10, 9]
    },
    {
        "titulo": "The Dark Knight",
        "diretor": "Christopher Nolan",
        "bilheteria": 1005,
        "avaliacoes": [10, 10, 9, 10, 10]
    },
    {
        "titulo": "Jurassic Park",
        "diretor": "Steven Spielberg",
        "bilheteria": 1029,
        "avaliacoes": [8, 9, 9, 8, 9]
    }
]

def top_bilheteria(filmes):
    top = []
    usados = []
    for _ in range(3):
        maior = None
        for f in filmes:
            if f not in usados:
                if maior is None or f["bilheteria"] > maior["bilheteria"]:
                    maior = f
        if maior:
            top.append(maior)
            usados.append(maior)
    print("Top 3 Bilheteiras:")
    for f in top:
        print(f"{f['titulo']} - ${f['bilheteria']}M")


def top_avaliacao(filmes):
    top = []
    usados = []
    for _ in range(3):
        melhor = None
        for f in filmes:
            if f not in usados:
                media = sum(f["avaliacoes"]) / len(f["avaliacoes"])
                if melhor is None:
                    melhor = f
                    melhor_media = media
                elif media > melhor_media:
                    melhor = f
                    melhor_media = media
        if melhor:
            top.append((melhor, melhor_media))
            usados.append(melhor)

    print("op 3 Melhor Avaliados:")
    for f, m in top:
        print(f"{f['titulo']} - Média {m:.2f}")

def bilheteria_por_diretor(filmes):
    totais = {}
    for f in filmes:
        diretor = f["diretor"]
        if diretor in totais:
            totais[diretor] += f["bilheteria"]
        else:
            totais[diretor] = f["bilheteria"]
    print("Bilheteria por Diretor:")
    for d, total in totais.items():
        print(f"{d}: ${total}M")

def campeao(filmes):
    melhor = filmes[0]
    score_melhor = melhor["bilheteria"] * (sum(melhor["avaliacoes"]) / len(melhor["avaliacoes"]))
    for f in filmes:
        score = f["bilheteria"] * (sum(f["avaliacoes"]) / len(f["avaliacoes"]))
        if score > score_melhor:
            melhor = f
            score_melhor = score
    print("Campeão Absoluto:")
    print(f"{melhor['titulo']} com score {score_melhor:.1f}")

def main():
    top_bilheteria(filmes)
    top_avaliacao(filmes)
    bilheteria_por_diretor(filmes)
    campeao(filmes)

main()
