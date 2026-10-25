a=input('Digite um valor em metros: ')
try:
    float(a)
    b = True
except:
    b = False
if b == True:
    print('Valor em centimetros é de:{}\nValor em milimetros é de:{}'.format(float(a)*100,float(a)*1000))
else:
    print('Valor incorreto')