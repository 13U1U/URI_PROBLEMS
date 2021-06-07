while True:
    try:
        go = input().strip()
        res = 1
        if go == "0":
            break
        for x in range(len(go)):
            res = (1+x)*res
        print(res)
    except EOFError:
        break

#0.018 / 27.05.2021 / 4
