# Если первая строка (s1) больше второй (s2) ЛЕКСИКОГРАФИЧЕСКОМ порядке, то вернется True. Return было бы s1 > s2
# Но задание - обратный лексикографический порядок.
# Было s1 > s2 в лексикографическом порядке. Стало s2 > s1 в обратном
# То есть в новом раскладе True  - если s1 < s2. False - если s1 > s2 или s1 == s2
def reverse_lexicographic(s1, s2):
    return s2 > s1

test_result = reverse_lexicographic("aaa", "bbb")
print("Лексикографический порядок: 'aaa' > 'bbb' =", "aaa" > "bbb")  # Выведет False
print(f"Обратный порядок: 'aaa' > 'bbb' = {test_result}")  # Выведет True

# Интерактивный ввод
s1 = input('Введите первую строку: ')
s2 = input('Введите вторую строку: ')
result = reverse_lexicographic(s1, s2)
print(result)

