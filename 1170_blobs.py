vez = int(input())
for x in range(vez):
    C = float(input())
    day = 0
    while True:
        if C > 1:
            C = C/2
            day += 1
        else:
            print(f"{day} dias")
            break
#0.087 / 25.05.2021 / 1
