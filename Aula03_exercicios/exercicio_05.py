a = int(input("Digite um número: "))
b = int(input("Digite outro número: "))

if a % b == 0 or b % a == 0:
    print("São multiplos!")
else:
    print("Não são multiplos!")