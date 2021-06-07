import math
a, b = map(float, input().split())
c, d = map(float, input().split())
ab = float((a - c)**2)
cd = float((b - d)**2)
res = math.sqrt(float(ab+cd))
print(f"{res:.4f}")
#0.035 / 29/05/2021 / 3
