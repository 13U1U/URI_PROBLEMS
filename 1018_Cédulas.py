x = int(input())

n1 = x//100
x = x-(n1*100)

n2 = x//50
x = x-(n1*50)

n3 = x//20
x = x-(n3*20)

n4 = x//10
x = x-(n4*10)

n5 = x//5
x = x-(n5*5)

n6 = x//2
x = x-(n6*2)

print(f"{x}")
print(f"{n1} nota(s) de R$ 100,00")
print(f"{n2} nota(s) de R$ 50,00")
print(f"{n3} nota(s) de R$ 20,00")
print(f"{n4} nota(s) de R$ 10,00")
print(f"{n5} nota(s) de R$ 5,00")
print(f"{n6} nota(s) de R$ 2,00")
print(f"{x} nota(s) de R$ 1,00")
#0.059 / 31.05.2021 / 1
