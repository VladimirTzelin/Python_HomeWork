
# 55.  Создать телефонный справочник с возможностью импорта и экспорта данных в формате .txt.
# Фамилия, имя, отчество, номер телефона - данные, которые должны находиться в файле.
# 1. Программа должна выводить данные
# 2. Программа должна сохранять данные в текстовом файле
# 3. Поиск по фамилии


# 1 - добавление контакта
# 2 - вывод списка
# 3 - поиск по фамилии
# 4 - изменение данных
# 5 - удаление данных
# 6 - выход

def interface():
    print(" 1 - добавление контакта \n 2 - вывод списка \n 3 - поиск по фамилии \n 4 - изменение данных\n 5 - удаление данных \n 6 - выход")
    enter = int(input("Введите номер операции: "))
    return enter


def start():
    path = 'phone_book.txt'
    try:
        file = open(path, 'r')
    except IOError:
        print('Создан файл данных -> phone_book.txt')
        file = open(path, 'w')
    finally:
        file.close()


def add_cont(file_name, stroka):
    with open(file_name, 'a', encoding='utf-8') as data:
        # data = open(file_name, 'a')
        data.write(stroka + "\n")
    data.close()


def show_all(file_name):
    with open(file_name, 'r', encoding='utf-8') as data:
        for line in data:
            print(line[:-1])
    data.close()


def search(file_name, stroka):
    is_found = 0
    with open(file_name, 'r', encoding='utf-8') as data:
        for line in data:
            if stroka.lower() in line.split()[0].lower():
                print(line)
                is_found = 1
                break
    if not is_found:
        print("Такой записи нет")

    data.close()


def change_name(file_name, ch_name):
    data = open(file_name, 'r', encoding='utf-8')
    list_name = list()
    for line in data:
        if ch_name in line:
            new_name = input("Введите ФИО и номер абонета:  ")
            list_name.append(new_name + "\n")
            continue
        list_name.append(line)
    data.close()
    list_name = list(filter(lambda x: x != " ", list_name))
    data = open(file_name, 'w', encoding='utf-8')
    for item in list_name:
        data.write(item)
    data.close()
    print(f'Контакт: {ch_name} >>изменён<<\n')


def del_name(file_name, del_name):
    is_found = 0
    with open(file_name, 'r', encoding='utf-8') as data:
        list_name = list()
        for line in data:
            if del_name in line:
                is_found = 1
                continue
            if line != " ":
                list_name.append(line)
    list_name = list(filter(lambda x: x != " ", list_name))
    data = open(file_name, 'w', encoding='utf-8')
    for item in list_name:
        data.write(item)
    data.close()
    if is_found:
        print(f'Контакт: {del_name} >>удалён<<\n')
    else:
        print(f'Контакт: {del_name} >>не найден<<\n')
    