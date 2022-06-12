import json
import string


class Person:
    def __init__(self, name, surname, patronymic, old, phone_number, email):
        self.name = name
        self.surname = surname
        self.patronymic = patronymic
        self.old = old
        self.phone_number = phone_number
        self.email = email

    def __str__(self):
        return f'{"Name:":<14} {self.__name}\n' \
               f'{"Surname:":<14} {self.__surname}\n' \
               f'{"Patronymic:":<14} {self.__patronymic}\n' \
               f'{"Years:":<14} {self.old}\n' \
               f'{"Phone numbers:":<14} {self.phone_number}\n' \
               f'{"Emails:":<14} {self.email}'

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        self.__name = new_name

    @property
    def surname(self):
        return self.__surname

    @surname.setter
    def surname(self, new_surname):
        self.__surname = new_surname

    @property
    def patronymic(self):
        return self.__patronymic

    @patronymic.setter
    def patronymic(self, new_patronymic):
        self.__patronymic = new_patronymic

    @property
    def old(self):
        return self.__old

    @old.setter
    def old(self, new_old):
        self.__old = new_old

    @property
    def phone_number(self):
        return self.__phone_number

    @phone_number.setter
    def phone_number(self, new_phone):
        self.__phone_number = new_phone

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, new_email):
        self.__email = new_email


# Класс для хранения и обработки email адрессов
class Email:
    def __init__(self):
        self.emails = []

    def reload(self):
        self.emails = []

    def add_email(self, emails):
        for value in emails.split():
            if '@' in value:
                self.emails.append(value)
            else:
                raise ValueError('Неверный формат ввода!')


# Класс для хранения и обработки номеров телефона
class Phone:
    def __init__(self):
        self.phone_list = []

    def reload(self):
        self.phone_list = []

    def add_phone_number(self, numbers):
        for value in numbers.split():
            if len(value) == 12 and not len(value.strip(string.digits)):
                self.phone_list.append(value)
            else:
                raise ValueError('Неверный формат ввода!')


class Directory:
    def __init__(self, filename='List.json'):
        self.directory = []
        self.filename = filename

    def save(self):
        """
        Метод сохранения данных в файл

        :return: None
        """
        with open(self.filename, 'w', encoding='UTF-8') as file:
            lst = []
            for line in self.directory:
                lst.append(line.__dict__)
            json.dump(lst, file, indent=2)

    def load(self):
        """
        Метод загрузки файла, при старте программы

        :return: None
        """
        try:
            with open(self.filename, encoding='UTF-8') as file:
                data = json.load(file)
                for i in data:
                    self.directory.append(Person(name=i["_Person__name"],
                                                 surname=i["_Person__surname"],
                                                 patronymic=i["_Person__patronymic"],
                                                 old=i["_Person__old"],
                                                 phone_number=i["_Person__phone_number"],
                                                 email=i["_Person__email"]))
        except (EOFError, OSError):
            pass

    def add(self, name, surname, patronymic, old, phone_number, email):
        """
        Метод для добавления нового контакта

        :param name: str
        :param surname: str
        :param patronymic: str
        :param old: int
        :param phone_number: list
        :param email: list
        :return: None
        """
        self.directory.append(Person(name, surname, patronymic, old, phone_number, email))
        print('Обьект успешно добавлен')
        self.save()

    def list(self):
        """
        Метод для вывода на экран информации о контактах

        :return: None
        """
        for value in self.directory:
            print(f'Имя: {value.name} | Фамилия: {value.surname} | Список номеров: {value.phone_number}')

    def __getitem__(self, item):
        """
        Метод для получения данных о выбраном контакте

        :param item: int
        :return: str
        """
        return self.directory[item]

    def __delitem__(self, item):
        """
        Метод для удаления данных из списка контактов

        :param item: int
        :return: None
        """
        del self.directory[item]
        self.save()
