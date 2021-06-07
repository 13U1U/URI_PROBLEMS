n1, n2, n3, n4 = map(float, input().split())

n1 = n1 * 2
n2 = n2 * 3
n3 = n3 * 4

media = float((n1+n2+n3+n4)/10)

if media >= 7.0:
    print(f"Media: {media:.1f}")
    print('Aluno aprovado.')
else:
    if media >= 5.0:
        print(f"Media: {media:.1f}")
        print('Aluno em exame.')
        x = float(input())
        exa = (x+media)/2
        print(f"Nota do exame: {x:.1f}")
        if exa >= 5.0:
            print('Aluno aprovado.')
        else:
            print('Aluno reprovado.')
        print(f"Media final: {exa:.1f}")

    else:
        print(f"Media: {media:.1f}")
        print('Aluno reprovado.')
#0.001 / 03.06.2021 / 2
