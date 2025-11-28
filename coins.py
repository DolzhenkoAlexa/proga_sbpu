sum = int(input("Введите сумму,которую нужно разменять: "))
coins = []

for i in range(3):
    coin = int(input(f"Введите номинал монеты {i+1}: ")) # Введена абстрактность
    coins.append(coin)

coins.sort(reverse=True) # Cортируем по убыванию
coin_val1, coin_val2, coin_val3 = coins[0], coins[1], coins[2]

for amount1 in range(sum // coin_val1, -1, -1):
    remaining  = sum - amount1 * coin_val1
    for amount2 in range(remaining  // coin_val2, -1, -1):
        remaining  = remaining  - amount2 * coin_val2
        if coin_val3 != 0 and remaining % coin_val3 == 0: # Третий цикл убран
            amount3 = remaining  // coin_val3
            print("Количество монет номинала", coin_val1, ":", amount1)
            print("Количество монет номинала", coin_val2, ":", amount2)
            print("Количество монет номинала", coin_val3, ":", amount3)
            exit()

print("-42!")
