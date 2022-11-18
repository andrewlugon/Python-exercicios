def ultima_parada(combustivel,consumo,postos_de_gasolina):
    maximo = combustivel*consumo
    resultado = -1
    for x in postos_de_gasolina:
        if maximo >= x:
            if resultado < x:
                resultado = x     
    return resultado