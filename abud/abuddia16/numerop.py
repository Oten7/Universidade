n1 = int(input("digite um numero"))
primo = True
if n1 < 2:
    primo = False

else:
    for i in range(2, n1):
        if n1 % i == 0:
            primo = False
            break

if primo:
    print("numero primo")
else:
    print("numero não é primo")