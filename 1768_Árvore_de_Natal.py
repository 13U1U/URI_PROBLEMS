while True:
    try:
        go = int(input())
        ast = 1
        esp = int(go/2)
        fin = esp
        while True:
            esp -= 1
            if esp <= 0:
                print("*"*ast)
            else:
                print(" "* (esp-1) , "*"*ast)
            ast += 2
            if ast >= go:
                break
        print(" " * (fin-2) , '*')
        print(" " * (fin-3) , '***')
        print()

    except EOFError:
        break
