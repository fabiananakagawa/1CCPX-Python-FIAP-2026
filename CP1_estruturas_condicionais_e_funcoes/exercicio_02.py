a = int(input("Dígite o primeiro lado: "))
b = int(input("Dígite o segundo lado: "))
c = int(input("Dígite o terceiro lado: "))

lados = sorted([a, b, c], reverse=True)

A, B, C = lados

if A >= B + C:
    print("NAO FORMA TRIANGULO")

else:

    if A**2 == B**2 + C**2:
        print("TRIANGULO RETANGULO")

    elif A**2 > B**2 + C**2:
        print("TRIANGULO OBTUSANGULO")

    elif A**2 < B**2 + C**2:
        print("TRIANGULO ACUTANGULO")

    if A == B == C:
        print("TRIANGULO EQUILATERO")

    elif A == B or A == C or B == C:
        print("TRIANGULO ISOSCELES")