try:
    a = int(input('Digite um valor: '))
    b = int(input('Digite um valor: '))
    c = int(input('Digite um valor: '))
    if a>b>c :
        print('{},{},{}'.format(a, b, c))
    elif a>c>b:
        print('{},{},{}'.format(a, c, b))
    elif b>a>c:
        print('{},{},{}'.format(b, a, c))
    elif b>c>a:
        print('{},{},{}'.format(b, c, a))
    elif c>a>b:
        print('{},{},{}'.format(c, a, b))
    elif c>b>a:
        print('{},{},{}'.format(c, b, a))
except ValueError:
    print('Valor invalido')