a = int(input("Digite um número: "))
b = int(input("Digite um número: "))
operacao = (input("Digite um caractere matemático (+ , -, *, /): "))

if operacao == "+":
    resultado = a + b
elif operacao == "-":
    resultado = a - b
elif operacao == "*":
    resultado = a * b
elif operacao == "/":
    if b != 0:
        resultado = a / b
    else:
        resultado = "erro: divisão por zero!"
else:
        resultado = "Operação invalida!"

print("Resultado:", resultado)
