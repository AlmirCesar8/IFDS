n1 = float(input("Insira sua primeira nota: "))
n2 = float(input("Insira sua segunda nota: "))
m = (n1 + n2)/2
print("Sua média foi:", m)
if m<3:
    print("Reprovado!!")
elif m<6:
    print("Recuperação!!")
else:
    print("Aprovado!!")