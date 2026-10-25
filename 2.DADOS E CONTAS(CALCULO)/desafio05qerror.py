#-------Pergunta---------
a=input('Digite um número: ')

#------pré lógica------
try:
    float(a)
    z= True
except ValueError:
    z = False
c= a.isnumeric()
if z== True:
    b = int(float(a)) == float(a)
d= a.isalpha() or a.isalnum()
#-------Os "SE"----------
if b == True:
    print('O sucessor de {} é {}\nO antecessor de {} é {}'.format(int(float(a)),int(float(a))+1,int(float(a)),int(float(a))-1))
if d== True:
    print('Você não digitou um número')
if b == False:
    print('Tem que ser inteiro')
