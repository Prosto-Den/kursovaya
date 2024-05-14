import customtkinter as ctk
from CTkMessagebox import CTkMessagebox
from settings import *
from tkinter.filedialog import askopenfile
import shutil
from PIL import Image, ImageTk
import os


class AddWindow(ctk.CTkToplevel):
    def __init__(self, type: str):
        super().__init__()

        self.title('Add book')
        self.geometry('400x600')
        self.resizable(False, False)
        self.iconbitmap('./pictures/icon.ico')

        # load default picture
        picture = Image.open('./pictures/books/default.png').resize((300, 300))
        self.__book_image = ImageTk.PhotoImage(picture)
        self.__picture_name = 'default.png'

        # widget for showing the picture
        self.__image = ctk.CTkLabel(self, text = '', image = self.__book_image)

        self.__picture_path = './pictures/books/'

        self.focus()
        self.grab_set()

        self.__create_layout(type)

        self.mainloop()

    def __init_book_window(self):
        # entry widgets
        self.__title = ctk.CTkEntry(self, placeholder_text = 'Название', font = ENTRY_FONT)
        self.__authors = ctk.CTkEntry(self, placeholder_text = 'Автор(ы)', font = ENTRY_FONT)
        self.__publisher = ctk.CTkEntry(self, placeholder_text = 'Издательство', font = ENTRY_FONT)
        self.__publish_year = ctk.CTkEntry(self, placeholder_text = 'Год издания', font = ENTRY_FONT)
        self.__amount = ctk.CTkEntry(self, placeholder_text = 'Количество', font = ENTRY_FONT)

    def __create_book_layout(self):
        self.__init_book_window()

        self.__title.pack(fill = 'x', padx = 5, pady = 5)
        self.__authors.pack(fill = 'x', padx = 5, pady = 5)
        self.__publisher.pack(fill = 'x', padx = 5, pady = 5)
        self.__publish_year.pack(fill = 'x', padx = 5, pady = 5)
        self.__amount.pack(fill = 'x', padx = 5, pady = 5)

        ctk.CTkButton(self, 
                  text = 'Сохранить', 
                  font = FONT,
                  text_color = BTN_TEXT_COLOUR,
                  fg_color = BTN_COLOUR,
                  hover_color = HOVER_BTN_COLOUR, 
                  command = self.__save_book_data).pack(pady = 10)

    def __create_layout(self, type: str) -> None:
        self.__image.pack(pady = 5)

        ctk.CTkButton(self, 
                  text = 'Выбрать изображение', 
                  font = FONT,
                  text_color = BTN_TEXT_COLOUR,
                  fg_color = BTN_COLOUR,
                  hover_color = HOVER_BTN_COLOUR, 
                  command = self.__select_image).pack(pady = 5)
        
        if type == 'Книгу':
            self.__create_book_layout()


    # select image for the book
    def __select_image(self):
        file_path = askopenfile(filetypes = [('JPG files', ['*jpeg', '*jpg']), ('PNG files', '*png'), ('Image files', ['*jpg', '*jpeg', '*png'])])

        if file_path is None:
            return
        else:
            self.__picture_name = file_path.name.split('/')[-1]

            # если файл с таким названием уже есть в папке - спрашиваем, нужно ли его копировать
            if self.__picture_name in os.listdir(self.__picture_path):

                message = CTkMessagebox(self, title = 'Внимание',
                                        message = 'Файл с таким названием уже есть в папке. Заменить его?',
                                        option_1 = 'Да',
                                        option_2 = 'Нет',
                                        icon = 'warning')
                
                if message.get() == 'Да':
                    shutil.copy(file_path.name, self.__picture_path)

            else:
                shutil.copy(file_path.name, self.__picture_path)

            path = self.__picture_path + self.__picture_name

            image = Image.open(path).resize((300, 300))
            self.__book_image = ImageTk.PhotoImage(image)

            self.__image.configure(image = self.__book_image)

    def __save_book_data(self):
        title = self.__title.get()
        authors = self.__authors.get().split(',')
        publisher = self.__publisher.get()
        publish_year = self.__publish_year.get()
        amount = self.__amount.get()

        if title == '' or authors == '' or publisher == '' or publish_year == 0 or amount == '':
            CTkMessagebox(self, 
                          title = 'Внимание',
                          message = 'Необходимо заполнить все поля',
                          icon = 'cancel',
                          option_1 = 'Закрыть',
                          font = FONT)
            return

        print(self.__picture_path + self.__picture_name)
        print(title)
        print(authors)
        print(publisher)
        print(publish_year)
        print(amount)