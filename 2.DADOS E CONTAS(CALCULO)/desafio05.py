#--------pergunta----------
a=input('Digite um numero inteiro: ')

#---------lógica-----------
try:
    float(a)
    b= True
except ValueError:
    b = False
if b == True and int(float(a))==float(a):
    print('O sucessor de {} é {}\nO antecessor de {} é {}'.format(int(float(a)),int(float(a))+1,int(float(a)),int(float(a))-1))
if b == False:
    print('O valor digitado não é um numero')
if b == True and int(float(a)) != float(a):
    print('O valor digitado não é inteiro')
