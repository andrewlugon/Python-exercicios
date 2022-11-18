def calcula_total_leds(altura,largura): 
    ledAltura = 4 + (2*(altura-1))
    ledLargura = (altura + 1) * (largura-1)
    print(ledAltura,ledLargura)
    resultado = ledAltura + ledLargura
    if altura==0 or largura==0:
        return 0
    else:
        return resultado

print(calcula_total_leds(2,3))