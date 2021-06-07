while True:
    try:
        lis = []
        go = int(input())
        for x in range(go):
            ago = str(input())
            lis.append(ago)
        lis.sort()
        for y in range(len(lis)):
            print(lis[y])
    except EOFError:
        break
#0.084 / 28.05.2021 / 3
