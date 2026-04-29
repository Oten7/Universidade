renda = float(input("Qual sua renda mmensal: "))
idade = int(input("Qual sua idade?: "))
nome_limpo = int(input("Possui nome limpo? 01-Sim 02-Nao: "))

aprovado = ((renda >= 2500 and idade >= 21) or (renda >= 10000)) and nome_limpo == 1

if aprovado:
    print("Seu emprestimo foi aprovado")
else:
    print("Seu emprestimo foi reprovado")

