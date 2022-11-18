import math
def calcula_porcentagem_sorteio(assinante,minutos_assistidos):
    horas = []
    totalhoras = 0
    resultado = []
    for x in minutos_assistidos:
            x = x/60
            horas.append(math.ceil(x))
    for x in range(0,len(assinante),1):
        if assinante[x]:
            horas[x] = horas[x]*2
        totalhoras += horas[x]
    for x in range(0,len(assinante),1):
        resultadoProvisorio = horas[x]/totalhoras*100
        resultado.append(round(resultadoProvisorio))    
    return resultado