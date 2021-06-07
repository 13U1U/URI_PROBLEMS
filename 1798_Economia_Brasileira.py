n = s = 0
go = int(input())
res = input().split()
for X in range(go):
    if res[X] == '1':
        n += 1
    else:
        s += 1
if s > n:
    print('Y')
else:
    print('N')
#0.126 / 28.05.2021 / 1
