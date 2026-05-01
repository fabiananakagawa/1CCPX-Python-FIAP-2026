# OPERADORES DE ATRIBUIÇÃO
num = 15
print(num)

num = num + 2
print(num) #17

num += 2
print(num)

#OPERADORES RELACIONAIS

print() #pular linha
print(6 == 3) #Booleano

idade = 20
print(idade == 20)

maior_idade = idade >= 18
print(maior_idade) #guarda true (resultado da operação)

#OPERADORES LOGICOS
#logica E (END)
print()

verificar_email = True
verificar_senha = False

login = verificar_email and verificar_senha
print(login)

if not login:
    print("Po cara acerta ai...")

    print()
    #NOTAS...

nota_final = 3

if nota_final < 4:
    print("Reprovado")
else:
    if nota_final < 6:
        print("Recuperação")
    else:
        print("Aprovado")

print("FIM")

#outro jeito de fazer
if nota_final < 4:
    print("Reprovado")
elif nota_final < 6:
    print("Recuperação")
else:
    print("Aprovado")

print("FIM")
