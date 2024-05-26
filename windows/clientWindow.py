import customtkinter as ctk
import json
from settings import *
from windows.clientInfo import InfoClient


class ClientLabel(ctk.CTkLabel):
    def __init__(self, parent, data: dict):
        super().__init__(parent, fg_color = 'white', font = FONT,
                         text = data['name'])
        
        self.bind('<Button-1>', lambda _: InfoClient(parent, data))


class ClientsWindow(ctk.CTkToplevel):
    def __init__(self, parent):
        super().__init__(master = parent)

        self.title('Читатели')
        self.geometry('300x200')

        with open('./temp/selectAllClients.json', encoding = 'utf-8') as file: 
            data = dict(json.load(file))

        rows: int = data.__len__()
        self.__rowIndex = tuple(i for i in range(rows))

        self.rowconfigure(self.__rowIndex, weight = 1, uniform = 'a')
        self.columnconfigure(0, weight = 1, uniform = 'a')

        self.__create_layout(data)

    def __create_layout(self, data: dict):
        index = 0

        for item in data:
            ClientLabel(self, data[item]).grid(row = index, column = 0, pady = 5, padx = 5, sticky = 'nsew')

            index += 1