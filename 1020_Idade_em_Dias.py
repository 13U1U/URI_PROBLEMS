x = int(input())


ano = x // 365
x = x - ano*365


mes = x // 30
x = x - mes*30


dia = x
print(f"{ano} ano(s)")
print(f"{mes} mes(es)")
print(f"{dia} dia(s)")
#0.177 / 31.05.2021 / 4
