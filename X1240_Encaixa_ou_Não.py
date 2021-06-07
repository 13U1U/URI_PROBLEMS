while True:

    go = int(input())
    if go == 0:
        break
    for x in range(go):
        n1,n2 = map(str,input().split())


        j = int(n1[-1])
        y = int(n1[-1])
        z = int(n1[-2])
        w = int(n2[-2])
        if j == y and z == w :
            print("encaixa")
        else:
            print("nao encaixa")