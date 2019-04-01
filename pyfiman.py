from tkinter import *
import os


def update_path_field(path_field, path):
    """Поле со строкой пути для активного окна
    
    Arguments:
        path_field {Entry} -- Поле со строкой пути
        path {str} -- Путь
    """

    path_field.delete(0, "end")
    path_field.insert(0, path)


def update_list_box(list_box):
    """Обновляет список файлов и папок в панели
    
    Arguments:
        list_box {Listbox} -- Одна из панелей
    """

    list_box.delete(0, "end")
    path = path_field.get()
    dir_content = os.listdir(path)

    for item in dir_content:
        list_box.insert("end", item)


if __name__ == "__main__":
    # Создание главного окна и размещение на нем виджетов
    main_window = Tk()
    main_window.title("pyfiman")
    main_window.resizable(False, False)

    # Установка строки для отображения пути
    path_field = Entry(main_window)
    path_field.grid(row=0, column=0, columnspan=10, sticky="nwes")

    # Установка кнопки GO справа от поля со строкой пути
    go_button = Button(main_window, text="GO")
    go_button.grid(row=0, column=10, columnspan=2, sticky="nwes")

    # Установка правой и левой панелей
    left_panel = Listbox(main_window, heigh=15, selectmode="single")
    left_panel.grid(row=1, column=0, columnspan=5, sticky="nwes")
    left_scroll = Scrollbar(command=left_panel.yview)
    left_scroll.grid(row=1, column=5, sticky="nwes")

    right_panel = Listbox(main_window, heigh=15, selectmode="single")
    right_panel.grid(row=1, column=6, columnspan=5, sticky="nwes")
    right_scroll = Scrollbar(command=right_panel.yview)
    right_scroll.grid(row=1, column=11, sticky="nwes")

    # Установка нижних кнопок
    copy_button = Button(main_window, text="Copy", width=8)
    move_button = Button(main_window, text="Move", width=8)
    rename_button = Button(main_window, text="Rename", width=8)
    mkdir_button = Button(main_window, text="Mkdir", width=8)
    delete_button = Button(main_window, text="Del", width=8)
    exit_button = Button(main_window, text="Exit", width=8)
    bottom_buttons = [copy_button, move_button,
                      rename_button, mkdir_button, delete_button, exit_button]
    count = 0
    for button in bottom_buttons:
        button.grid(row=2, column=count, columnspan=2, sticky="nwes")
        count += 2

    # Определить ОС, на которой работает pyfiman
    if os.name == "posix":
        start_path = "/"  # В качестве пути взять root
    elif os.name == "nt":
        start_path = "C:\\"
    else:
        exit(1)

    # Установить стандартные пути для панелей
    left_panel_path = start_path
    right_panel_path = start_path
    update_path_field(path_field, start_path)

    # Загрузить содержимое панелей
    update_list_box(left_panel)
    update_list_box(right_panel)

    mainloop()

    # TODO:+Прикрутить скролл к листбоксам
    # TODO: Сделать скролл невидимым (не упаковывать в окно?)
    # TODO: Чекать файл/директория перед вываливанием в листбокс
    # TODO: Обработчики событий для кнопок
    # TODO: Изменение отображаемой директории в зависимости от активного листбокса
    # TODO:+Переписать формирование формы. Нет смысла пилить для этого пачку функций
