try:
    a = float(input('Digite o seu salario: '))
    if a > 1250:
        print('O seu novo salário é de {:.2f} reais'.format(a*1.1))
    elif a < 0 :
        print('Erro')
    else:
        print('O seu novo salário é de {:.2f} reais'.format(a*1.15))
except ValueError:
    print('Ocorreu um erro')