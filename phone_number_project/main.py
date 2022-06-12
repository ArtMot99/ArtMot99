from phone_number_project.functions import *


def start_program():
    try:
        while True:
            enter_command = int(input(f'Введите цифру для выполнения команды!\n'
                                      '1. Создать новый контакт.\n'
                                      '2. Вывести список существующих контактов.\n'
                                      '3. Полная информация о выбраном контакте.\n'
                                      '4. Изменить выбраный контакт.\n'
                                      '5. Удалить выбраный контакт.\n'
                                      '6. Закрыть программу.\n'
                                      '>>> '))
            print(enter_command)

            if enter_command == 1:
                create_new_kontakt()

            if enter_command == 2:
                list_with_all_contacts()

            if enter_command == 3:
                all_info_about_contact()

            if enter_command == 4:
                edit_contact()

            if enter_command == 5:
                delete_contact()

            if enter_command == 6:
                exit_program()

    except ValueError:
        print('Ошибка ввода!')


if __name__ == '__main__':
    start_program()
