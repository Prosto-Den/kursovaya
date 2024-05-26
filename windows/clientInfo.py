import customtkinter as ctk
from settings import *


class InfoClient(ctk.CTkToplevel):
    def __init__(self, parent, data: dict):
        super().__init__(master = parent)

        self.title(data['name'])
        self.geometry('300x300')

        self.rowconfigure((0, 1, 2, 3), weight = 1, uniform = 'a')
        self.columnconfigure((0, 1), weight = 1, uniform = 'a')

        birthday = data['birthday'].split('-')[::-1]

        self.__nameVar = ctk.StringVar(self, value = data['name'])
        self.__birthdayVar = ctk.StringVar(self, value = '/'.join(birthday))
        self.__passportVar = ctk.StringVar(self, value = data['passport'])

        self.__id = data['id']
        self.__nameEntry = ctk.CTkEntry(self, textvariable = self.__nameVar, font = ENTRY_FONT)
        self.__birthdayEntry = ctk.CTkEntry(self, textvariable = self.__birthdayVar, font = FONT)
        self.__passportEntry = ctk.CTkEntry(self, textvariable = self.__passportVar, font = ENTRY_FONT)

        self.__create_layout()

    def __create_layout(self):
        ctk.CTkLabel(self, text = 'ФИО', font = FONT).grid(row = 0, column = 0, sticky = 'ew', padx = 5, pady = 5)
        ctk.CTkLabel(self, text = 'Дата рождения', font = FONT).grid(row = 1, column = 0, sticky = 'ew', padx = 5, pady = 5)
        ctk.CTkLabel(self, text = 'Номер паспорта', font = FONT).grid(row = 2, column = 0, sticky = 'ew', padx = 5, pady = 5)

        self.__nameEntry.grid(row = 0, column = 1, sticky = 'ew', padx = 5, pady = 5)
        self.__birthdayEntry.grid(row = 1, column = 1, sticky = 'ew', padx = 5, pady = 5)
        self.__passportEntry.grid(row = 2, column = 1, sticky = 'ew', padx = 5, pady = 5)


