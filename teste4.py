faturamento = {
  "SP": 67836.43,
  "RJ": 36678.66,
  "MG": 29229.88,
  "ES": 27165.48,
  "Outros": 19849.53
}

# Faturamento total
total_faturamento = sum(faturamento.values())

# Percentual de cada estado
percentuais = {estado : (valor / total_faturamento) * 100 for estado, valor in faturamento.items()} 

# Resultados
print("Percentual de representação de cada estado: ")
for estado, percentual in percentuais.items():
    print(f"{estado}: {percentual:.2f}%")

# Resultados no console:
# Menor faturamento: R$ 373.78
# Maior faturamneto: R$ 48924.24
# Dias com faturamento acima da média: 10