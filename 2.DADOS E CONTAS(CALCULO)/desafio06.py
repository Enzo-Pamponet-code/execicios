a=input('digite um numero: ')
try:
    float(a)
    b= True
except ValueError:
    b = False
if b == True:
    print('o dobro de {} é {}\nA raiz quadrada de {} é {:.2f}\nO triplo de {} é {}'.format(a,float(a)*2,a,float(a)**(1/2),a,float(a)*3))
if b == False:
    print('O valor digitado não é um número')
