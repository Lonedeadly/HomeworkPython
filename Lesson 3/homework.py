# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример: [2, 3, 5, 9, 3, 5] -> на нечётных позициях элементы 3 и 9, ответ: 12
from builtins import print


def task1():
    lst = [2, 3, 5, 9, 3]
    sum = 0
    i = 1
    while i < len(lst):
        sum += lst[i]
        i += 2
    print(sum)

# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]
def task2():
    new_lst = []
    lst = [2, 3, 4, 5, 6]
    for i in range(len(lst)):
        if i <= len(lst) / 2:
            new_lst.append(lst[i] * lst[-i-1])
    print(new_lst)


# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# Пример: [1.1, 1.2, 3.1, 5, 10.01] => 0.19
def task3():
    lst = [1.1, 1.2, 3.1, 5, 10.01]
    min_i = 0
    max_i = 0
    for i in lst:
        drob = i % 1
        if drob < min_i:
            min_i = drob
        if drob > max_i:
            max_i = drob
    print(max_i - min_i)


# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10
def task4():
    a = int(input("Введите число: "))
    lst = []
    while a / 2 >= 1:
        lst.append(a % 2)
        a = int(a / 2)
    else:
        lst.append(a)
    lst.reverse()
    print("".join(map(str, lst)))


# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
#
# Пример:
#
# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]
def task5():
    a = int(input("Введите число: "))
    lst = [0, 1]
    for i in range(a - 1):
        lst.append(lst[i] - lst[-1])
    lst.reverse()

    for i in range(a):
        print(lst[-1], lst[-2])
        lst.append(lst[-1] + lst[-2])
    print(lst)

task = int(input("Какую задачу проверить? "))

if task == 1:
    task1()
elif task == 2:
    task2()
elif task == 3:
    task3()
elif task == 4:
    task4()
elif task == 5:
    task5()
else:
    print("Пора спать")





