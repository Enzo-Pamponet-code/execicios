import random
a=input('Nome do primeiro aluno: ')
b=input('Nome do segundo aluno: ')
c=input('Nome do terceiro aluno: ')
d=input('Nome do quarto aluno: ')
e = random.sample([a, b , c , d], k=4)
print(e)