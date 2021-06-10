x = float(input())
saf = 0
aum = 0
prc = 0
if x <= 400:
    saf = x*1.15
    aum = x*0.15
    prc = 15
else:
    if x <= 800:
        saf = x*1.12
        aum = x*0.12
        prc = 12
    else:
        if x <= 1200:
            saf = x*1.10
            aum = x*0.10
            prc = 10
        else:
            if x <= 2000:
                saf = x*1.07
                aum = x*0.07
                prc = 7
            else:
                saf = x*1.04
                aum = x*0.04
                prc = 4
print(f"Novo salario: {saf:.2f}")
print(f"Reajuste ganho: {aum:.2f}")
print(f"Em percentual: {prc} %")
#0.001 / 10.06.2021 / 3
