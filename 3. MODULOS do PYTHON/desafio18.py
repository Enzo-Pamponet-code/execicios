#importar
import math
#pergunta
a=input('Digite um ângulo: ')
#lógic
try:
    b=float(a)
    c = math.pi/(180/b)
    print('O sen({}) é {:.5f}\nO cos({}) é {:.5f}\nA tan({}) é {:.5f}'.format(b,math.sin(c),b,math.cos(c),b,math.tan(c)))
except:
    print('Valor invalido')