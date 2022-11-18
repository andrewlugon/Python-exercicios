def calcula_top_ocorrencias_de_queries(texto,queries,k):

    lista = []
    lista2 = []
    resultado = []

    for x in queries:
        counta = texto.count(x)
        lista.append(str(counta)) 
        lista2.append(x)

    for y in range(k):
        contador = 0
        remover = 0
        for x in range(0, len(lista),1):
            if int(lista[x]) > contador:
                contador = int(lista[x])
                remover = x  
        resultado.append(lista2[remover])   
        lista.remove(lista[remover])
        lista2.remove(lista2[remover])       
    
    return resultado