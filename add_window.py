import customtkinter as ctk
from CTkMessagebox import CTkMessagebox
from settings import *
from tkinter.filedialog import askopenfile
import shutil
from PIL import Image, ImageTk
import os
import json
from convert_to_json import to_json


class AddMaterialWindow(ctk.CTkToplevel):
    def __init__(self, parent, type: str) -> None:
        super().__init__(master = parent)

        self.title('Add book')
        self.geometry('500x700')
        self.resizable(False, False)

        # load default picture
        picture = Image.open(MATERIALS_PICTURE_PATH + 'default.png').resize((300, 300))
        self.__book_image = ImageTk.PhotoImage(picture)
        self.__picture_name: str = 'default.png'

        # widget for showing the picture
        self.__title = ctk.CTkEntry(self, placeholder_text = 'Название', font = ENTRY_FONT)
        self.__image = ctk.CTkLabel(self, text = '', image = self.__book_image)
        self.__amount = ctk.CTkEntry(self, placeholder_text = 'Количество', font = ENTRY_FONT)
        self.__price = ctk.CTkEntry(self, placeholder_text = 'Цена', font = ENTRY_FONT)
        self.__fine = ctk.CTkEntry(self, placeholder_text = 'Штраф', font = ENTRY_FONT)

        self.focus()

        self.__create_layout(type)

    # init widgets for book
    def __init_book_window(self) -> None:
        self.__authors = ctk.CTkEntry(self, placeholder_text = 'Автор(ы)', font = ENTRY_FONT)
        self.__publisher = ctk.CTkEntry(self, placeholder_text = 'Издательство', font = ENTRY_FONT)
        self.__publish_year = ctk.CTkEntry(self, placeholder_text = 'Год издания', font = ENTRY_FONT)
        self.__amount = ctk.CTkEntry(self, placeholder_text = 'Количество', font = ENTRY_FONT)

    # init widgets for paper
    def __init_paper_window(self) -> None:
        self.__number = ctk.CTkEntry(self, placeholder_text = 'Номер выпуска', font = ENTRY_FONT)
        self.__date = ctk.CTkEntry(self, placeholder_text = 'Дата выпуска', font = ENTRY_FONT)

    # init widgets for magazine
    def __init_magazine_window(self):
        self.__init_paper_window()

        self.__publisher = ctk.CTkEntry(self, placeholder_text = 'Издательство', font = ENTRY_FONT)

    # create layput for book
    def __create_book_layout(self) -> None:
        self.__init_book_window()

        self.__authors.pack(fill = 'x', padx = 5, pady = 5)
        self.__publisher.pack(fill = 'x', padx = 5, pady = 5)
        self.__publish_year.pack(fill = 'x', padx = 5, pady = 5)

    # create layout for paper
    def __create_paper_layout(self):
        self.__init_paper_window()

        self.__number.pack(fill = 'x', padx = 5, pady = 5)
        self.__date.pack(fill = 'x', padx = 5, pady = 5)

    # create layout for magazine
    def __create_magazine_layout(self):
        self.__init_magazine_window()
        self.__create_paper_layout()

        self.__publisher.pack(fill = 'x', pady = 5, padx = 5)

    # create the whole layout
    def __create_layout(self, type: str) -> None:
        command = None

        self.__image.pack(pady = 5)

        ctk.CTkButton(self, 
                  text = 'Выбрать изображение', 
                  font = FONT,
                  text_color = BTN_TEXT_COLOUR,
                  fg_color = BTN_COLOUR,
                  hover_color = HOVER_BTN_COLOUR, 
                  command = self.__select_image).pack(pady = 5)
        
        self.__title.pack(fill = 'x', pady = 5, padx = 5)

        if type == 'Книгу':
            self.__create_book_layout()
            command = self.__save_book_data

        elif type == 'Газету':
            self.__create_paper_layout()
            command = self.__save_paper_data

        elif type == 'Журнал':
            self.__create_magazine_layout()
            command = self.__save_magazine_data

        self.__amount.pack(fill = 'x', pady = 5, padx = 5)
        self.__price.pack(fill = 'x', pady = 5, padx = 5)
        self.__fine.pack(fill = 'x', pady = 5, padx = 5)

        ctk.CTkButton(self, 
                  text = 'Сохранить', 
                  font = FONT,
                  text_color = BTN_TEXT_COLOUR,
                  fg_color = BTN_COLOUR,
                  hover_color = HOVER_BTN_COLOUR, 
                  command = command).pack(pady = 10)


    # select image for the book
    def __select_image(self) -> None:
        file_path = askopenfile(filetypes = [('JPG files', ['*jpeg', '*jpg']), ('PNG files', '*png'), ('Image files', ['*jpg', '*jpeg', '*png'])])

        if file_path is None:
            return
        else:
            self.__picture_name = file_path.name.split('/')[-1]

            # если файл с таким названием уже есть в папке - спрашиваем, нужно ли его копировать
            if self.__picture_name in os.listdir(MATERIALS_PICTURE_PATH):

                message = CTkMessagebox(self, title = 'Внимание',
                                        message = 'Файл с таким названием уже есть в папке. Заменить его?',
                                        option_1 = 'Да',
                                        option_2 = 'Нет',
                                        icon = 'warning')
                
                if message.get() == 'Да':
                    shutil.copy(file_path.name, MATERIALS_PICTURE_PATH)

            else:
                shutil.copy(file_path.name, MATERIALS_PICTURE_PATH)

            path = MATERIALS_PICTURE_PATH + self.__picture_name

            image = Image.open(path).resize((300, 300))
            self.__book_image = ImageTk.PhotoImage(image)

            self.__image.configure(image = self.__book_image)

    # show warning if not all fields are filled
    def __show_warning(self) -> None:
        CTkMessagebox(self, 
                          title = 'Внимание',
                          message = 'Необходимо заполнить все поля',
                          icon = 'cancel',
                          option_1 = 'OK',
                          font = FONT)

    # save book data
    def __save_book_data(self) -> None:
        title = self.__title.get()
        authors = self.__authors.get().replace(' ', '').split(',')
        publisher = self.__publisher.get()
        publish_year = int(self.__publish_year.get())
        amount = int(self.__amount.get())
        price = float(self.__price.get())
        fine = float(self.__fine.get())

        if title == '' or authors == '' or publisher == '' or publish_year == 0 or amount == '':
            self.__show_warning()
            return

        data = to_json(title, 'Книга', amount, price, fine,
                authors = authors, 
                publisher = publisher,
                publish_year = publish_year)
        
        with open(DATA_PATH + 'material.json', 'w', encoding = 'utf-8') as file:
            json.dump(data, file, indent = 4, ensure_ascii = False)

    # save newspaper data
    def __save_paper_data(self) -> None:
        title = self.__title.get()
        number = self.__number.get()
        date = self.__date.get()
        amount = int(self.__amount.get())
        price = float(self.__price.get())
        fine = float(self.__fine.get())

        if title == '' or number == '' or date == '' or amount == '':
            self.__show_warning()
            return
        
        data = to_json(title, 'Газета', amount, price, fine,
                       number = number,
                       date = date)

        with open(DATA_PATH + 'material.json', 'w', encoding = 'utf-8') as file:
            json.dump(data, file, indent = 4, ensure_ascii = False)

    # save magazine data
    def __save_magazine_data(self) -> None:
        title = self.__title.get()
        number = self.__number.get()
        date = self.__date.get()
        publisher = self.__publisher.get()
        amount = int(self.__amount.get())
        price = float(self.__price.get())
        fine = float(self.__fine.get())

        if title == '' or number == '' or date == '' or publisher == '' or amount == '':
            self.__show_warning()
            return
        
        data = to_json(title, 'Журнал', amount, price, fine, 
                       number = number, date = date, publisher = publisher)
        
        with open(DATA_PATH + 'material.json', 'w', encoding = 'utf-8') as file:
            json.dump(data, file, indent = 4, ensure_ascii = False)