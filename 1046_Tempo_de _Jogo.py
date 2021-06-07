ini, fim = map(int, input().split())
h = 0
if ini < fim:
    h = fim - ini
else:
    h = (fim+24) - ini
print(f"O JOGO DUROU {h} HORA(S)")
#0.085 / 04.06.2021 / 1
