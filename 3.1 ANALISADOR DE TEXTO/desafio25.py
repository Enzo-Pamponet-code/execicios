while True:
    nome =input('Digite seu nome completo: ').strip().lower()
    if len(nome) == 0 :
        print('Informação incorreta')
    elif nome in 'silva' :
        if 'silva' in nome:
            print('Tem silva')
        else:
            print('não tem silva')
        break
    else :
        print('não tem silva')
        break
