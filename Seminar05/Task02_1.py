import random


def candy_game(n):
    start = random.randint(1, 2)
    player = 1
    bot = 1
    if start == 1:
        bot = 2
        print("Начинает игрок")
    else:
        player = 2
        print("Начинает  Бот")
    remain = n
    while n > 0:
        if player == 1:
            enter = input("Сколько конфет хотите взять?: ")
            if enter.isdigit():
                number = int(enter)
            else:
                print("Ошибка ввода, повторите попытку!")
                continue
            if number > 28 or number <= 0 or number > remain:
                print("Вы взяли неверное количество конфет, повторите попытку!")
                continue
            remain -= number
            if remain == 0:
                print("Поздравляю Вы победили!!!!!")
                break
            player, bot = bot, player
        else:
            print("Ходит Бот!")
            if remain < 29:
                number = remain
            else:
                number = remain % 28 - 1
            if number == 0:
                number = random.randint(1, 28)
            print(f"Бот взял {number} конфет(у)")
            remain -= number
            if remain == 0:
                print("Бот победил!!!!!")
                break
            player, bot = bot, player

        print(f"Осталось {remain} конфет(а)")


print(candy_game(200))