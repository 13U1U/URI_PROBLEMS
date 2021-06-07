while True:
    try:
        a, b = map(int, input().split())
        if a == 0 and b == 0:
            break
        else:
            m1 = str(input())
            m2 = str(input())
            if m2 in m1:
                print('S')
            else:
                print('N')

    except EOFError:
        break
