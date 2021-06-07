c, qan = map(int, input().split())
if c == 1:
    print(f"Total: R$ {float(qan * 4.00):.2f}")
elif c == 2:
    print(f"Total: R$ {float(qan * 4.50):.2f}")
elif c == 3:
    print(f"Total: R$ {float(qan * 5.00):.2f}")
elif c == 4:
    print(f"Total: R$ {float(qan * 2.00):.2f}")
else:
    print(f"Total: R$ {float(qan * 1.50):.2f}")
#0.002 / 01.06.2021 / 1
