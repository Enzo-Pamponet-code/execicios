try :
    a = int(input('Digite um numero: '))
    if a//2 == a/2:
        print('Par')
    else:
        print('Impar')
except ValueError:
    print('Valor invalido')