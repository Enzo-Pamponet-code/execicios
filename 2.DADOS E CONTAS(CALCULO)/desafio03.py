n1 = input('digite um numero ')
n2 = input('digite outro numero ')
n3 = n1.isnumeric()
n4 = n2.isnumeric()
if n3 and n4:
    print('A soma entre {} e {} dá {}'.format(n1, n2, float(n1) + float(n2)))
if n3== False or n4== False:
    print('Só pode numeros')