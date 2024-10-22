texto = input("Digite uma sting: ")

# Para armazenar o resultado
texto_invertido = ""

#Inverter usando um loop
for i in range(len(texto) - 1,-1,-1 ):
    texto_invertido += texto[i]

print("String invertida:", texto_invertido)