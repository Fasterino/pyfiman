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
        # Проверить, файл это или директория
        if os.path.isdir(path + item):  # Если директория
            list_box.insert("end", item + "/")  # В конец добавить /
        elif os.path.isfile(path + item):  # Перестраховывамся. Если попадает какое-то дерьмо, не добавляем
            list_box.insert("end", item)


def left_panel_clicked(event):
    """Обрабатывает клик левой кнопкой мыши по левой панели
    
    Arguments:
        event {Event} -- Событие клика левой кнопкой мыши
    """

    global last_active_panel, path_field,  left_panel_path

    if last_active_panel == "r":  # Проверка нужна, чтобы не затирать путь лишний раз
        last_active_panel = "l" # Запоминаем последнюю использованную панель
        update_path_field(path_field, left_panel_path)


def right_panel_clicked(event):
    """Обрабатывает клик левой кнопкой мыши по правой панели
    
    Arguments:
        event {Event} -- Событие клика левой кнопкой мыши
    """

    global last_active_panel, path_field, right_panel_path

    if last_active_panel == "l":  # Проверка нужна, чтобы не затирать путь лишний раз
        last_active_panel = "r"  # Возможно, это можно сделать средствами Tk, но нет
        update_path_field(path_field, right_panel_path)


def left_panel_doubleclicked(event):
    """Обрабатывает двойной клик в левой панели
    
    Arguments:
        event {Event} -- Событие двойного клика левой кнопкой мыши
    """
    global path_field, right_panel, left_panel_path

    current_path = path_field.get()
    new_path = left_panel.get(left_panel.curselection())
    left_panel_path = current_path + new_path
    update_path_field(path_field, left_panel_path)
    update_list_box(left_panel)


def right_panel_doubleclicked(event):
    """Обрабатывает двойной клик в правой панели
    
    Arguments:
        event {Event} -- Событие двойного клика левой кнопкой мыши
    """
    global path_field, right_panel, right_panel_path

    current_path = path_field.get()
    new_path = right_panel.get(right_panel.curselection())
    right_panel_path = current_path + new_path
    update_path_field(path_field, right_panel_path)
    update_list_box(right_panel)


def go_button_clicked(event):
    """Обрабатывает нажатие на кнопку GO
    
    Arguments:
        event {Event} -- Событие нажатия на кнопку
    """

    global left_panel_path, right_panel_path

    path = path_field.get()

    if last_active_panel == "l":
        left_panel_path = path
        update_list_box(left_panel)
    elif last_active_panel == "r":
        right_panel_path = path
        update_list_box(right_panel)



if __name__ == "__main__":
    # Создание главного окна и размещение на нем виджетов
    main_window = Tk()
    main_window.title("pyfiman")
    main_window.resizable(False, False)

    # Установка строки для отображения пути
    path_field = Entry(main_window)
    path_field.grid(row=0, column=0, columnspan=5, sticky="nwes")

    # Установка кнопки GO справа от поля со строкой пути
    go_button = Button(main_window, text="GO")
    go_button.grid(row=0, column=5, sticky="nwes")
    # Привязать обработчик нажатия кнопки
    go_button.bind("<Button-1>", go_button_clicked)

    # Установка правой и левой панелей
    left_panel = Listbox(main_window, heigh=15, selectmode="single")
    left_panel.grid(row=1, column=0, columnspan=3, sticky="nwes")
    left_scroll = Scrollbar(command=left_panel.yview)  # Сделать скролл, но не добавить в окно. Гениально.

    right_panel = Listbox(main_window, heigh=15, selectmode="single")
    right_panel.grid(row=1, column=3, columnspan=3, sticky="nwes")
    right_scroll = Scrollbar(command=right_panel.yview)  # И он все равно работает. Виджет есть, но не отображается.

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
        button.grid(row=2, column=count, sticky="nwes")
        count += 1

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

    # Привязать обработчики клика по панелям
    last_active_panel = "l"
    left_panel.bind("<Button-1>", left_panel_clicked)
    left_panel.bind("<Double-Button-1>", left_panel_doubleclicked)
    right_panel.bind("<Button-1>", right_panel_clicked)
    right_panel.bind("<Double-Button-1>", right_panel_doubleclicked)

    # Загрузить содержимое панелей
    update_list_box(left_panel)
    update_list_box(right_panel)

    mainloop()

    # TODO:+Прикрутить скролл к листбоксам
    # TODO:+Сделать скролл невидимым (не упаковывать в окно?)
    # TODO:+Чекать файл/директория перед вываливанием в листбокс
    # TODO: Обработчики событий для кнопок
    # TODO: Изменение отображаемой директории в зависимости от активного листбокса
    # TODO:+Переписать формирование формы. Нет смысла пилить для этого пачку функций
