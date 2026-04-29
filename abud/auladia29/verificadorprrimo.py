numero = int(input("Digite um número inteiro: "))
primo = True

if numero < 2:
    primo = False
else:
    for i in range(2, numero):
        if numero % i == 0:
            primo = False
            break

if primo:
    print(f"{numero} é primo.")
else:
    print(f"{numero} não é primo.")