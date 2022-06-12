import sys
from string import ascii_letters
from phone_number_project.classes import *

p = Phone()
e = Email()
d = Directory()
d.load()


def add_name():
    while True:
        name = input('Введите имя >>> ')
        if len(name.strip(ascii_letters)) or not name:
            print(f'Имя должно состоять только из латинских букв, повторите ввод!')
        else:
            break
    return name


def add_surname():
    while True:
        surname = input('Введите фамилию >>> ')
        if len(surname.strip(ascii_letters)) or not surname:
            print(f'Фамилия должна состоять только из латинских букв, повторите ввод!')
        else:
            break
    return surname


def add_patronymic():
    while True:
        patronymic = input('Введите отчество >>> ')
        if len(patronymic.strip(ascii_letters)) or not patronymic:
            print(f'Отчество должно состоять только из латинских букв, повторите ввод!')
        else:
            break
    return patronymic


def add_old():
    while True:
        try:
            old = int(input('Введите возраст >>> '))
            break
        except ValueError:
            print('Возраст должен быть целым числом, повторите ввод!')
    return old


def add_phone_number():
    while True:
        try:
            phone_number = input(f'Введите номера телефонов, которые хотите добавить:\n'
                                 f'В формате: 380********* 380*********\n'
                                 f'>>> ')
            p.add_phone_number(phone_number)
            break
        except ValueError:
            print('Неверный формат ввода, повторите попытку!')
    return phone_number


def add_email():
    while True:
        try:
            email = input(f'Введите email адресса, которые хотите добавить:\n'
                          f'В формате: admin@gmail.com admin1@gmail.com\n'
                          f'>>> ')
            e.add_email(email)
            break
        except ValueError:
            print('Неверный формат ввода, повторите попытку!')
    return email


dict_for_create_contact = {
    'name': add_name,
    'surname': add_surname,
    'patronymic': add_patronymic,
    'old': add_old,
    'phone': add_phone_number,
    'email': add_email,
}


def create_new_kontakt():
    name = dict_for_create_contact['name']()
    surname = dict_for_create_contact['surname']()
    patronymic = dict_for_create_contact["patronymic"]()
    old = dict_for_create_contact['old']()
    phone = dict_for_create_contact['phone']()
    email = dict_for_create_contact['email']()

    d.add(name, surname, patronymic, old, phone.split(), email.split())

    p.reload()
    e.reload()


def list_with_all_contacts():
    d.list()


def all_info_about_contact():
    try:
        enter_number = int(input('Введите порядковый номер контакта (можно посмотреть в пункте "2")\n'
                                 '>>> '))
        print(d[enter_number - 1])
    except IndexError:
        print('Такого номера не существует!')
    except ValueError:
        print('Введите исправный номер контакта!')


def delete_contact():
    try:
        enter_number = int(input('Введите порядковый номер контакта для удаления (можно посмотреть в пункте "2")\n'
                                 '>>> '))
        agree = input(f'Вы точно хотите удалить контакт: {d[enter_number - 1].name} {d[enter_number - 1].surname} ?\n'
                      f'Для подтверждения операции введите "y" >>> ')
        if agree == 'y':
            del d[enter_number - 1]
            print(f'Контакт был успешно удален!')
        else:
            pass
    except IndexError:
        print('Такого номера не существует!')
    except ValueError:
        print('Введите исправный номер контакта!')


def edit_contact():
    try:
        enter_number = int(input(f'Введите порядковый номер контакта для изменения (можно посмотреть в пункте "2")\n'
                                 f'>>> '))
        enter_command = input(f'Введите параметр для изменения [name, surname, patronymic, old]\n'
                              f'>>> ')
        done_save = 'Контакт успешно изменен!'
        if enter_command == 'name':
            new_name = input(f'Имя, которое вы хотите изменить: {d[enter_number - 1].name}\n'
                             f'Введите новое имя для контакта >>> ')
            d[enter_number - 1].name = new_name
            print(done_save)
        if enter_command == 'surname':
            new_surname = input(f'Фамилия, которую вы хотите изменить: {d[enter_number - 1].surname}\n'
                                f'Введите новую фамилию для контакта >>> ')
            d[enter_number - 1].surname = new_surname
            print(done_save)
        if enter_command == 'patronymic':
            new_patronymic = input(f'Отчество, которое вы хотите изменить: {d[enter_number - 1].patronymic}\n'
                                   f'Введите новое отчество для контакта >>> ')
            d[enter_number - 1].patronymic = new_patronymic
            print(done_save)
        if enter_command == 'old':
            new_old = input(f'Возраст, который вы хотите изменить: {d[enter_number - 1].old}\n'
                            f'Введите новый возраст для контакта >>> ')
            d[enter_number - 1].old = new_old
            print(done_save)
        d.save()
    except IndexError:
        print('Такого номера не существует!')
    except ValueError:
        print('Введите исправный номер контакта!')


def exit_program():
    print('Сеанс окончен.\n'
          'Все данные сохранены.')
    sys.exit()
