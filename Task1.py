'''Создайте программу для игры с конфетами человек против человека.

Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. 
Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. 
Все конфеты оппонента достаются сделавшему последний ход. 
Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?

a) Добавьте игру против бота

b) (доп) Подумайте как наделить бота ""интеллектом""
'''
import random


def p2p():

    num_of_players = 2
    ostatok = 2021
    num_of_try = 28
    list_of_players = [i for i in range(1, num_of_players+1)]
    i = 0
    while ostatok > 0:
        if num_of_try > ostatok:
            num_of_try = ostatok
        candy_take = int(input(
            f"\nОсталось {ostatok} конфет.  \nИгрок {list_of_players[i]} может взять не более {num_of_try} конфет: "))
        if candy_take < 0 or candy_take > num_of_try:
            print("\nВведено неверное значение, повторите ввод!")
        else:
            ostatok -= candy_take
            if ostatok == 0:
                break
            else:
                if i == num_of_players-1:
                    i = 0
                else:
                    i += 1

    print(f"Игрок {list_of_players[i]} забрал последние конфеты. Он победил!!")


def p2b():

    num_of_players = 2
    ostatok = 2021
    num_of_try = 28
    start = input("Нажмите enter для начала игры")
    coin = random.randint(0, 2)
    if coin == 0:
        list_of_players = ["Игрок", "Bot"]
        print("Игрок начинает первый \n")
    else:
        list_of_players = ["Bot", "Игрок"]
        print("Bot начинает первый \n")
    i = 0
    while ostatok > 0:
        if num_of_try > ostatok:
            num_of_try = ostatok
        if list_of_players[i] == "Игрок":
            candy_take = int(input(
                f"\nОсталось {ostatok} конфет.  \nИгрок {list_of_players[i]} может взять не более {num_of_try} конфет: "))
            if candy_take < 0 or candy_take > num_of_try:
                print("\nВведено неверное значение, повторите ввод!")

        else:
            candy_take = random.randint(1, num_of_try)
            print(
                f"\nОсталось {ostatok} \n{list_of_players[i]} : {candy_take}")
        ostatok -= candy_take
        if ostatok == 0:
            break
        else:
            if i == num_of_players-1:
                i = 0
            else:
                i += 1

    print(f"Игрок {list_of_players[i]}забрал последние конфеты. Он победил!! ")


a = int(input("выберите режим игры\nДля режима игрок против игрока, введите 1\nДля режима игрок против бота введите 2:"))
if a == 1:
    p2p()
else:
    p2b()
