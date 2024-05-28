import customtkinter as ctk
import json
from settings import *
from dll import insertBorrowBook, selectAllClientMaterial, selectAllMaterials


class BorrowWindows(ctk.CTkToplevel):
    def __init__(self, parent):
        super().__init__(master = parent)

        self.title('Выдать книгу')
        self.geometry('400x200')

        materials = []
        clients = []

        with open('./temp/selectAllMaterials.json', encoding = 'utf-8') as file:
            data = dict(json.load(file))

            for _, value in data.items():
                temp = str(value['id']) + ' | ' + value['title']

                materials.append(temp)

        with open('./temp/selectAllClients.json', encoding = 'utf-8') as file:
            data = dict(json.load(file))

            for _, value in data.items():
                temp = str(value['id']) + ' | ' + value['name']

                clients.append(temp)

        self.__frame = ctk.CTkFrame(self)
        self.__btn = ctk.CTkButton(self, text = 'Выдать',
                                   font = FONT,
                                   text_color = BTN_TEXT_COLOUR,
                                   fg_color = BTN_COLOUR,
                                   hover_color = HOVER_BTN_COLOUR,
                                   command = self.__borrow)

        self.__chooseClient = ctk.CTkComboBox(self.__frame, values = clients, 
                                              button_color = BTN_COLOUR,
                                              button_hover_color = HOVER_BTN_COLOUR)

        self.__chooseMaterial = ctk.CTkComboBox(self.__frame, values = materials, 
                                              button_color = BTN_COLOUR,
                                              button_hover_color = HOVER_BTN_COLOUR)

        self.__frame.rowconfigure((0, 1), weight = 1, uniform = 'a')
        self.__frame.columnconfigure((0, 1), weight = 1, uniform = 'a')

        self.__create_frame_layout()

        self.__frame.pack(pady = 5, padx = 5, fill = 'both')
        self.__btn.pack(pady = 5, padx = 5)

    def __create_frame_layout(self):
        ctk.CTkLabel(self.__frame, text = 'Читатель', font = FONT).grid(row = 0, column = 0)
        ctk.CTkLabel(self.__frame, text = 'Материал', font = FONT).grid(row = 1, column = 0)

        self.__chooseClient.grid(row = 0, column = 1, sticky = 'news')
        self.__chooseMaterial.grid(row = 1, column = 1, sticky = 'news')

    def __borrow(self):
        id_client = int(self.__chooseClient.get().split(' | ')[0])
        id_material = int(self.__chooseMaterial.get().split(' | ')[0])

        insertBorrowBook(id_client, id_material)

        selectAllClientMaterial()

        selectAllMaterials()

        
