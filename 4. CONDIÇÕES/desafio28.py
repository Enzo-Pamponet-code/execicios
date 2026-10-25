import random
ponto = 0
while True:
    try:
        print('-'*20,'Irei pensar um numero entre 0 e 5','-'*20)
        a = random.randint(0, 5)
        b = int(input('Digite um numero entre 0 e 5: '))
        print('-'*20,'Processando...','-'*20)
        if a == b:
            print('Você acertou, {} estava correto'.format(a))
            ponto += 1
        else:
            print('Você errou, numero escolhido: {}'.format(a))
    except ValueError:
        print('numero invalido')
    print('\033[0;31m{}\033[m'.format(ponto))