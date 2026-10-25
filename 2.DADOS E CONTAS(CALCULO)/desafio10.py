a=input('Digite quanto você tem carteira:R$ ')
try:
    float(a)
    print('Você poderia comprar em 2016 com esses dolares: ${:.2f}'.format(float(a)/3.27))
except ValueError:
    print('Valor incorreto')