import csv
import other_functions as helpof


def get_fieldnames():
    fieldnames = ['login', 'password', 'name', 'type']
    return fieldnames


def get_users():
    users = []
    fieldnames = get_fieldnames()
    with open("users.csv", 'r', newline="", encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile, delimiter=";", fieldnames=fieldnames)
        for row in reader:
            users.append(dict(row))
    return users


def add_user(user_login, user_password, user_name, user_type):

    with open("users.csv", 'a', newline="", encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile, delimiter=';')
        writer.writerow([user_login, user_password, user_name, user_type])


def save_file(row):
    with open("users.csv", 'a', newline="") as csvfile:
        writer = csv.writer(csvfile, delimiter=';')
        writer.writerow([row['login'], row['password'], row['name']])


def input_login():
    return input('Введите логин: ')


def input_password():
    return input('Введите пароль: ')


def input_name():
    return input('Введите ФИО: ')


def input_type():
    user_type = -1
    while user_type == -1:
        user_type = helpof.input_number('Выберите тип пользователя:\n0 - Администратор\n1 - Преподаватель\n2 - Студент')

    return user_type


def authorization():

    valid = False

    users_table = get_users()
    if len(users_table) == 0:
        print('В базе отсутствуют пользователи')
        return

    user_login = ''
    while user_login == '':
        user_login = input_login()
        user = list(user for user in users_table if user['login'] == user_login)
        if len(user) == 0:
            print('\nПользователь не найден')
            user_login = ''
        else:
            user = user[0]

    user_password = ''
    while user_password == '':
        user_password = input_password()
        if not user['password'] == user_password:
            print('Неверный пароль')
            user_password = '';

    return user


def registration():

    users_table = get_users()

    user_login = ''
    while user_login == '':
        user_login = input_login()
        if not len(users_table) == 0:
            result = list(user for user in users_table if user['login'] == user_login)
            if not len(result) == 0:
                print('\nТакой пользователь уже существует')
                user_login = ''

    user_password = ''
    while user_password == '':
        user_password = input_password()
    user_name = input_name()
    user_type = -1
    while user_type < 0 or user_type > 3:
        user_type = input_type()
    add_user(user_login, user_password, user_name, user_type)

    print('Пользователь успешно зарегистрирован')
