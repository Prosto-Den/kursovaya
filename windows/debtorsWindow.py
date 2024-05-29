import customtkinter as ctk
import json
from settings import *
from tkinter import Misc


# line with debtors info
class DebtorLine(ctk.CTkFrame):
    def __init__(self, parent: Misc, data: dict) -> None:
        super().__init__(parent)

        self.rowconfigure(0, weight = 1)
        self.columnconfigure((0, 1), weight = 3, uniform = 'a')
        self.columnconfigure(2, weight = 3, uniform = 'a')
        self.columnconfigure((3, 4), weight = 2, uniform = 'a')

        # transform date to comfortable format
        date = data['borrow_date'].split('-')[::-1]
        borrow_date = '/'.join(date)

        self.__nameLbl = ctk.CTkLabel(self, text = data['name'], font = FONT)
        self.__titleLbl = ctk.CTkLabel(self, text = data['title'], font = FONT)
        self.__dateLbl = ctk.CTkLabel(self, text = borrow_date, font = FONT)
        self.__expireLbl = ctk.CTkLabel(self, text = data['expired'], font = FONT)
        self.__fineLbl = ctk.CTkLabel(self, text = round(data['total_fine'], 2), font = FONT)

        self.__create_layout()

    def __create_layout(self) -> None:
        self.__nameLbl.grid(row = 0, column = 0, sticky = 'news')
        self.__titleLbl.grid(row = 0, column = 1, sticky = 'news')
        self.__dateLbl.grid(row = 0, column = 2, sticky = 'news')
        self.__expireLbl.grid(row = 0, column = 3, sticky = 'news')
        self.__fineLbl.grid(row = 0, column = 4, sticky = 'news')


# show info about debtors
class DebtorsWindow(ctk.CTkToplevel):
    def __init__(self, parent: Misc) -> None:
        super().__init__(master = parent)

        self.title('Должники')
        self.resizable(False, False)

        self.__title = ctk.CTkFrame(self)
        self.__frame = ctk.CTkScrollableFrame(self, fg_color = 'white')

        self.__create_title_layout()
        self.__create_frame_layout()

        self.__title.pack(fill = 'x')
        self.__frame.pack(fill = 'both')

    def __create_title_layout(self) -> None:
        self.__title.rowconfigure(0, weight = 1)
        self.__title.columnconfigure((0, 1), weight = 3, uniform = 'a')
        self.__title.columnconfigure(2, weight = 3, uniform = 'a')
        self.__title.columnconfigure((3, 4), weight = 2, uniform = 'a')

        ctk.CTkLabel(self.__title, text = 'Имя', font = FONT).grid(row = 0, column = 0)
        ctk.CTkLabel(self.__title, text = 'Название', font = FONT).grid(row = 0, column = 1)
        ctk.CTkLabel(self.__title, text = 'Дата выдачи', font = FONT).grid(row = 0, column = 2)
        ctk.CTkLabel(self.__title, text = 'Просрочено', font = FONT).grid(row = 0, column = 3)
        ctk.CTkLabel(self.__title, text = 'Штраф', font = FONT).grid(row = 0, column = 4)

    def __create_frame_layout(self) -> None:
        with open('./temp/selectAllDebtors.json', encoding = 'utf-8') as file:
            data = json.load(file)

        if data is not None:
            data = dict(data)

            for _, value in data.items():
                DebtorLine(self.__frame, value).pack(fill = 'x')

        else:
            ctk.CTkLabel(self.__frame, text = 'Должников нет :)', font = FONT).pack(fill = 'x')