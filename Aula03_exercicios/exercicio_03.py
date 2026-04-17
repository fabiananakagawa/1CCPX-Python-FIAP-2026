num_1 = int(input("Digite um número: "))
num_2 = int(input("Digite outro número: "))

if num_1 > num_2:
    print(f"{num_1} é o maior!")
elif num_1 < num_2:
    print(f"{num_2} é o maior!")
else:
    num_1 = num_2
    print("Os dois números são iguais!")