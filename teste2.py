def fibonacci(n):
    fib =[0, 1]
    while fib[-1] < n:
        fib.append(fib[-1] + fib[-2])
    return fib

def verifica_fibonacci(numero):
    seq = fibonacci(numero)
    if numero in seq:
        return f"O número {numero} pertence à sequência."
    else:
        return f"O número {numero} não pertence à sequência."
    
# Pedir o número ao usuario 
numero = int(input("Digite um número para verificar se pertence a sequência de Fibonacci: "))

print(verifica_fibonacci(numero))