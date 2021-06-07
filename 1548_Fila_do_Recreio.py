go = int(input())
for x in range(go):
    alu = int(input())
    nota1 = list(input().split())
    notafin = []
    f1 = []
    resposta = 0
    j = 0
    for t in range(alu):
        tes1 = float(nota1[t])
        f1.append(str(tes1/1000))
    f2 = sorted(f1)
    for y in range(alu):
        j -= 1
        notafin.append(f2[j])
    for q in range(alu):
        if notafin[q] == f1[q]:
            resposta += 1
        else:
            ...
    print(resposta)
#0.224 / 31/05/2021 / 1