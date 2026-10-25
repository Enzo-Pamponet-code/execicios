while True :
    pergunta = input('Fale um numero: ').strip()
    if pergunta.isnumeric() and float(pergunta) <= 9999 :
        dcondicional =' '.join(pergunta)
        split = dcondicional.split()
        if len(split) < 4:
            sif = ('0 '+dcondicional).split()
            print('milhar: {}\ncentena: {}\ndezena: {}\nunidade: {}'.format(sif[0], sif[1], sif[2], sif[3]))
        elif len(split) == 4 :
            sif = dcondicional.split()
            print('milhar: {}\ncentena: {}\ndezena: {}\nunidade: {}'.format(sif[0], sif[1], sif[2], sif[3]))
        elif len(split) == 2 :
            sif = ('0 0 '+dcondicional).split()
            print('milhar: {}\ncentena: {}\ndezena: {}\nunidade: {}'.format(sif[0], sif[1], sif[2], sif[3]))
        elif len(split) == 1 :
            sif = ('0 0 0 '+dcondicional).split()
            print('milhar: {}\ncentena: {}\ndezena: {}\nunidade: {}'.format(sif[0], sif[1], sif[2], sif[3]))
        else :
            sif = ('0 0 0 0 '+dcondicional).split()
            print('milhar: {}\ncentena: {}\ndezena: {}\nunidade: {}'.format(sif[0], sif[1], sif[2], sif[3]))
        break
    else :
        print('Digite um numero entre 0 e 9999')