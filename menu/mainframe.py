import customtkinter as ctk
import json
from menu.cell import Cell
import os
from settings import SELECT_ALL_MATERIALS_PATH


class MainFrame(ctk.CTkScrollableFrame):
    def __init__(self, parent):
        super().__init__(parent, fg_color = 'white')

        self.__parent = parent

        # если файл не пустой, открываем его
        if os.stat(SELECT_ALL_MATERIALS_PATH).st_size != 0:
            with open('./temp/selectAllMaterials.json', encoding = 'utf-8') as file:
                self.__data = dict(json.load(file))
        else:
            self.__data = dict()

        columns = 3

        if self.__data.__len__() == 0:
            rows = 1
        elif self.__data.__len__() % columns == 0:
            rows = self.__data.__len__() // columns
        else:
            rows = self.__data.__len__() // columns + 1

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

    def redraw_mainframe(self):
        self.__parent.redraw_mainframe()
