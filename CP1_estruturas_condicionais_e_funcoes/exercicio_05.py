def pode_aprovar(idade, renda, valor):
    if idade > 18 and valor <= renda * 20:
        return True
    return False

def definir_taxa(parcelas):
    if parcelas <= 6:
        return 0.05
    elif parcelas <= 12:
        return 0.08
    else:
        return 0.10

def calcular_parcela(valor, taxa, n):
    parcela = valor * (taxa * (1 + taxa) ** n) / ((1 + taxa) ** n - 1)
    return parcela

nome = input("Nome: ")
idade = int(input("Idade: "))
renda = float(input("Renda mensal: "))
valor = float(input("Valor empréstimo: "))
parcelas = int(input("Parcelas: "))

if pode_aprovar(idade, renda, valor):

    taxa = definir_taxa(parcelas)

    parcela = calcular_parcela(valor, taxa, parcelas)

    total = parcela * parcelas
    juros = total - valor

    print("EMPRÉSTIMO APROVADO")
    print(f"Cliente: {nome}")
    print(f"Valor financiado: R${valor:.2f}")
    print(f"Taxa: {taxa*100:.0f}%")
    print(f"Parcela: R${parcela:.2f}")
    print(f"Total pago: R${total:.2f}")
    print(f"Juros pagos: R${juros:.2f}")

else:
    print("EMPRÉSTIMO NEGADO")