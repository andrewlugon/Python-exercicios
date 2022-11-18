def checa_numero_escondido4(numero,numero_oculto):
    numero_lista = list(str(numero))
    oculto = list(str(numero_oculto))
    iguais = [elemento for elemento in oculto if elemento in numero_lista]
    for x in range(0,len(iguais)-1,1):
        for y in range(1,len(iguais),1):
            if iguais[x] > iguais [y] or iguais != oculto:
                return False
    return True