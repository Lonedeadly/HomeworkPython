import actions
import file


def select_menu(i):

    if i == 1:
        action = actions.view_recordings
    elif i == 2:
        action = actions.add_recordings
    elif i == 3:
        action = actions.export_recordings
    elif i == 4:
        action = actions.import_recordings
    elif i == 5:
        action = actions.quit_program
    return action


def view_menu():
    menu = (
        "1. Просмотр записей",
        "2. Добавление записей",
        "3. Экспорт",
        "4. Импорт",
        "5. Выход",
    )

    data = file.read_file()

    stop = False
    while not stop:
        print(menu)

        select_number = -1
        while select_number < 1 or select_number > 5:
            select_number = actions.input_number("Выберите действие(1-5): ")

        action = select_menu(select_number)
        data = action(data)

        if select_number == 5:
            stop = True
