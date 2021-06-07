while True:
    go = int(input())
    if go == 0:
        break
    lis = -1
    marywin = johnwin = cont = 0
    x =  input()
    win = x.split()

    for x in range(len(win)):
        lis += 1
        cont = int(win[lis])
        if cont == 0:
            marywin += 1
        else:
            johnwin += 1

    print(f"Mary won {marywin} times and John won {johnwin} times")
#0.075 / 25.05.2021 / 5