try:
    c1 = float(input('Comprimento do primeiro segmento de reta: '))
    c2 = float(input('Compimento da segunda reta: '))
    c3 = float(input('Comprimento da terceira reta: '))
    if c1 < c2 + c3 and c2 < c1 + c3 and c3 < c1 + c2:
        print('É possivel formar um triangulo com essas medidas')
    else:
        print('não é possivel formar um triangulo')
except ValueError:
    print('Valor invalido')