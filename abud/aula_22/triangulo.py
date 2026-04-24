a = float(input("digite o primeiro lado: "))
b = float(input("digite o segundo lado: "))
c = float(input("digite o pterceiro lado: "))

if a + b > c and a + c > b and b + c > a:
    print("os lados formam um trinagulo!")

    if a == b == c:
        tipo = "Equilátero"
    elif a == b or a == c  or b == c:
        tipo = "Isósceles"
    else:
        tipo = "Escalåeno"
    
    lado = sorted([a, b, c])
    l1, l2, l3 = lado[0], lado[1], lado[2]

    if l1**2 + l2**2 == 2:
        print(f"Classificacao: Triangulo Retangulo e {tipo}")
    else:
        print(f"Classificacao: {tipo}")
else:
    if a + b == c or a + c == b or b + c == a:
        print("Nao forma triangulo, mas forma um segmento degenerado")
    else:
        print("Nao forma um triangulo")
