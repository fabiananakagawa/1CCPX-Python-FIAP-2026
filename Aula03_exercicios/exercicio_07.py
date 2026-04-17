ano_nascimento = int(input("Digite seu ano de nascimento: "))

ano_atual = 2026

idade = ano_atual - ano_nascimento

if idade < 16:
    print("Voto proibido esse ano!")
elif idade >= 16 and idade < 18 or idade > 70:
    print("Voto opcional para esse ano!")
else:
    print("Voto obrigatório esse ano!")
