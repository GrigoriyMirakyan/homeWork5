# Создайте программу для игры в ""Крестики-нолики"".


game_field = list(range(1, 10))


def draw_field(game_field):
    print("-" * 13)
    for i in range(3):
        print("|", game_field[0+i*3], "|",
              game_field[1+i*3], "|", game_field[2+i*3], "|")
        print("-" * 13)


def input_answer(XO):
    valid = False
    while not valid:
        player_answer = int(input("Куда поставим " + XO+"? "))

        if player_answer >= 1 and player_answer <= 9:
            if (str(game_field[player_answer-1]) not in "XO"):
                game_field[player_answer-1] = XO
                valid = True
            else:
                print("Эта клеточка уже занята")
        else:
            print("Некорректный ввод. Введите число от 1 до 9 чтобы походить.")


def check_win(game_field):
    win_num = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6),
               (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
    for i in win_num:
        if game_field[i[0]] == game_field[i[1]] == game_field[i[2]]:
            return game_field[i[0]]
    return False


def main(game_field):
    n = 0
    win = False
    while not win:
        draw_field(game_field)
        if n % 2 == 0:
            input_answer("X")
        else:
            input_answer("O")
        n += 1
        if n > 4:
            tmp = check_win(game_field)
            if tmp:
                print(tmp, "выиграли!")
                win = True
                break
        if n == 9:
            print("Ничья!")
            break
    draw_field(game_field)


main(game_field)
