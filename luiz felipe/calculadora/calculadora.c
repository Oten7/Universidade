#include <stdio.h>

int main() {
  float num1,num2, resultado;
  char operador;
  int resto;

printf("digite seu primeiro numero: ");
scanf("%f", &num1);

printf("digite o segundo numero: ");
scanf("%f", &num2);

printf("digite o operador (+,-,*,/.%): ");
scanf(" %c", &operador);

if (operador == '+') {
    printf("Resultado %2.f", num1 + num2);
} else if (operador == '-') {
    printf("Resultado %2.f", num1 - num2);
} else if (operador == '*') {
    printf("Resultado %2.f", num1 * num2);
} else if (operador == '/') {
    if (num2 == 0) {
        printf("Erro: nao é possivel dividir por 0");
    } 
    else {
    resultado = num1 / num2;
    printf("Resultado %2.f", resultado);
    }
}
else if (operador == '%') {
    if (num2 == 0) {
        printf("Erro: nao é possivel dividir por 0");
    } else {
        int n1 = (int)num1;
        int n2 = (int)num2;
        resto = n1 % n2;
        printf("Resultado %d", resto);
    }
} else {
    printf("operecao invalida");
}
return 0;
}
