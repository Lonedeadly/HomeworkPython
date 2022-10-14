import random
from builtins import range


# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".
def task1():
    a = "вабв ава абв аве"
    # a = input("Введите текст: ")
    lst = a.split()
    print(lst)
    new_lst = []
    for i in lst:
        if i.find("абв") == -1:
            new_lst.append(i)
    print(new_lst)


# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход.
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
#   a) Добавьте игру против бота
#   b) Подумайте как наделить бота ""интеллектом""
def task2():
    def ask_current_amount_bot(step):
        if step.get('use_bot_mind'):
            total = step.get('total')
            max_step = step.get('max_step')
            pos_step = total // (max_step + 1)
            if total <= max_step:
                current_amount = max_step
            else:
                current_amount = total - (pos_step * (max_step + 1))
            if current_amount == 0:
                current_amount = random.randint(1, step.get('max_step'))
        else:
            current_amount = random.randint(1, step.get('max_step'))

        return current_amount

    def ask_current_amount(step):
        move_player1 = step.get('move_player1')
        if move_player1:
            player = step.get('player1')
        else:
            player = step.get('player2')
        max_step = step.get('max_step')

        if step.get('use_bot') and not move_player1:
            current_amount = ask_current_amount_bot(step)
            print(f"{player} сколько конфет вы заберете (от 1 до {max_step})? {current_amount}")
        else:
            current_amount = int(input(f"{player} сколько конфет вы заберете (от 1 до {max_step})? "))
            while current_amount == 0 or current_amount > max_step:
                print("Введено некорректное число")
                current_amount = int(input(f"{player} сколько конфет вы заберете (от 1 до {max_step})? "))

        return current_amount

    def next_step(step):
        current_amount = ask_current_amount(step)
        step.update(move_player1=not step.get('move_player1'))
        step.update(current_amount=current_amount)
        step.update(total=step.get('total') - current_amount)

        return step

    def start(use_bot, use_mind_bot):
        total = 121
        max_step = 28
        move_player1 = bool(random.randint(0, 1))

        if use_bot:
            player1 = "Путин Владимир Владимирович"
            player2 = "Компьютер"
        else:
            player1 = "Путин Владимир Владимирович"
            player2 = "Джо Байден"

        if move_player1:
            print(f"Первый ход за {player1}")
        else:
            print(f"Первый ход за {player2}")

        step = {"use_bot": use_bot,
                "use_bot_mind": use_mind_bot,
                "total": total,
                "current_amount": 0,
                "move_player1": move_player1,
                "max_step": max_step,
                "player1": player1,
                "player2": player2}

        print(step)
        print()

        while step.get('total') > 0:
            max_step = step.get('max_step')
            if max_step > step.get('total'):
                step.update(max_step=step.get('total'))
            print()
            print(f"Конфет на столе {step.get('total')}")
            step = next_step(step)
        else:
            print('__________________________')
            if not step.get('move_player1'):
                win = player1
            else:
                win = player2
            print(f"Победитель {win}")

        # mind_comp = ""
        #
        # move_player1 = random.randint(0, 1)
        # if move_player == 0:
        #     print("Первый ход за компьютером")
        # else:
        #     print("Первый ход за человеком")
        #

    bot_diff = 0
    use_bot = bool(int(input("Включить игру против бота (0 - Нет, 1 - Да)? ")))
    if use_bot:
        use_mind_bot = bool(int(input("Добавить боту интелект? (0 - Нет, 1 - Да)? ")))
    else:
        use_mind_bot = False

    start(use_bot, use_mind_bot)


# Создайте программу для игры в ""Крестики-нолики"".
def task3():
    def raw_input(steps, sym):
        valid = False
        while not valid:
            b = int(input(f"Куда ставим {sym} (0-8)? "))
            if 0 <= b <= 8:
                if steps[b] == " ":
                    valid = True
            else:
                continue

        return b

    def print_board(step):
        for i in range(3):
            print(f'| {step[(i * 3) + 0]} | {step[(i * 3) + 1]} | {step[(i * 3) + 2]} |')
            print('|---|---|---|')

    def check_win(wins_row, step, sym):
        for i in wins_row:
            win = True
            for a in i:
                if not step[a] == sym:
                    win = False
                    break
            if win:
                break
        return win

    wins_row = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
    steps = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
    print_board(steps)
    end = False
    shag = False
    i = 0
    while not end and not i == 9:
        if shag:
            sym = "o"
        else:
            sym = "x"
        steps[raw_input(steps, sym)] = sym
        print_board(steps)
        end = check_win(wins_row, steps, sym)
        shag = not shag
        i += 1
    else:
        if not end and i == 10:
            print("Ничья")
        else:
            print(f"Выйграл {sym}")


def task4():
    def coding(txt):
        count = 1
        res = ''
        for i in range(len(txt) - 1):
            if txt[i] == txt[i + 1]:
                count += 1
            else:
                res = res + str(count) + txt[i]
                count = 1
        if count > 1 or (txt[len(txt) - 2] != txt[-1]):
            res = res + str(count) + txt[-1]
        return res

    def decoding(txt):
        number = ''
        res = ''
        for i in range(len(txt)):
            if not txt[i].isalpha():
                number += txt[i]
            else:
                res = res + txt[i] * int(number)
                number = ''
        return res

    s = input("Введите текст для кодировки: ")
    cod = coding(s)
    print(f"Текст после кодировки: {cod}")
    print(f"Текст после дешифровки: {decoding(cod)}")

task = int(input("Какую задачу проверить? "))

if task == 1:
    task1()
elif task == 2:
    task2()
elif task == 3:
    task3()
elif task == 4:
    task4()
# elif task == 5:
#     task5()
else:
    print("Пора спать")
