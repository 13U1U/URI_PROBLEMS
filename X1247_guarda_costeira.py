def guarda(D, VF, VG):
    if D > 11:
        print("N")
    else:
        if VF > VG - 1:
            print("N")
        if VF < VG:
            print("S")


while True:

    try:
        A, B, C = map(int, input().split())
        guarda(A, B, C)

    except EOFError:
        break
