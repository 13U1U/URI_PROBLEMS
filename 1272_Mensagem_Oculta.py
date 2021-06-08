go = int(input())
for t in range(go):
    lis = input().split()
    r = ''
    for x in range(len(lis)):
        pal = str(lis[x])
        pli = list(pal)
        r += str(pli[0])
    print(r)
#0.354 / 08.06.2021 / 1
