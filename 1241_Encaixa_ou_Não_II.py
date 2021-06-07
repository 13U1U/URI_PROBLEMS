while True:
    try:
        go = int(input())
        for x in range(go):
            a, b = list(map(str, input().split()))
            tes = []
            tes2 = []
            if len(a) < len(b):
                print('nao encaixa')
            else:
                for y in range(len(b)):
                    y += 1
                    tes.append(a[-y])
                    tes2.append(b[-y])
                if tes2 == tes:
                    print('encaixa')
                else:
                    print('nao encaixa')
    except EOFError:
        break
