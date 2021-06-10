while True:
    lis = input().upper().split()
    t1 = list(lis[0])
    res = str(t1[0])
    fi = 'Y'
    if lis[0] == '*':
        break
    else:
        for x in range(len(lis)):
            tes = list(lis[x])
            if res == tes[0]:
                ...
            else:
                fi = 'N'
    print(fi)
#0.081 / 10.06.2021 / 1
