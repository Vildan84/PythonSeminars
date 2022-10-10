import random

board = {1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 8: 8, 9: 9}


def print_board(b):
    print("_____________")
    print(f"| {b[1]} | {b[2]} | {b[3]} |")
    print(f"| {b[4]} | {b[5]} | {b[6]} |")
    print(f"| {b[7]} | {b[8]} | {b[9]} |")
    print("-------------")


def check_result(d):
    check = ((1, 2, 3), (4, 5, 6), (7, 8, 9), (1, 4, 7), (2, 5, 8), (3, 6, 9), (1, 5, 9), (3, 5, 7))
    for e in check:
        if d[e[0]] == d[e[1]] == d[e[2]]:
            return True
    return False


def game_zero_x():
    start = random.randint(1, 2)
    player_x = 1
    player_zero = 1
    if start == 1:
        player_zero = 2
        print("Начинает игрок номер 1")
    else:
        player_x = 2
        print("Начинает игрок номер 2")

    count = 0
    print_board(board)
    while count < 7:
        if player_x == 1:
            enter = input("Игрок X выберете ячейку:  ")
            if enter.isdigit():
                number = int(enter)
            else:
                print("Введена буква!!!")
                continue
            if number > 9 or number < 0 or board[number] == "X" or board[number] == "O":
                print("Ячейка занята или число вне диапазона")
                continue
            board[number] = "X"
            print_board(board)
            count += 1
            if count >= 5:
                if check_result(board):
                    print("Победил игрок X !!!")
                    break
            player_x, player_zero = player_zero, player_x
        else:
            enter = input("Игрок O выберете ячейку:  ")
            if enter.isdigit():
                number = int(enter)
            else:
                print("Введена буква!!!")
                continue
            if number > 9 or number < 0 or board[number] == "X" or board[number] == "O":
                print("Ячейка занята или число вне диапазона")
                continue
            board[number] = "O"
            print_board(board)
            count += 1
            if count >= 5:
                if check_result(board):
                    print("Победил игрок Zero !!!")
                    break
            player_x, player_zero = player_zero, player_x
    else:
        print("Ничья!!!")


game_zero_x()




