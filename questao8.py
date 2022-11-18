def escolhe_taxi(tf1,vqr1,tf2,vqr2):
    cont1 = 0
    cont2 = 0
    cont3 = 0.0
    resultado = "Tanto faz"
    for x in range(1 ,1000, 1): 
        z = 0   
        if float(tf1) + (float(vqr1) * x) < float(tf2) + (float(vqr2) * x):
            cont1 += 1
        if float(tf2) + (float(vqr2) * x) < float(tf1) + (float(vqr1) * x):
            cont2 += 1
        for y in range(0 , 20, 1):
            if float(tf2) + (float(vqr2) * (x+z)) == float(tf1) + (float(vqr1) * (x+z)):
                cont3 += x+z
            z += 0.01 
            if x+z == 7.14:
                if round(float(tf2) + (float(vqr2) * (x+z)),2) == round(float(tf1) + (float(vqr1) * (x+z)),2):
                    cont3 += x+z
    if cont1 > 0 and cont2 == 0:
        resultado = "Empresa 1"
    if cont2 > 0 and cont1 == 0:
        resultado = "Empresa 2"
    if cont1 > 0 and cont2 > 0:
        if cont1 < cont2:
            resultado = f'Empresa 1 quando a distância < {cont3}, Tanto faz quando a distância = {cont3}, Empresa 2 quando a distância > {cont3}'
        if cont2 < cont1:
            resultado = f'Empresa 2 quando a distância < {cont3}, Tanto faz quando a distância = {cont3}, Empresa 1 quando a distância > {cont3}'
    return resultado