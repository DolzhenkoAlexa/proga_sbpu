#include <stdio.h>
#include <string.h>

// Функция проверки подстроки
int checkSub(char str[], char substr[]) 
{
    int result = 0;
    for (int i = 0; str[i] != '\0'; i++) { // Проходим по каждому элементу str
        int found = 1; // Создаем "флаг", по которому будем определять надо ли прибавлять 1 к result
        for (int j = 0; substr[j] != '\0'; j++) { // Проходим по каждому элементу substr
            if (str[i+j] != substr[j]) { // Если элементы не совпадают, то обнуляем флаг
                found = 0;
                break;
            }
        }
        if (found == 1) {
            result++;
        }
    }
    return result;
}


int main(void) 
{
    printf("Введите строку\n");
    char str[512];
    fgets(str, sizeof(str), stdin);
    str[strlen(str) - 1] = '\0'; // удаляем последний элемент (по индексу), который в fgets является \n

    printf("Введите подстроку\n");
    char substr[512];
    fgets(substr, sizeof(substr), stdin);
    substr[strlen(substr) - 1] = '\0';

    int result = checkSub(str, substr);
    printf("%d", result);

    return 0;
}
