while True:
    try:
        N = int(input())
        meat_dict = {}
        meat_order = ""
        if(0 <= N <= 10):
            for i in range(N):
                meat,Di = input().split(" ")
                meat_dict.setdefault(int(Di),meat)

            for key in sorted(meat_dict):
                meat_order+=meat_dict[key]+" "

            print(meat_order[:-1])

    except EOFError:
        break
#0.035 / 30/05/2021 / 19
