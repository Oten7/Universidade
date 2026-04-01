import random

print("===Jogo da Adivinhação===")
print("Escolha o nível:")
print("1 - Fácil (1 a 10)")
print("2 - Médio (1 a 50)")
print("3 - Difícil (1 a 100)")

opcao = input("Opção: ")

if opcao == "1":
    nivel = "Fácil"
    minimo = 1
    maximo = 10
elif opcao == "2":
    nivel = "Médio"
    minimo = 1
    maximo = 50
else:
    nivel = "Difícil"
    minimo = 1
    maximo = 100

numero_secreto = random.randint(minimo, maximo)
tentativas = 0

print(f"(Nível {nivel}): adivinhe o número entre {minimo} e {maximo}")

while True:
    chute = int(input("Chute: "))
    tentativas += 1

    if chute == numero_secreto:
        print(f"Acertou em {tentativas} tentativas!")
        break
    elif chute < numero_secreto:
        print("É maior!")
    else:
        print("É menor!")