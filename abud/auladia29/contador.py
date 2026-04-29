numero_positivo = int(input("digite um valor inteiro e positivo: "))

contador = 1

if numero_positivo > 50:
        print(f"{numero_positivo} é maior que 50")
else:
    while contador <= numero_positivo:
        print(contador)
        contador += 1
