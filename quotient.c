#include <stdio.h>
#include <stdlib.h>

int findQ(int a, int b)
{
    if (b == 0) {
        printf("Нельзя делить на ноль!\n");
        return 0;
    }
    
    int q = 0;
    while ((q + 1) * abs(b) <= abs(a)) {
        q++;
    }
    
    // Определяем знак
    if ((a < 0 && b > 0) || (a > 0 && b < 0)) {
        return -q;
    }
    return q;
}

int main()
{
    int a, b;
    
    printf("Введите два целых числа a и b: \n");
    scanf("%d %d", &a, &b);
    
    int q = findQ(a, b);
    if (b != 0) {
        printf("Неполное частное от деления: %d\n", q);
    }
    return 0;
}
