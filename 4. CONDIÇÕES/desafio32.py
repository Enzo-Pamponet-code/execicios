from datetime import date
try:
    a = int(input('Fale um ano(se for igual a 0 vai mostrar o ano atual): '))
    if a == 0:
        b = date.today().year
        if b % 4 == 0 and a % 100 != 0:
            print('Ano de {} é bissexto'.format(b20))
        elif b % 4 == 0 and a % 100 == 0 and a % 400 == 0:
            print('Ano de {} é bissexto'.format(b))
        else:
            print('Ano de {} não é bissexto'.format(b))
    elif a % 4 == 0 and a % 100 != 0:
        print('Ano bissexto')
    elif a % 4 == 0 and a % 100 == 0 and a % 400 == 0:
        print('Ano bissexto')
    else:
        print('Ano não bissexto')
except ValueError:
    print('Valor invalido')