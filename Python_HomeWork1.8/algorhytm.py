from functional import interface
path = "phone_book.txt"
enter = 0
while enter != 6:
    enter = interface()
    if enter == 1:
        from functional import add_cont
        stroka = str(input("Введите ФИО и номер телефона через пробел: "))
        add_cont(path, stroka)
    elif enter == 2:
        from functional import show_all
        show_all(path)
    elif enter == 3:
        from functional import search
        stroka = str(input("Введите фамилию: "))
        search(path, stroka)
    elif  enter == 4:
        from functional import change_name
        ch_name = str(input("Введите фамилию: "))
        change_name(path, ch_name)
        #print('Режима редактирования пока нет')
    elif  enter == 5:
        from functional import del_name
        stroka = str(input("Введите фамилию для удаления: "))
        del_name(path, stroka)
        #print('Режима удаления пока нет')
print("До встречи!")
