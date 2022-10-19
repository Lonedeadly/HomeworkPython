import file


def input_number(text):
    tmp = input(text)
    if not tmp.isnumeric():
        return -1
    return int(tmp)


def view_recordings(data):
    print("Просмотр записей")
    for row in data:
        print(row)
    return data


def add_recordings(data):
    print('Добавление записей')
    repeat = True
    while repeat:
        row = file.get_structure_row()
        row['first_name'] = input('Введите имя: ')
        row['second_name'] = input('Введите фамилию: ')
        row['phone'] = input('Введите телефон: ')
        row['description'] = input('Введите описание: ')

        data.append(row)
        repeat = -1
        while not repeat == 0 and not repeat == 1:
            repeat = input_number('Запись добавлена. Добавить еще? (0 - Нет, 1 - Да) ')
        bool(repeat)

    return data


def export_recordings(data):
    print('Экспорт записей')
    file_address = 'export_file.csv'
    file.save_file(data, file_address)
    return data


def import_recordings(data):
    print('Импорт записей')
    file_address = 'export_file.csv'
    new_data = file.read_file(file_address)
    for row in new_data:
        data.append(row)
    return data


def quit_program(data):
    print('Завершение работы')
    file.save_file(data)
    return True
