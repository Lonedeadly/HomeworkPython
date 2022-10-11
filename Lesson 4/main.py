from random import choices, randrange

def Task1():
    d = float(input('Введите точность чиcла Пи: '))
    summa = 1
    n = 3
    flag = False
    while 1 / n > d:
        if flag:
            summa = summa + (1 / n)
            flag = False
        else:
            summa = summa - (1 / n)
            flag = True
        n = n + 2
    print(summa * 4)


def is_prime(number):
    for i in range(2, number):
        if number % i == 0:
            return False
    return True


def prime_factors(number):
    if is_prime(number):
        return 'Это простое число'

    factor = 2
    lst = []
    while number != 1:
        if is_prime(factor) and number % factor == 0:
            number /= factor
            lst.append(factor)
        else:
            factor += 1

    return lst


def Task2():
    num = int(input('Число = '))
    print(prime_factors(num))


def Task3():
    n = int(input('Количество чисел в последовательности = '))
    lst = []
    lst_result = []
    sum = 0

    for i in range(n):
        lst.append(int(input('Число ' + str(i + 1) + ' = ')))

    for i in range(n):
        if lst.count(lst[i]) == 1:
            lst_result.append(lst[i])

    print(lst_result)


def add_plus_minus(str_data):
    if str_data == '':
        return str_data
    return str_data + f" {choices('+-', k=1)[0]} "


def add_to_file(str_data):
    with open("task4.txt", "a", encoding="utf-8") as output:
        output.write(str_data + '\n')


def Task4():
    k = int(input('k = '))

    ls = []
    for i in range(k):
        ls.append(randrange(0, 101))
    print('Список коэффициентов')
    print(ls)

    eq = ''
    while k >= -1:
        if ls[k - 1] == 0:
            k -= 1
            continue
        elif k > 1:
            eq = add_plus_minus(eq)
            eq = eq + f'{ls[k - 1]}*x^{k}'
        elif k == 1:
            eq = add_plus_minus(eq)
            eq = eq + f'{ls[k - 1]}'
        elif k == 0:
            eq = eq + ' = 0'
        k -= 1

    print(eq)
    add_to_file(eq)


def read_file(name):
    with open(name, "r", encoding="utf-8") as output:
        lst = []
        for line in output:
            lst.append(line)
        output.close()
        return lst


def Task5():
    lst_1 = read_file('file1.txt')
    lst_2 = read_file('file2.txt')
    if len(lst_1) != len(lst_2):
        print('The contents of the files do not match!')
        return
    with open("task5.txt", "w", encoding="utf-8") as output:
        for i in range(2):
            output.write(lst_1[i].replace('= 0', '+ ').replace('\n', '') + lst_2[i])


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