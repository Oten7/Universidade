primeira_nota = float(input("digite sua primeira nota"))
segunda_nota = float(input("digite sua segunda nota"))
terceira_nota = float(input("digite sua terceira nota"))

media = (primeira_nota + segunda_nota + terceira_nota) / 3

print(f"Sua média é: {media:.2f}")
if media >= 7:
    print("aprovado")
elif media >= 5:
    print("recupeção")
else:
    print("reprovado")