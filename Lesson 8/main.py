# Создать информационную систему позволяющую работать
# с сотрудниками некой компании \ студентами вуза \ учениками школы
import users
import other_functions as helpof


def view_menu():
    s = 2


stop = False
while not stop:

    action = -1
    while action < 0 or action > 2:
        print('_________________________________________________________')
        action = helpof.input_number('0 - Авторизация\n1 - Регистрация\n2 - Выход')

    if action == 0:
        user = users.authorization()
        if user is not None:
            print(f'Добро пожаловать {user["name"]} - {user["type"]}')
    elif action == 1:
        users.registration()
    elif action == 2:
        print('До встречи')
        stop = True
