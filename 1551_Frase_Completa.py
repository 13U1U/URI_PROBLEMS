go = int(input())
for t in range(go):
    x = list(input().lower())
    n1 = 0
    lis =['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    for y in lis:
        if y in x:
            n1 += 1
    if n1 >= 26:
        print('frase completa')
    elif n1 >= 13:
        print('frase quase completa')
    else:
        print('frase mal elaborada')
