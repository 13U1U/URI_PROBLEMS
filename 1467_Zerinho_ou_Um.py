while True:
    try:
        a, b, c = map(int, input().split())
        if a == b == c:
            print('*')
        else:
            if a != b and a != c:
                print("A")
            else:
                if b != a and b != c:
                    print("B")
                else:
                    print("C")
    except EOFError:
        break
#0.184 / 09.06.2021 / 1
