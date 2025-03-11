def sequencia_fibonacci(limite):
    sequencia = [0, 1]
    while sequencia[-1] < limite:
        sequencia.append(sequencia[-1] + sequencia[-2])
    return sequencia

def eh_numero_fibonacci(n):
    sequencia = sequencia_fibonacci(n)
    return n in sequencia

# Número a ser verificado
numero = 34

# Verificando se o número pertence à sequência
if eh_numero_fibonacci(numero):
    print(f"O número {numero} pertence à sequência de Fibonacci.")
else:
    print(f"O número {numero} não pertence à sequência de Fibonacci.")

# Saída:
# O número 34 pertence à sequência de Fibonacci