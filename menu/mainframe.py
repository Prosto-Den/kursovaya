import customtkinter as ctk
import json
import os
from menu.cell import Cell
from tkinter import Misc
from settings import SELECT_ALL_MATERIALS_PATH


class MainFrame(ctk.CTkScrollableFrame):
    def __init__(self, parent: Misc):
        super().__init__(parent, fg_color = 'white')

        self.__parent = parent

        columns = 3
        
        # если файл не пустой, открываем его
        with open('./temp/selectAllMaterials.json', encoding = 'utf-8') as file:
            data = json.load(file)
        
        data = dict(data) if data is not None else dict()

        if len(data) == 0:
            rows = 1

        elif len(data) % columns == 0:
            rows = len(data) // columns

        else:
            rows = len(data) // columns + 1

        rowIndex = tuple(i for i in range(rows))
        self.__columnIndex = tuple(i for i in range(columns))

        self.rowconfigure(rowIndex,
                          weight = 1, uniform = 'a')
        
        self.columnconfigure(self.__columnIndex, weight = 1, uniform = 'a')

        self.__create_layout(data)

    def __create_layout(self, data: dict):
        row = 0
        column = 0
        types = list()

        if self.__parent.bookVar.get():
            types.append('Книга')

        if self.__parent.newsVar.get():
            types.append('Газета')

        if self.__parent.magazineVar.get():
            types.append('Журнал')

        for item in data:
            if (len(self.__parent.searchVar.get()) == 0 or self.__parent.searchVar.get() in data[item]['title']) and \
                data[item]['type'] in types:
                Cell(self, item).grid(row = row, column = column, pady = 5)

                column += 1

                if column not in self.__columnIndex:
                    column = 0
                    row += 1

    def redraw_mainframe(self):
        self.__parent.redraw_mainframe()
