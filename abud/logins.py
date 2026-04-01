print("======CADASTRO DE LOGIN======")
usuario_cadastrado = input("Digite seu usuario: ")
senha_cadastrado = input("Digite sua senha: ")

print("===USUARIO CADASTRADO===")

print("===LOGIN===")
max_tentaivas = 3
tentativas = 0
acesso = False

while tentativas < max_tentaivas:
    usuario = input("Digite seu usuario: ")
    senha = input("Digite sua senha: ")
    if senha == usuario_cadastrado:
        acesso = True
        break
    else:
        tentativas += 1
        restantes = max_tentaivas - tentativas
        if restantes > 0:
            print(f"login incorreto! Tentativas Restantes: {restantes} ")
if acesso:
    print("login com sucesso!")
else:
    print("login invalido!")