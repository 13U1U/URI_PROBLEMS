x = float(input())

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

m1 = x//1
x = x-(m1)

m2 = x//0.50
x = x-(m2*0.50)

m3 = x//0.25
x = x-(m3*0.25)

m4 = x//0.10
x = x-(m4*0.10)

m5 = x//0.05
x = x-(m5*0.05)

m6 = x

print("NOTAS:")
print(f"{n1} nota(s) de R$ 100,00")
print(f"{n2} nota(s) de R$ 50,00")
print(f"{n3} nota(s) de R$ 20,00")
print(f"{n4} nota(s) de R$ 10,00")
print(f"{n5} nota(s) de R$ 5,00")
print(f"{n6} nota(s) de R$ 2,00")

print("MOEDAS:")
print(f"{m1} moeda(s) de R$ 1.00")
print(f"{m2} moeda(s) de R$ 0.50")
print(f"{m3} moeda(s) de R$ 0.25")
print(f"{m4} moeda(s) de R$ 0.10")
print(f"{m5} moeda(s) de R$ 0.05")
print(f"{m6} moeda(s) de R$ 0.01")
