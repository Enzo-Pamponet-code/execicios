a=input('Quantidade de km que o carro percorreu: ')
b=input('Quantidade de dias que você está com o carro: ')
try:
    c=float(a)
    d=float(b)
    print('O valor total, sendo que a cada 1 km é 0.15 reais e a cada dia é 60 reais, é: {:.2f} reais'.format(c*0.15 + d*60))
except ValueError:
    print('Valor incorreto')