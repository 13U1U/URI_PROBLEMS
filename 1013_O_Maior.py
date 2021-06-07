a, b, c = map(int, input().split())
if a>=b and a>=c:
    print(f'{a} eh o maior')
else:
    if b>=a and b>=c:
        print(f'{b} eh o maior')
    else:
        print(f'{c} eh o maior')
#0.000 / 28.05.2021 / 2
