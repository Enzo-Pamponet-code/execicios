try :
    a = float(input('Qual é a distancia da viagem: '))
    if a <= 200:
        print('O valor é de {:.2f}'.format(a*0.5))
    else:
        print('O valor é de {:.2f}'.format(a*0.45))
except ValueError:
    print('Valor invalido')