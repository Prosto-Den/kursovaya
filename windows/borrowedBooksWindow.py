import customtkinter as ctk
import json
import datetime as dt
from tkinter import Misc
from settings import *
from PIL import Image, ImageTk
from dll import deleteBorrow, selectAllClientMaterial, insertIntoDebtors, selectAllDebtors
from CTkMessagebox import CTkMessagebox


class BorrowedLine(ctk.CTkFrame):
    def __init__(self, parent: Misc, data: dict):
        super().__init__(parent)

        self.__parent = parent

        self.rowconfigure(0, weight = 1)
        self.columnconfigure((0, 1), weight = 3, uniform = 'a')
        self.columnconfigure((2, 3), weight = 4, uniform = 'a')
        self.columnconfigure(4, weight = 2, uniform = 'a')

        borrow = data['borrow_date'].split('-')[::-1]
        retrn = data['return_date'].split('-')[::-1]

        borrow_date = '/'.join(borrow)
        return_date = '/'.join(retrn)

        self.__clientID = data['client_id']
        self.__materialID = data['material_id']

        self.__name = ctk.CTkLabel(self, text = data['name'], font = FONT)
        self.__title = ctk.CTkLabel(self, text = data['title'], font = FONT)
        self.__borrowDate = ctk.CTkLabel(self, text = borrow_date, font = FONT)
        self.__returnDate = ctk.CTkLabel(self, text = return_date, font = FONT)

        self.__create_layout()

    def __create_layout(self):
        self.__name.grid(row = 0, column = 0)
        self.__title.grid(row = 0, column = 1)
        self.__borrowDate.grid(row = 0, column = 2)
        self.__returnDate.grid(row = 0, column = 3)

        cross = Image.open('./pictures/cross.png')
        tick = Image.open('./pictures/tick.png')

        cross_image = ImageTk.PhotoImage(cross)
        tick_image = ImageTk.PhotoImage(tick)

        ctk.CTkButton(self, text = '', image = tick_image,
                      fg_color = BTN_COLOUR,
                      hover_color = HOVER_BTN_COLOUR, width = 20, 
                      command = self.__return_book).grid(row = 0, column = 4, sticky = 'w', pady = 2, padx = 2)
        
        ctk.CTkButton(self, text = '', image = cross_image,
                      fg_color = BTN_COLOUR,
                      hover_color = HOVER_BTN_COLOUR, width = 20,
                      command = self.__debt).grid(row = 0, column = 4, sticky = 'e', pady = 2, padx = 2)
        
    def __return_book(self):
        deleteBorrow(self.__materialID, self.__clientID)

        selectAllClientMaterial()

        self.__parent.master.master.master.redraw()

    def __debt(self):
        return_date = dt.datetime.strptime(self.__returnDate._text, '%d/%m/%Y').date()

        if return_date < dt.datetime.now().date():
            insertIntoDebtors(self.__clientID, self.__materialID)

            selectAllDebtors()

        else:
            CTkMessagebox(self.__parent, title = 'Внимание!',
                          message = 'Этот читатель ещё не задолжал книгу',
                          icon = 'warning', sound = True)




class BorrowedBooksWindow(ctk.CTkToplevel):
    def __init__(self, parent: Misc):
        super().__init__(master = parent)
        
        self.title('Взятые книги')
        self.geometry('700x300')

        self.__title = ctk.CTkFrame(self)
        self.__frame = ctk.CTkScrollableFrame(self, fg_color = 'white')

        self.__create_title_layout()
        self.__create_frame_layout()

        self.__title.pack(fill = 'x')
        self.__frame.pack(fill = 'both')

    def __create_title_layout(self):
        self.__title.rowconfigure(0, weight = 1)
        self.__title.columnconfigure((0, 1), weight = 2, uniform = 'a')
        self.__title.columnconfigure((2, 3), weight = 3, uniform = 'a')
        self.__title.columnconfigure(4, weight = 1, uniform = 'a')

        ctk.CTkLabel(self.__title, text = 'ФИО', font = FONT).grid(row = 0, column = 0)
        ctk.CTkLabel(self.__title, text = 'Книга', font = FONT).grid(row = 0, column = 1)
        ctk.CTkLabel(self.__title, text = 'Дата выдачи', font = FONT).grid(row = 0, column = 2)
        ctk.CTkLabel(self.__title, text = 'Дата возврата', font = FONT).grid(row = 0, column = 3)
        ctk.CTkLabel(self.__title, text = 'Опции', font = FONT).grid(row = 0, column = 4)

    def __create_frame_layout(self):
        with open('./temp/selectAllClientMaterial.json', encoding = 'utf-8') as file:
            data = json.load(file)

        if data is not None:
            data = dict(data)

            for _, value in data.items():
                BorrowedLine(self.__frame, value).pack(fill = 'x', pady = 5)

        else:
            ctk.CTkLabel(self.__frame, text = 'Ещё никто не взял книгу :(', font = FONT).pack()

    def redraw(self):
        self.__frame.pack_forget()

        self.__frame = ctk.CTkScrollableFrame(self, fg_color = 'white')

        self.__create_frame_layout()

        self.__frame.pack(fill = 'both')