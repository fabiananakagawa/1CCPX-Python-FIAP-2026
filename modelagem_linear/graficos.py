# preparando o ambiente
from collections import Counter
import matplotlib.pyplot as plt
from numpy.ma.core import argsort

# graficos para variaveis qualitativas:
# grafico de setores:
# 1) conjunto de dados:
dados1 = ['sim']*20 + ['não']*45
print(dados1)

respostas1 = Counter(dados1)
print(respostas1)

#construção grafica:
plt.pie(list(respostas1.values()),
            labels=list(respostas1.keys()),
            autopct='%1.2f%%',
            colors=['blue', 'red'])

plt.title('Resultado da pesquisa aplicada pelo Mc donalds - 2026')
plt.legend(list(respostas1.keys()),
            loc='upper right')
plt.show()