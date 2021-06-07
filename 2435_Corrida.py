c1, dis1, vel1 = map(int, input().split())
c2, dis2, vel2 = map(int, input().split())
tin1 = dis1/vel1
tin2 = dis2/vel2
if tin1 < tin2:
    print(c1)
else:
    print(c2)
#0.041 / 01.06.2021 / 9
