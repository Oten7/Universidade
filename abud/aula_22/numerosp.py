numero = int(input("Digite um número inteiro: "))
 

if numero > 0:
    print("O número é positivo.")
elif numero < 0:
    print("O número é negativo.")
else:
    print("O número é zero.")
 

if numero % 2 == 0:
    print("O número é par.")
else:
    print("O número é ímpar.")
 

if numero != 0:
    if numero % 3 == 0:
        print("É múltiplo de 3.")
    if numero % 5 == 0:
        print("É múltiplo de 5.")
    if numero % 7 == 0:
        print("É múltiplo de 7.")
 

if numero % 3 == 0 and numero % 5 == 0 and numero % 7 != 0:
    print("FizzBuzz especial!")
elif numero % 3 == 0 and numero % 5 == 0 and numero % 7 == 0:
    print("Número raro!")
 

if numero > 1:
    e_primo = True
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            e_primo = False
            
    if e_primo:
        print("O número é primo.")
 

if numero < 0 and numero % 2 == 0:
    print("Número negativo par problemático!")