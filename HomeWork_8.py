# # Задача №49. Решение в группах. Создать телефонный справочник с возможностью импорта
#  и экспорта данных в формате .txt. Фамилия, имя, отчество, номертелефона - данные,
#  которые должны находиться в файле.
# 1. Программа должна выводить данные
# 2. Программа должна сохранять данные в текстовом файле
# 3. Пользователь может ввести одну из характеристик для поиска определенной записи
#   (Например имя или фамилию человека)
# 4. Использование функций. Ваша программа не должна быть линейной

# Обязательное ДЗ - доделать телефонный справочник с внешним хранилищем информации,
#  дополнить функционалом добавления информации, удаления и редактирования.

db_path = 'phone_book.json'
welcome = 'Enter command: 1 - read & show | 2 - add record | 3 - search | 4 - init DB | 5 - delete | 6 - edit q - Quit\n'
phone_book = {}

def print_book(book):
    for k, v in book.items():
        print(k, " - ", end=" | ")
        for i, j in v.items():
            print(i, j, end=" | ")
        print()


def init_db(path, db):
    with open(path, 'w', encoding='utf-8') as fh:  # открываем файл на запись
        fh.write(json.dumps(db, ensure_ascii=False))  # преобразовываем словарь data в unicode-строку и записываем в файлe_ascii=False))
        print('БД успешно сохранена')


def load_db(path):
    # загрузить из json
    with open(path, 'r', encoding='utf-8') as fh:  # открываем файл на чтение
        BD_local = json.load(fh)  # загружаем из файла данные в словарь data
    print('БД успешно загружена')
    return BD_local


def new_record(book):
    k = input("New name: ")
    a = {}
    a['phone'] = list(input('New phone: ').split())
    a['birthday'] = input('New birthday: ')
    book[k] = a
    print('Запись успешно внесена')


def search_db(employer, name):
    for k, v in employer.items():
        if v['name'] == name:
            print(v['Phone'])
            return

    print('Не найдено: "{}"'.format(name))


def delete(book, name):
    for k in list(book):
        if book[k]['name'] == name:
            del book[k]
    print(book)


def edit(book):
    a = input("Введите id абонента: ")
    for i in list(book)[:]:
        if a in i:
            print(f'Редактировать: {i} \n')
            flag = True
            while flag:
                x = input('Введите новый элемент: ')
                book[i] = x
                print(i)
                break
            else:
                print('Не верно указан индекс элемента \n')
            break


def init_db(path, db):
    with open(path, 'w', encoding='utf-8') as fh:  # открываем файл на запись
        # преобразовываем словарь data в unicode-строку и записываем в файл
        fh.write(json.dumps(db, ensure_ascii=False))
        print('БД успешно сохранена')


try:
    phone_book = load_db(db_path)
except:
    phone_book = {'id1': {'name': "Лев", 'surname': "Толстой", 'patronymic': "Николаевич", 'Phone': "89-57-34"},
                  'id2': {'name': "Владимир", 'surname': "Ленин", 'patronymic': "Ильич", 'Phone': "07-11-1917"},
                  'id3': {'name': "Александр", 'surname': "Пушкин", 'patronymic': "Сергеевич", 'Phone': None}}

print('База данных не найдена, создаём тестовую БД')


def action():
    action = None
    while action != 'q':
        action = input(f'({welcome}').lower()
        if action == '1':
            print(phone_book)
        elif action == '2':
            new_record(phone_book)
        elif action == '3':
            name_id1 = input("Put the name: ")
            search_db(phone_book, name_id1)
        elif action == '4':
            init_db(db_path, phone_book)
        elif action == '5':
            name = input("Put the name: ")
            delete(phone_book, name)
        elif action == '6':
            edit(phone_book)

action()
save_db(db_path, phone_book)