lista_frutas = ["morango", "maça", "uva"]

# lista_frutas[0] = "morango"
# lista_frutas[1] = "maça"
# lista_frutas[2] = "uva"
print(lista_frutas[1])

lista_frutas.append("melancia")
print(lista_frutas[3])

for i in range(len(lista_frutas)):
    print(lista_frutas[i])

    print()

    for fruta in lista_frutas:
        print(fruta)


