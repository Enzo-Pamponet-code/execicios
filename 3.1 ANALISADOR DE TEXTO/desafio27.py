while True:
    a = input('Digite seu nome completo: ').strip().capitalize()
    if len(a) == 0:
        print('errado')
    else:
        b = a.split()
        c = b[-1].capitalize()
        d = b[0]
        print('Seu primeiro nome: {}\nSeu ultimo nome: {}'.format(d, c))
        break