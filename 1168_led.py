go = int(input())
for x in range(go):
    lis = list(str(input()))
    led = 0
    for p in range(len(lis)):
        tt = int(lis[p])
        if tt == 2 or tt == 3 or tt == 5:
            led += 5
        else:
            if tt == 6 or tt == 9 or tt == 0:
                led += 6
            else:
                if tt == 4:
                    led += 4
                else:
                    if tt == 7:
                        led += 3
                    else:
                        if tt == 1:
                            led += 2
                        else:
                            if tt == 8:
                                led += 7
                            else:
                                ...
    print(f"{led} leds")
#0.099 / 26.05.2021 / 1
