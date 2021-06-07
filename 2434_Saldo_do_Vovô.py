go, dol = map(int, input().split())
me = dol
for x in range(go):
    op = int(input())
    dol += op
    if me > dol:
        me = dol
print(me)
#0.093 / 07.06.2021 / 2
