from random import randrange

def task1():
    a = input('Введите число: ')
    sum = 0

    for i in range(0, len(a)):
        if a[i].isdigit():
            sum = sum + int(a[i])
    print(sum)


def task2():
    n = int(input('Введите число: '))
    a = 1
    lst = []
    for i in range(1, n + 1):
        a = a * i
        lst.append(a)
    print(lst)


def task3():
    n = int(input('Введите число: '))
    sum = 0
    lst = []
    for i in range(1, n + 1):
        lst.append((1 + 1 / i) ** i)
    for i in range(len(lst)):
        sum = sum + lst[i]

    print(round(sum, 3))


def task4():
    n = int(input('Введите число: '))
    lst = []
    pos1 = int(input('Позиция первого элемента = '))
    pos2 = int(input('Позиция второго элемента = '))

    for i in range(-n, n+1):
        lst.append(i)
    print(lst)

    result = lst[pos1-1] * lst[pos2-1]
    print(result)


def task5():
    lst = []
    for i in range(10):
        lst.append(i)
    print(lst)

    for i in range(10):
        temp = lst[i]
        random = lst[randrange(0, 10)]
        lst[i] = lst[random]
        lst[random] = temp
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