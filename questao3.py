def retorna_menor_e_maior_valor_de_vendas(tickets):
    menor_valor = tickets[0][0]
    maior_valor = tickets[0][0]
    for x in range(len(tickets)):
        for y in range(len(tickets[x])):
            if tickets[x][y] != 0 and tickets[x][y]>20 and tickets[x][y]<500 :    
                if tickets[x][y] < menor_valor:
                    menor_valor = tickets[x][y]
                if tickets[x][y] > maior_valor:
                    maior_valor = tickets[x][y]
    resultado = [menor_valor,maior_valor]
    return resultado  