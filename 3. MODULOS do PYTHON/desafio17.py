#importar
import math
#pergunta
a = input('Fale o valor do primeiro cateto: ')
b = input('Fale o valor do segundo cateto: ')
#parte logica
try:
    c = float(a)
    d = float(b)
    if math.sqrt((c**2)+(d**2)) == int(math.sqrt((c**2)+(d**2))) :
        print('A hipotenusa vale {}'.format(int(math.sqrt((c**2)+(d**2)))))
    else:
        print('A hipotenusa vale {}'.format(float(math.sqrt((c**2)+(d**2)))))
except ValueError:
    print('Valor incorreto')