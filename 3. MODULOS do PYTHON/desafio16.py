#importar
import math
#pergunta
a=input('digite um numero quebrado: ')
#logica para não da erro
try:
    b=float(a)
    if float(a) != int(float(a)):
        print('O inteiro de {} é {}'.format(a, math.trunc(b)))
    else:
        print('O valor não é quebrado')
except ValueError:
    print('Valor incorreto')