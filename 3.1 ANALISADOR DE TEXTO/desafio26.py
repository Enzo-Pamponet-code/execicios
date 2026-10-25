while True:
    digite = input('Digite algo: ').strip().lower()
    if len(digite) == 0 :
        print('Quantidade de vezes que o A aparece: 0\nQuando o A aparece: 0\n Quando o A acaba: 0')
    else:
        if digite.count('a') == 0 :
            print('Quantidade de vezes que o A aparece: 0\nQuando o A aparece: 0\n Quando o A acaba: 0')
        else:
            v1 = digite.count('a')
            v2 = int(digite.find('a'))+1
            v3 = digite.rfind('a') + 1
            print('Quantidade de vezes que o A aparece: {}\nQuando o A aparece: {}\n Quando o A acaba: {}'.format(v1,v2,v3))