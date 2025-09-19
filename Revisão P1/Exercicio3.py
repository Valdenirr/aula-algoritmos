# Lista de músicas
musicas = [
    {
        "titulo": "Back in Black",
        "artista": "AC/DC",
        "downloads": 6800,
        "avaliacoes": [5, 4, 5, 5, 4, 5]
    },
    {
        "titulo": "Stairway to Heaven",
        "artista": "Led Zeppelin",
        "downloads": 8900,
        "avaliacoes": [5, 5, 4, 5, 5, 5]
    },
    {
        "titulo": "Enter Sandman",
        "artista": "Metallica",
        "downloads": 8100,
        "avaliacoes": [5, 5, 5, 4, 4, 5, 5]
    }
]

def media_avaliacoes(musicas):
    print("=== Média das Avaliações ===")
    for musica in musicas:
        media = sum(musica["avaliacoes"]) / len(musica["avaliacoes"])
        print(musica["titulo"], "->", round(media, 2))

def artista_top_downloads(musicas):
    downloads_artistas = {}
    for musica in musicas:
        artista = musica["artista"]
        if artista not in downloads_artistas:
            downloads_artistas[artista] = 0
        downloads_artistas[artista] += musica["downloads"]

    maior_downloads = -1
    artista_top = ""
    for artista, total in downloads_artistas.items():
        if total > maior_downloads:
            maior_downloads = total
            artista_top = artista

    print("Artista com mais downloads")
    print(artista_top, "->", maior_downloads)


def ranking_musicas(musicas):
    ranking = []
    for musica in musicas:
        media = sum(musica["avaliacoes"]) / len(musica["avaliacoes"])
        ranking.append((musica["titulo"], round(media, 2)))

    resultado = []
    while ranking:
        maior = ranking[0]
        for item in ranking:
            if item[1] > maior[1]:
                maior = item
        resultado.append(maior)
        ranking.remove(maior)

    print("Ranking das Músicas Mais Bem Avaliadas")
    for pos, (titulo, media) in enumerate(resultado, start=1):
        print(f"{pos}º lugar: {titulo} -> {media}")


def main():
    media_avaliacoes(musicas)
    artista_top_downloads(musicas)
    ranking_musicas(musicas)

main()
