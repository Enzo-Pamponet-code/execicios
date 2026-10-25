while True:
        cidade = input('Digite o nome da cidade: ').strip().lower()
        if len(cidade) == 0:
            print('Não tem letra.')
            continue
        pro = cidade.split()
        if cidade.find('santo') > -1 or cidade.find('santo') > -1:
            if pro[0] in ['santo', 'santos']:
                print('Tem Santo(s) na primeira palavra')
                break
            else:
                print('Tem Santos(s), mas não é na primeira palavra.')
                break
        else:
            print('Pelo visto não tem santos.')
            break