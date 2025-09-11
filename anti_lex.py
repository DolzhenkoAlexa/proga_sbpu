str1 = input("Введите первую строку: ")
str2 = input("Введите вторую строку: ")

def anti_lex(str1, str2):
    min_len = min(len(str1), len(str2))

    if len(str1) != len(str2):
        if len(str1) < len(str2):
            return -1
        else:
            return 1

    for i in range(min_len):
        if str1[i] != str2[i]:
            if str1[i] > str2[i]:
                return -1
            else:
                return 1
    return 0

result = anti_lex(str1, str2)

if result == -1:
    print(f"'{str1}' идет перед '{str2}'")
elif result == 1:
    print(f"'{str2}' идет перед '{str1}'")
else:
    print("Строки одинаковы")