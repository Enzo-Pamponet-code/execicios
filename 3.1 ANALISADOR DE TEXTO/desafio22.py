#------------um programa que pegue o nome de uma pessoa e deixe ele maiúsculo; minuscula ; quantas letras tem sem considerar o espaço e quantas letras tem o primeiro nome------------------
while True :
    nome = input('Digite o seu nome todo: ').strip()
    if len(nome) > 0 :
        tf_ = nome.split()
        tf = ''.join(tf_)
        tf0 = tf.isalpha()
        v_ = nome.upper()
        v_0 = nome.lower()
        v_1 = nome.split()
        v_2 = len(''.join(v_1))
        v_3 = len(v_1[0])
        
        if tf0:
            print('Seu nome em letra maiuscula: {}\nSeu nome em letra minuscula: {}\nQuantidade de letras: {}\nQuantidade de letras tem o seu primeiro nome: {}\n'.format(
                    v_, v_0, v_2, v_3))
            break
        else:
            print('Nome não tem numero! Refaça!')
    else :
        print('Zero caracter')