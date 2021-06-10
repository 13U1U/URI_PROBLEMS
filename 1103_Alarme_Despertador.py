while True:
    h1, m1, h2, m2 = map(int, input().split())
    res = 0
    if  h1 == m1 == h2 == m2 == 0:
        break
    else:
        if h1 == h2 and m1 >= m2: #hora
            res += 1440
            res -= m1 - m2
        elif h1 == h2 and m1 < m2:
            res += m2 - m1
        else:
            if h1 < h2:
                res += (h2 - h1) * 60
                res += m2 - m1
            else:
                res += (h2+(24-h1))*60
                res += m2-m1
    print(res)
#0.000 / 09.06.2021 / 1
