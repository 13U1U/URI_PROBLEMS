numT = 0
res = 0
while True:
    go = int(input())
    if go == 0:
        break
    else:
        lis = input().split()
        numT += 1
        for x in range(len(lis)):
            if x+1 == int(lis[x]):
                res = lis[x]
            else:
                ...
        print(f"Teste {numT}")
        print(res)
        print()
#0.000 / 10.06.2021 / 2
