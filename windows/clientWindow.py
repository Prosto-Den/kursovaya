import customtkinter as ctk
import json
from settings import *
from PIL import Image, ImageTk
from CTkMessagebox import CTkMessagebox
from dll import deleteClient, selectAllClients
from tkinter import Misc


class ClientLine(ctk.CTkFrame):
    def __init__(self, parent: Misc, data: dict):
        super().__init__(master = parent)

        self.__parent = parent

        self.rowconfigure(0, weight = 1)
        self.columnconfigure(0, weight = 1)
        self.columnconfigure(1, weight = 4, uniform = 'b')
        self.columnconfigure((2, 3), weight = 3, uniform = 'b')
        self.columnconfigure(4, weight = 2, uniform = 'b')

        date = data['birthday'].split('-')[::-1]

        birthday = '/'.join(date)

        self.__id: int = data['id']
        self.__idLbl = ctk.CTkLabel(self, text = data['id'], font = FONT)
        self.__nameLbl = ctk.CTkLabel(self, text = data['name'], font = FONT)
        self.__birthdayLbl = ctk.CTkLabel(self, text = birthday, font = FONT)
        self.__passportLbl = ctk.CTkLabel(self, text = data['passport'], font = FONT)

        self.__create_layout()

    def __create_layout(self):
        edit = Image.open('./pictures/edit.png')
        delete = Image.open('./pictures/delete.png')

        edit_image = ImageTk.PhotoImage(edit)
        delete_image = ImageTk.PhotoImage(delete)

        self.__idLbl.grid(row = 0, column = 0, sticky = 'w', ipady = 2)
        self.__nameLbl.grid(row = 0, column = 1, sticky = 'we', padx = [5, 0], ipady = 2)
        self.__birthdayLbl.grid(row = 0, column = 2, sticky = 'nsew', padx = [5, 0], ipady = 2)
        self.__passportLbl.grid(row = 0, column = 3, sticky = 'nsew', padx = [5, 0], ipady = 2)

        ctk.CTkButton(self, image = delete_image, 
                      text = '', width = 20,
                      fg_color = BTN_COLOUR,
                      hover_color = HOVER_BTN_COLOUR,
                      command = self.__delete).grid(row = 0, column = 4, sticky = 'ew')

    def __delete(self):
        message = CTkMessagebox(self, title = f'Удалить {self.__nameLbl._text}?',
                                message = 'Вы уверены, что хотите удалить читателя из базы данных? Отменить действие будет невозможно!',
                                option_1 = 'Да',
                                option_2 = 'Нет',
                                icon = 'warning')
        
        if message.get() == 'Да':
            deleteClient(self.__id)

            selectAllClients()

            self.__parent.master.master.master.redraw()


class ClientsWindow(ctk.CTkToplevel):
    def __init__(self, parent) -> None:
        super().__init__(master = parent)

        self.geometry('600x300')
        self.title('Читатели')
        self.resizable(False, False)

        with open(DATA_PATH + 'selectAllClients.json', encoding = 'utf-8') as file:
            self.__data = dict(json.load(file))

        self.__title = ctk.CTkFrame(self)
        self.__list = ctk.CTkScrollableFrame(self, fg_color = 'white')

        self.__create_title_layout()
        self.__create_list_layout()

        self.__title.pack(fill = 'both')
        self.__list.pack(expand = True, fill = 'both')

    def __create_title_layout(self):
        self.__title.rowconfigure(0, weight = 1)
        self.__title.columnconfigure(0, weight = 1)
        self.__title.columnconfigure(1, weight = 4, uniform = 'b')
        self.__title.columnconfigure((2, 3), weight = 3, uniform = 'b')
        self.__title.columnconfigure(4, weight = 2, uniform = 'b')

        ctk.CTkLabel(self.__title, text = 'ID', font = FONT).grid(row = 0, column = 0, sticky = 'w', padx = 5)
        ctk.CTkLabel(self.__title, text = 'Имя', font = FONT).grid(row = 0, column = 1, sticky = 'we')
        ctk.CTkLabel(self.__title, text = 'Дата рождения', font = FONT).grid(row = 0, column = 2, sticky = 'news')
        ctk.CTkLabel(self.__title, text = 'Паспорт', font = FONT).grid(row = 0, column = 3, sticky = 'news')
        ctk.CTkLabel(self.__title, text = 'Опции', font = FONT).grid(row = 0, column = 4, sticky = 'ew', padx = [0, 8])

    def __create_list_layout(self):
        for item in self.__data:
            ClientLine(self.__list, self.__data[item]).pack(fill = 'x')

    def redraw(self):
        self.__title.pack_forget()
        self.__list.pack_forget()

        self.__title = ctk.CTkFrame(self)
        self.__list = ctk.CTkScrollableFrame(self, fg_color = 'white')

        with open('./temp/selectAllClients.json', encoding = 'utf-8') as file:
            self.__data = dict(json.load(file))

        self.__create_title_layout()
        self.__create_list_layout()

        self.__title.pack(fill = 'both')
        self.__list.pack(expand = True, fill = 'both')