a=input('Fale o seu salário: ')
try:
    b=float(a)*1.15
    if float(a)>=0:
        print('O seu salário era de {} Reais para {:.2f} Reais'.format(a, b))
    else:
        print('valor negativo')
except ValueError:
    print('Valor incorreto')
