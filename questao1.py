def calcula_numero_da_senha(senha):
    decodificacao = ''
    for y in range(10):
        contador1 = 0
        contador0 = 0
        for x in range(len(senha)):
            p = senha[x]
            if p[y] == '0':
                contador0 += 1
            else:
                contador1 += 1
        if contador1 > contador0:
            decodificacao += '1'
        if contador0 > contador1:
            decodificacao += '0'
        if contador1 == contador0:
            decodificacao += '1'

    binario = int(decodificacao)
    n = len(str(binario))
    decimal = 0
    i = 0
    while n >= 0:
        resto = binario % 10
        decimal = decimal + (resto * (2**i))
        n = n - 1
        i = i + 1
        binario = binario//10
    return decimal