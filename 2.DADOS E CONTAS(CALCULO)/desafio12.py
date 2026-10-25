a=input('Preço de um produto:R$ ')
try:
    float(a)
    print('Esse produto com 5% de desconto vale: {:.2f}'.format(float(a)-float(a)*(5/100)))
except ValueError:
    print('Valor invalido')