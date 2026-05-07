# Preparo do ambiente:
import pandas as pd
import matplotlib.pyplot as plt

# Conjunto de dados:
vendas_camiseta = pd.Series([2, 4, 3, 4, 5, 2, 4, 11, 4, 2])
print(vendas_camiseta)

# Análise Exploratória de dados: Etapa de Estatística Descritiva
# Medida de tendencia central
# 1) Média: esperança matemática
print(vendas_camiseta.mean())

# 2) Mediana: Elemento central, separa o conjunto de dados ao meio, 50% dos dados ficam abaixo e 50% acima
print(vendas_camiseta.median())

# 3) Moda: Elemento com maior frequência absoluta
print(vendas_camiseta.mode())

# Medidas de dispersão:
# 1) maximo
print(vendas_camiseta.max())

# 2) Mínimo
print(vendas_camiseta.min())

# 3) Amplitude
print(vendas_camiseta.max() - vendas_camiseta.min())

# 4) Variância Amostral --> Não é interpretável, pois a grandeza da variável é alterada
print(vendas_camiseta.var())

# 5) Desvio padrão Amostral
print(vendas_camiseta.std())

# 6) Coeficiênte de Varição Amostral:
print(vendas_camiseta.std() / vendas_camiseta.mean() * 100)

# Medidas Separatrizes:
# Quartis
print(vendas_camiseta.quantile([0.25, 0.50, 0.75]))

# Analise grafica: Boxplot
plt.boxplot(vendas_camiseta,
            patch_artist=True,
            boxprops=dict(facecolor="red"))
plt.show()

print(vendas_camiseta.describe())