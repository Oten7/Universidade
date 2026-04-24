nome_completo = input("Digite o nome completo: ")
idade = int(input("Digite sua idade: "))
salario = float(input("Digite seu salario: "))
codigo = int(input("Digite seu codigo: "))

name = "RELATORIO"

print(f"{'RELATÓRIO':^30}")
print("=" * 30)
print()
print(f"Nome completo: {nome_completo}")
print(f"{'Idade: ' :<15} {idade} anos")
print(f"{'Salario: ' :<15} {salario:.2f}")
print(f"{'Codigo ' :<15} {codigo:06d}")
print()
print("=" * 30)