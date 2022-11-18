def anagramas(palavra):
    if len(palavra) <=1:
        return palavra
    else:
        tmp = []
        for aux in anagramas(palavra[1:]):
            for i in range(len(palavra)):
                tmp.append(aux[:i] + palavra[0:1] + aux[i:])
        return tmp

def menor_string_maior(name):
    variacoes = sorted(set(anagramas(name)))
    r = "sem resposta"
    for x in variacoes:
        if x > name:
            r = x
            break
    return r