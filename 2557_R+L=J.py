while True:
    try:
        res = 0
        lis = str(input())
        lis = lis.replace('=', '@')
        lis = lis.replace('+', '@')
        lis = lis.split('@')
        if "J" in lis:
            res = int(lis[0]) + int(lis[1])
        else:
            if "R" in lis:
                res = int(lis[2]) - int(lis[1])
            else:
                if "L" in lis:
                    res = int(lis[2]) - int(lis[0])
                else:
                    ...
        print(res)
    except EOFError:
        break
#0.014 / 01.06.2021 / 1
