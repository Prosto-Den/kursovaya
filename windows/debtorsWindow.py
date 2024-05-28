import customtkinter as ctk
from settings import *


class DebtorsWindow(ctk.CTkToplevel):
    def __init__(self, parent):
        super().__init__(master = parent)

        self.__title = ctk.CTkFrame(self)

        self.__create_title_layout()

        self.__title.pack()

    def __create_title_layout(self):
        self.__title.rowconfigure(0, weight = 1)
        self.__title.columnconfigure((0, 1), weight = 2, uniform = 'a')
        self.__title.columnconfigure(2, weight = 3, uniform = 'a')
        self.__title.columnconfigure((3, 4), weight = 2, uniform = 'a')

        ctk.CTkLabel(self.__title, text = 'Имя', font = FONT).grid(row = 0, column = 0)
        ctk.CTkLabel(self.__title, text = 'Название', font = FONT).grid(row = 0, column = 1)
        ctk.CTkLabel(self.__title, text = 'Дата выдачи', font = FONT).grid(row = 0, column = 2)
        ctk.CTkLabel(self.__title, text = 'Просрочено', font = FONT).grid(row = 0, column = 3)
        ctk.CTkLabel(self.__title, text = 'Штраф', font = FONT).grid(row = 0, column = 4)