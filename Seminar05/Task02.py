import random


def candy_game(n):
    start = random.randint(1, 2)
    player_one = 1
    player_two = 1
    if start == 1:
        player_two = 2
        print("Начинает игрок номер 1")
    else:
        player_one = 2
        print("Начинает игрок номер 2")
    remain = n
    while n > 0:
        if player_one == 1:
            enter = input("Сколько конфет хотите взять игрок 1: ")
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
            player_one, player_two = player_two, player_one
        else:
            enter = input("Сколько конфет хотите взять игрок 2: ")
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
            player_one, player_two = player_two, player_one

        print(f"Осталось {remain} конфет(а)")


print(candy_game(100))




