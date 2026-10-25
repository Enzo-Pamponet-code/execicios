a=input('Digite a temperatura em graus Celsius: ')
try:
    b= float(a)*(9/5)+32
    print('A temperatura de C° para F° é de: {} F°'.format(b))
except ValueError:
    print('Valor incorreto')
