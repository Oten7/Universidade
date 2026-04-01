#include <stdio.h>
int main () {
float nota1,nota2,media;
int frequencia;

printf("digite sua primeira nota (0 a 10): ");
scanf("%f", &nota1);
printf("digite sua segunda nota (0 a 10): ");
scanf("%f", &nota2);
printf("digite sua frequencia (0 a 100%)");
scanf("%d", &frequencia);
if (nota1 < 0 || nota1 > 10 || nota2 < 0 || nota2 > 10 || frequencia < 0 || frequencia > 100) {
    printf("valores invalidos!!");
} else {
    media = (nota1 + nota2) /2;
 
    if (media >= 7 && frequencia >= 75) {
        printf("Media  %2.f\n", media);
        printf("Frequencia %d%%\n", frequencia);
        printf("Situcao: Aprovado");
    }
    else if (media >= 5 && frequencia >= 75) {
        printf("Media  %2.f\n", media);
        printf("Frequencia %d%%\n", frequencia);
        printf("Situcao: Recuperecao");
    } 
    else {
         printf("Media  %2.f\n", media);
         printf("Frequencia %d%%\n", frequencia);
         printf("Situcao: Reprovado");
    }
}
}





