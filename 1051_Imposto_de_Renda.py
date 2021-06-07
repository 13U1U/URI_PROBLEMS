ren = float(input())
if ren <= 2000.0:
    print('Isento')
else:
    if ren <= 3000.0:
        ren -= 2000.0
        ren = float(ren*0.08)
    else:
        if ren <= 4500.0:
            ren -= 3000
            ren = float(ren*0.18+80)
        else:
            ren -= 4500
            ren = float(ren*0.28+350)
    print(f"R$ {ren:.2f}")
