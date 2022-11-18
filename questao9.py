def shuffle_musicas(musicas_tocadas):
    ordem = sorted(musicas_tocadas)
    novaLista = []
    maiorlista = []
    menorlista = []
    tamanho = len(ordem)
    y = 1
    print(int(tamanho/2))
    for x in range(int(tamanho/2)):
        menorlista.append(ordem[x])
        maiorlista.append(ordem[tamanho-y])
        y += 1
    for x in range(int(tamanho/2)):
        novaLista.append(maiorlista[x])
        novaLista.append(menorlista[x])
    if tamanho%2 == 1:
        novaLista.append(ordem[int(tamanho/2)])
    if len(musicas_tocadas) == 1:
        novaLista = musicas_tocadas    

    return novaLista