while True:
    try:
        x, y = map(int, input().split())
        if x == 0  and y == 0:
            break
        else:
            res = str(x+y)
            res = res.replace("0", "")
            print(res)
    except EOFError:
        break
#0.000 / 07.06.2021 / 2
