x = str(input())
y = str(input())
x = x.split(' ')
y = y.split(' ')
fal = 0
for g in range(len(y)):
    if x[g] == y[g]:
        fal += 1
if fal > 0:
    print('N')
else:
    print('Y')
#0.001 / 05.06.2021 / 3
