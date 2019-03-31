import tkinter as tk
import os
import sys


def setup_button(window, text):
    """
    Настраивает кнопку.

    :param window: Окно, на котором должна располагаться кнопка.
    :param text: Текст для отображения на кнопке.
    :returns: Кнопку.
    """

    return tk.Button(window, text=text, width=8)



def setup_entry(window):
    """
    Настраивает строку ввода для окон.

    :param window: Окно, на котором должна располагаться строка ввода.
    :param text: Отображаемая по умолчанию в строка.
    :returns: Строку ввода.
    """

    return tk.Entry(window)


def setup_list_box(window):
    """
    Настраивает список элементов.

    :returns: Список элементов.
    """

    return tk.Listbox(window, heigh=15, selectmode="SINGLE")


def update_path_string(path_string, path):
    """
    Обновляет строку текущего пути.

    :param path_string: Строка пути
    """

    path_string.delete(0, "end")
    path_string.insert(0, path)


def list_dir():
    """
    Составляет список содержимого директории. Путь берет из строки текущего пути.

    :returns: Список содержимого директории.
    """

    path = path_string.get()

    return os.listdir(path)


def update_list_box(list_box):
    """
    Обновляет список элементов.

    :param list_box: Список элементов.
    """

    path = path_string.get()
    dir_content = os.listdir(path)

    for item in dir_content:
        list_box.insert("end", item)


if __name__ == "__main__":
    # Создание главного окна и размещение на нем виджетов 
    main_window = tk.Tk()
    main_window.title("pyfiman")
    main_window.resizable(False, False)

    # Установка строки для отображения пути
    path_string = setup_entry(main_window)
    path_string.grid(row=0, column=0, columnspan=5, sticky="nwes")

    # Установка кнопки GO справа от строки пути
    go_button = setup_button(main_window, "GO")
    go_button.grid(row=0, column=5, sticky="nwes")

    # Установка правой и левой панели
    left_panel = setup_list_box(main_window)
    right_panel = setup_list_box(main_window)
    left_panel.grid(row=1, column=0, columnspan=3, sticky="nwes")
    right_panel.grid(row=1, column=3, columnspan=3, sticky="nwes")

    # Установка нижних кнопок
    copy_button = setup_button(main_window, "Copy")
    move_button = setup_button(main_window, "Move")
    rename_button = setup_button(main_window, "Rename")
    mkdir_button = setup_button(main_window, "Mkdir")
    delete_button = setup_button(main_window, "Del")
    exit_button = setup_button(main_window, "Exit")
    bottom_buttons = [copy_button, move_button,
                      rename_button, mkdir_button, delete_button, exit_button]

    count = 0
    for button in bottom_buttons:
        button.grid(row=2, column=count, sticky="nwes")
        count += 1

    # Определить ОС, на которой работает pyfiman
    if os.name == "posix":
        start_path = "/Users/spmart/Qt/"  # В качестве пути взять root
    elif os.name == "nt":
        start_path = "C:\\"
    else:
        exit(1)

    # Установить стандартные пути для панелей
    left_panel_path = start_path
    right_panel_path = start_path
    update_path_string(path_string, start_path)

    # Загрузить содержимое панелей
    update_list_box(left_panel)
    update_list_box(right_panel)

    tk.mainloop()

    # TODO: Прикрутить скролл к листбоксам
    # TODO: Чекать файл/директория перед вываливанием в листбокс
    # TODO: Обработчики событий для кнопок
    # TODO: Изменение отображаемой директории в зависимости от активного листбокса