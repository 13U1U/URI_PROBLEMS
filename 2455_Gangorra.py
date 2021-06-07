z, y, x, w = map(int, input().split())


def gangorra(p1, c1, p2, c2):
    cri1 = float(p1 * c1)
    cri2 = float(p2 * c2)

    if p1 == 0 or c1 == 0 or p2 == 0 or c2 == 0:
        print(1)
        print(-1)
    else:
        if cri1 == cri2:
            print("0")
        else:
            if cri1 > cri2:
                print("-1")
            else:
                print("1")


gangorra(z, y, x, w)
#0.014 / 25.05.2021 / 46
