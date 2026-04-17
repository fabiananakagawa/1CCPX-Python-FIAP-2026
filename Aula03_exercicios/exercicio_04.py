nota_1 = float(input("Digite sua primeira nota: "))
nota_2 = float(input("Digite sua segunda nota: "))
nota_3 = float(input("Digite sua terceira nota: "))
nota_4 = float(input("Digite sua quarta nota: "))

soma = nota_1 + nota_2 + nota_3 + nota_4
media = soma/4
print(media)

if media >= 7:
    print("Aprovado!")
elif media >= 5 and media < 7:
    print("Em recuperação!")
else:
    print("Reprovado!")