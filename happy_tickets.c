#include <stdio.h>

int main() 
{
    int count = 0;
    int neededSum;
    printf("Введите 'заданную' сумму: \n");
    scanf("%d", &neededSum);
    
    // Генерация всех шестизначных билетиков циклами, учитывая варианты с нулями, типа 000000
    for (int a = 0; a < 10; a++) {
        for (int b = 0; b < 10; b++) {
            for (int c = 0; c < 10; c++) {
                for (int d = 0; d < 10; d++) {
                    for (int e = 0; e < 10; e++) {
                        for (int f = 0; f < 10; f++) {
                            int leftPart = a + b + c;
                            int rightPart = d + e + f;
                            
                            if (leftPart == rightPart && leftPart == neededSum) {
                                count++;
                            }
                        }
                    }
                }
            }
        }
    }
    
    // Вывод числа билета с нужной суммой первых (или последних, они равны) чисел
    printf("%d", count); 
    return 0;
}
