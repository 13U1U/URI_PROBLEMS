while True:
    try:
        cod = str(input())
        res = str(input())
        if res in cod:
            print('Resistente')
        else:
            print('Nao resistente')
    except EOFError:
        break
#0.028 / 09.08.2021 / 1
