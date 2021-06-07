fl = int(input())
lis = input().split()
if '*' in lis:
    res = int(lis[0]) * int(lis[2])
else:
    res = int(lis[0]) + int(lis[2])
if res > fl:
    print('OVERFLOW')
else:
    print('OK')
#0.028 / 02.06.2021 / 1
