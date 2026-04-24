valor = float(input("digite o valor: "))
cliente = input("tipo de cliente (comum/vip/funcionario): ").strip().lower()
 

if valor >= 1000:
    desconto = 20
elif valor >= 500:
    desconto = 10
else:
    desconto = 5
 

if cliente == "funcionario" and valor < 200:
    desconto = 0
    print("Sem desconto para funcionário com compra abaixo de R$ 200,00.")
else:

    if cliente == "vip":
        desconto += 5
    elif cliente == "funcionario":
        desconto += 10
 

    if cliente == "vip" and valor >= 2000:
        desconto = 40
 

    if desconto > 50:
        desconto = 50
 
valor_final = valor * (1 - desconto / 100)
 
print(f"Desconto aplicado: {desconto}%")
print(f"Valor final: R$ {valor_final:.2f}")
