import json

# Carrega os dados do arquivo json
with open("dados.json") as meu__json:
    dados = json.load(meu__json)

# Considerar penas os dias com faturamento
faturamento = [dia['valor'] for dia in dados if dia['valor'] > 0]

# Menor e o maior valor
menor_faturamento = min(faturamento)
maior_faturamento = max(faturamento)

# Média mensal
media_mensal = sum(faturamento)/ len(faturamento)

# Dias com faturamento acima da média
dias_acima_media = sum(1 for valor in faturamento if valor > media_mensal)

# Resultados:
print(f"Menor faturamento: R$ {menor_faturamento:.2f}")
print(f"Maior faturamneto: R$ {maior_faturamento:.2f}")
print(f"Dias com faturamento acima da média: {dias_acima_media}")

# Resultados no console:
# Menor faturamento: R$ 373.78
# Maior faturamneto: R$ 48924.24
# Dias com faturamento acima da média: 10