estado = int(input("Digite o código do estado de origem da carga do seu caminhão (1 a 5): "))
peso = float(input("Digite o peso em toneladas da sua carga: "))
codigo = int(input("Digite o código da carga (10 a 40): "))

kg = peso * 1000

if codigo >= 10 and codigo <= 20:
    preco = 100
elif codigo >= 21 and codigo <= 30:
    preco = 250
elif codigo >= 31 and codigo <= 40:
    preco = 340

preco_total = preco * kg

if estado == 1:
    imposto = 0.35
elif estado == 2:
    imposto = 0.25
elif estado == 3:
    imposto = 0.15
elif estado == 4:
    imposto = 0.05
else:
    imposto = 0

total_imposto = preco_total * imposto
total = total_imposto + preco_total

print(f'O peso do caminhão é de: {kg:,.0f} kg'.replace(",", "."))
print(f'O preço da carga é de: R$ {preco_total:,.2f}'.replace(",", "X").replace(".", ",").replace("X", "."))
print(f'O valor do imposto de acordo com o seu estado é de: R$ {total_imposto:,.2f}'.replace(",", "X").replace(".", ",").replace("X", "."))
print(f"O valor total transportado pelo caminhão é de: R$ {total:,.2f}".replace(",", "X").replace(".", ",").replace("X", "."))