import customtkinter as ctk
from tkinter import Misc
import json
from menu.cell import Cell


class MainFrame(ctk.CTkScrollableFrame):
    def __init__(self, parent):
        super().__init__(parent, fg_color = 'white')

        with open('./temp/selectAllMaterials.json', encoding = 'utf-8') as file:
            self.__data = dict(json.load(file))

        columns = 3
        rows = self.__data.__len__() // columns if self.__data.__len__() % columns == 0 else self.__data.__len__() // columns + 1

        self.__rowIndex = tuple(i for i in range(rows))
        self.__columnIndex = tuple(i for i in range(columns))

        self.rowconfigure(self.__rowIndex,
                          weight = 1, uniform = 'a')
        
        self.columnconfigure(self.__columnIndex, weight = 1, uniform = 'a')

        self.__create_layout()


    def __create_layout(self):
        row = 0
        column = 0

        for item in self.__data:
            Cell(self, self.__data[item]).grid(row = row, column = column, pady = 5)

            column += 1

            if column not in self.__columnIndex:
                column = 0
                row += 1

    def redraw_layout(self):
        with open('./temp/selectAllMaterials.json', encoding = 'utf-8') as file:
            data = dict(json.load(file))

        if data == self.__data:
            print('no changes')
            return
        else:
            self.place_forget()

            self.__data = data

            self.place(relx = 0, rely = 0.2, relwidth = 1, relheight = 0.8)
