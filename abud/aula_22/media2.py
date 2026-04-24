prova = float(input("Nota da prova (0 a 10): "))
trabalho = float(input("Nota do trabalho (0 a 10): "))
frequencia = float(input("Frequência (0 a 100%): "))

media = (prova * 0.7 + trabalho * 0.3)

# Situação
if media >= 7 and frequencia >= 75:
    situacao = "Aprovado direto"
elif (5 <= media <= 6.9) or (60 <= frequencia <= 74):
    situacao = "Recuperação"
else:
    situacao = "Reprovado"

# Observação
if media >= 8 and frequencia >= 90:
    observacao = "Aprovado com mérito"
elif media < 5 and trabalho >= 8:
    observacao = "Reprovado com bom desempenho em trabalho"
else:
    observacao = "—"

print(f"\n--- Resultado ---")
print("=" * 30)
print()
print(f"Média      : {media:.2f}")
print(f"Situação   : {situacao}")
print(f"Observação : {observacao}")
print()
print("=" * 30)