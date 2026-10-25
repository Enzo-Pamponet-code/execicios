a=input('Digite a sua primeira nota: ')
b=input('Digite sua segunda nota: ')
try:
    float(a)
    float(b)
    c = True
except ValueError:
    c = False
if c == True:
    print('Sua média é de {:.2f}'.format((float(a)+float(b))/2))
else:
    print('Você não digitou a sua nota com números')