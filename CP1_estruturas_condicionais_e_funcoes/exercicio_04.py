def calcular_horas_extras(salario, horas):
    return salario * 0.015 * horas

def calcular_faltas(salario, faltas):
    return salario * 0.02 * faltas

def calcular_bonus(cargo, bonus):
    if bonus == "s":
        if cargo == 1:
            return 1000
        elif cargo == 2:
            return 500
        elif cargo == 3:
            return 300
        elif cargo == 4:
            return 100
    return 0


nome = input("Nome: ")
cargo = int(input("Cargo: "))
salario = float(input("Salário base: "))
horas = float(input("Horas extras: "))
faltas = int(input("Faltas: "))
bonus = input("Recebeu bônus? (s/n): ")

extra = calcular_horas_extras(salario, horas)
desconto = calcular_faltas(salario, faltas)
valor_bonus = calcular_bonus(cargo, bonus)

bruto = salario + extra + valor_bonus
final = bruto - desconto

print(f"Funcionário: {nome}")
print(f"Salário bruto: R${bruto:.2f}")
print(f"Acréscimos: R${extra + valor_bonus:.2f}")
print(f"Descontos: R${desconto:.2f}")
print(f"Salário final: R${final:.2f}")