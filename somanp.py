soma = 0

for i in range(1, 11):
    numero = int(input("Digite um número: "))

    if numero % 2 == 0:
        soma = soma + numero

print("A soma dos números pares é:", soma)