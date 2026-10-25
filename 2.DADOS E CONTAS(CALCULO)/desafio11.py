a=input('Altura da parede em metros: ')
b=input('Largura da parede em metros: ')
try:
    float(a)
    float(b)
    print('Em uma parede com {} metros de altura e {} metros de largura tem uma área de {} metros quadrados, para um balde de tinta que \npode cobrir 2 metros quadrados de tinta, temos que precisamos de {} baldes de tinta'.format(a,b,float(a)*float(b),float(a)*float(b)/2))
except ValueError:
    print('Valor incorreto')