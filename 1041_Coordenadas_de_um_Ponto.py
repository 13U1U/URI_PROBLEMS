x, y = map(float, input().split())
if x == 0 and y == 0:
    print("Origem")
else:
    if x > 0 and y > 0:
        print('Q1')
    else:
        if x > 0 and y < 0:
            print('Q4')
        else:
            if x < 0 and y > 0:
                print('Q2')
            else:
                if x < 0 and y <0:
                    print('Q3')
                else:
                    if y == 0:
                        print('Eixo X')
                    else:
                        print('Eixo Y')
#0.001 / 01.06.2021 / 2
