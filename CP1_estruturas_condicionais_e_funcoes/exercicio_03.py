cp1 = float(input("Digite a nota CP1: "))
cp2 = float(input("Digite a nota CP2: "))
cp3 = float(input("Digite a nota CP3: "))
sp1 = float(input("Digite a nota Sprint 1: "))
sp2 = float(input("Digite a nota Sprint 2: "))
gs = float(input("Digite a nota GS: "))

# Descobrir menor checkpoint sem usar min()
menor = cp1

if cp2 < menor:
    menor = cp2

if cp3 < menor:
    menor = cp3

# Soma checkpoints tirando a menor
soma_cp = cp1 + cp2 + cp3 - menor

# Média checkpoints + sprints
media_base = (soma_cp + sp1 + sp2) / 4

# Média semestre
media = (media_base * 0.4) + (gs * 0.6)

# Média com peso
media_peso = media * 0.4

print(f"Média semestre: {media:.1f}")
print(f"Média com peso: {media_peso:.1f}")