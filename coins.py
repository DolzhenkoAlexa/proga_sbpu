num = int(input())

for c10 in range(num // 10, -1, -1):
    rem1 = num - c10 * 10
    for c9 in range(rem1 // 9, -1, -1):
        rem2 = rem1 - c9 * 9
        for c8 in range(rem2 // 8, -1, -1):
            rem3 = rem2 - c8 * 8
            if rem3 == 0:
                print('Колво 10: ', c10)
                print('Колво 9: ', c9)
                print('Колво 8: ', c8)
                exit()

print("-42!")
