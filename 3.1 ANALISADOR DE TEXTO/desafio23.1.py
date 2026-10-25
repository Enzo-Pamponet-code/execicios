while True :
    pergunta = input('Fale um numero: ').strip()
    if pergunta.isnumeric() and float(pergunta) <= 9999 :
        dcondicional =' '.join(pergunta)
        split = dcondicional.split()
        a = float(pergunta)
        if len(split) < 4:
            print('milhar: {}\ncentena: {}\ndezena: {}\nunidade: {}'.format(a//1000 % 10, a//100 % 10, a//10 % 10, a%10))
            break
        elif len(split) == 4 :
            sif = dcondicional.split()
            print('milhar: {}\ncentena: {}\ndezena: {}\nunidade: {}'.format(sif[0], sif[1], sif[2], sif[3]))
            break
    else :
        print('Digite um numero entre 0 e 9999')