board = list(range(1, 10))
wins_coord = [(1, 2, 3), (4, 5, 6), (7, 8, 9), (1, 4, 7), (2, 5, 8), (3, 6, 9), (1, 5, 9), (3, 5, 7)]


def draw_board():  # функция выводит игровое поле по строкам
    print('---------')
    for i in range(3):
        print('|', board[0 + i * 3], board[1 + i * 3], board[2 + i * 3], '|')
    print('---------')


"""1.Проверка допустимости чисел в игровом поле"""


def take_input(player_token):
    while True:
        value = input("Куда поставить:" + player_token + "? ")
        if not (value in '123456789'):
            print("Ошибачный ввод. Повторите")
            continue
        value = int(value)
        if str(board[value - 1]) in 'XO':
            print("Эта клетка уже занята")
            continue
        board[value - 1] = player_token
        break


"""Проверка на выигрыша"""


def check_win():
    for ech in wins_coord:
        if (board[ech[0] - 1]) == (board[ech[1] - 1]) == (board[ech[2] - 1]):
            return board[ech[1] - 1]
    else:
        return False


def main():
    counter = 0
    while True:
        draw_board()
        if counter % 2 == 0:
            take_input('X')
        else:
            take_input("O")
        if counter > 3:
            winner = check_win()
            if winner:
                draw_board()
                print(f'Игрок {winner} выиграл')
                break
        counter += 1
        if counter > 8:
            draw_board()
            print("Ничья")
            break


if __name__ == "__main__":
    main()