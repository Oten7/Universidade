soma = 0

for i in range(10):
    numero = int(input(f"digite o {i + 1} numero: "))
    if numero % 2 == 0:
        soma += numero

print(f"A somma dos pares é: {soma}")
