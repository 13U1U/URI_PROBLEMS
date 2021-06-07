go = int(input())
for x in range(go):
    lis = list(input())
    meg = lis[1].upper()
    if int(lis[0]) == int(lis[2]):
        print(int(lis[0]) * int(lis[2]))
    else:
        if lis[1] == meg:
            print(int(lis[2]) - int(lis[0]))
        else:
            print(int(lis[0]) + int(lis[2]))
#0.361 / 04.06.2021 / 6
