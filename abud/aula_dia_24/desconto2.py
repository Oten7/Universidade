valor_total = float(input("digite o valor total da compra: "))
vip = input("é cliente vip? (sim/nao): ") == "sim"
cupom = input("tem cupom de desconto? (sim/nao): ") == "sim"

if valor_total < 100:
    print("Desconto nao aplicado: Valor abaixo de 100")
elif (vip and valor_total > 500) or (cupom and valor_total):
    desconto = valor_total * 0.20
    valor_final = valor_total - desconto
    print(f"Super desconto aplicado: {desconto:.2f}")
    print(f"Valor finall: R$ {valor_final:.2f}")
else:
    print("Desconto nao aplicado")