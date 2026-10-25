a=input('Digite um número: ')
try:
    int(float(a))==float(a)
    print('{}*1={}\n{}*2={}\n{}*3={}\n{}*4={}\n{}*5={}\n{}*6={}\n{}*7={}\n{}*8={}\n{}*9={}\n{}*10={}'.format(a,a,a,int(a)*2,a,int(a)*3,a,int(a)*4,a,int(a)*5,a,int(a)*6,a,int(a)*7,a,int(a)*8,a,int(a)*9,a,int(a)*10))
except ValueError:
    print('Valor invalido')