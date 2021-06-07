a, b, c, d = map(int, input().split())
if b > c and d > a and c+d > a+b and c+d > 0 and a+b > 0 and a % 2 == 0:
    print("Valores aceitos")
else:
    print("Valores nao aceitos")
#0.033 / 01.06.2021 / 1
