print('-'*20,'não pode ultrapssar 80 km', '-'*20)
a = input('Qual a sua velocidade?: ').strip().lower()
try :
    if a.find('km') > -1:
        b = a[:len(a) - 2].strip()
        c = float(b)
        if c > 80:
            print('Multado: {} reais'.format((c - 80) * 7))
        else:
            print('Tudo de boas')
    elif float(a) > 80:
        d = float(a)
        print('Multado: {} reais'.format((d - 80) * 7))
    else:
        print('Tudo de boas')
except ValueError:
    print('Valor invalido')
