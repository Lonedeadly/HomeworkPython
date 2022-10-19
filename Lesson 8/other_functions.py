def input_number(text):
    print(text)
    tmp = input('Введите число: ')
    if not tmp.isnumeric():
        print('Некорректное значение. Введите число ёпрст!!')
        return -1
    return int(tmp)
