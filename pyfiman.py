import tkinter as tk
import os


def setup_button(window, text):
    """
    Настраивает кнопку.

    :param window: Окно, на котором должна располагаться кнопка.
    :param text: Текст для отображения на кнопке.
    :returns: Кнопку.
    """

    return tk.Button(window, text=text, width=8)
#    return tk.Button(window, text=text, width=10, height=1)  # Размеры кнопки указываются в знакоместах. Наркомания.



def setup_entry(window):
    """
    Настраивает стандартную ввода для окон.

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
    #return tk.Listbox(window, heigh=25, width=30, selectmode="SINGLE")


def setup_main_window():
    """
    Настраивает основные парметры главного окна и заполняет его виджетами.

    :returns: Главное окно приложения.
    """

    main_window = tk.Tk()
    main_window.title("pyfiman")
    #main_window.geometry("800x600")
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
    bottom_buttons = [copy_button, move_button, rename_button, mkdir_button, delete_button, exit_button]
    
    count = 0
    for button in bottom_buttons:
        button.grid(row=2, column=count, sticky="nwes")
        count += 1

    return main_window


if __name__ == "__main__":
    main_window = setup_main_window()
    
    tk.mainloop()
