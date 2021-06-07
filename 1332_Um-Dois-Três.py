go = int(input())
for x in range(go):
    lis = list(input().upper())
    if len(lis) >= 5:
        print('3')
    else:
        if lis[0] == 'T' and lis[1] == 'W':
            print('2')
        else:
            if lis[0] == 'T' and lis[2] == "O":
                print('2')
            else:
                if lis[1] == 'W' and lis[2] == "O":
                    print('2')
                else:
                    print('1')
#0.082 / 02.06/2021 / 3
