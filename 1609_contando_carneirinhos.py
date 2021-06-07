go = int(input())
while go > 0:
    go -= 1
    go2 = int(input())
    Cnho = list(input().split())
    print(len(set(Cnho)))
#0.066 / 26.05.2021 / 1
go = int(input())
while go > 0:
    go -= 1
    go2 = int(input())
    Cnho = list(input().split())
    lis = []
    for f2 in range(go2):
        if Cnho[f2] not in lis:
            lis.append(Cnho[f2])
    print(len(lis))
# Time limit exceeded