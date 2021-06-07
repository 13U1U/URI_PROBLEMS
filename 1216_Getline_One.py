y = x = 0
while True:
    try:
        ami = str(input())
        dis = float(input())
        x += 1
        y += dis
    except EOFError:
        fff = float(y/x)
        print(f"{fff:.1f}")
        break
#0.240 / 27.05.2021 / 1
