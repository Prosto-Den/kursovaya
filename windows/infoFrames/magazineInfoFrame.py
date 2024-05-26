from windows.infoFrames.baseInfoFrame import BaseInfoFrame
from settings import *
from convert_to_json import material_to_json
from dll.database import selectAllMaterials, updateMaterial
from CTkMessagebox import CTkMessagebox
import customtkinter as ctk
import json


# рамка для вывода информации о журнале
class MagazineInfoFrame(BaseInfoFrame):
    def __init__(self, parent, data: dict):
        super().__init__(parent, data)

        self.__numberVar = ctk.StringVar(self, data['info']['number'])
        self.__dateVar = ctk.StringVar(self, data['info']['date'])
        self.__publisherVar = ctk.StringVar(self, value = data['info']['publisher'])

        self.__number = ctk.CTkEntry(self, textvariable = self.__numberVar, font = FONT)
        self.__date = ctk.CTkEntry(self, textvariable = self.__dateVar, font = FONT)
        self.__publisher = ctk.CTkEntry(self, textvariable = self.__publisherVar, font = ENTRY_FONT)

        self._updateBtn.configure(command = lambda: self.__update(data))

        self.__create_layout()

    def __create_layout(self):
        ctk.CTkLabel(self, text = 'Название', fg_color = 'white', font = FONT).grid(row = 0, column = 0, pady = 5)
        ctk.CTkLabel(self, text = 'Номер выпуска', fg_color = 'white', font = FONT).grid(row = 1, column = 0, pady = 5)
        ctk.CTkLabel(self, text = 'Дата выпуска', fg_color = 'white', font = FONT).grid(row = 2, column = 0, pady = 5)
        ctk.CTkLabel(self, text = 'Издательство', fg_color = 'white', font = FONT).grid(row = 3, column = 0, pady = 5)
        ctk.CTkLabel(self, text = 'Количество', fg_color = 'white', font = FONT).grid(row = 4, column = 0, pady = 5)
        ctk.CTkLabel(self, text = 'Цена', fg_color = 'white', font = FONT).grid(row = 5, column = 0, pady = 5)
        ctk.CTkLabel(self, text = 'Штраф', fg_color = 'white', font = FONT).grid(row = 6, column = 0, pady = 5)

        self._title.grid(row = 0, column = 1, pady = 5, padx = 5, sticky = 'ew')
        self.__number.grid(row = 1, column = 1, pady = 5, padx = 5, sticky = 'ew')
        self.__date.grid(row = 3, column = 1, pady = 5, padx = 5, sticky = 'ew')
        self.__publisher.grid(row = 2, column = 1, pady = 5, padx = 5, sticky = 'ew')
        self._amount.grid(row = 4, column = 1, pady = 5, padx = 5, sticky = 'ew')
        self._price.grid(row = 5, column = 1, pady = 5, padx = 5, sticky = 'ew')
        self._fine.grid(row = 6, column = 1, pady = 5, padx = 5, sticky = 'ew')

        self._updateBtn.grid(row = 7, column = 0, sticky = 'ew', padx = 5)
        self._deleteBtn.grid(row = 7, column = 1, sticky = 'ew', padx = 5)

    def __update(self, data: dict):
        try:
            id = data['id']
            type = data['type']
            image_path = data['image_path']

            title = self._titleVar.get() if self._title.get() != '' else data['title']
            number = int(self.__numberVar.get())
            date = self.__dateVar.get() if self.__dateVar.get() != '' else data['info']['date']
            publisher = self.__publisher.get() if self.__publisher.get() != '' else data['info']['publisher']
            amount = int(self._amountVar.get())
            price = float(self._priceVar.get())
            fine = float(self._fineVar.get())

            updated_data = material_to_json(id = id, 
                                   title = title, 
                                   type = type, 
                                   amount = amount, 
                                   price = price, 
                                   fine = fine,
                                   image_path = image_path,
                                   number = number,
                                   date = date,
                                   publisher = publisher)

            with open(DATA_PATH + 'material.json', 'w', encoding = 'utf-8') as file:
                json.dump(updated_data, file, ensure_ascii = False, indent = 4)

            updateMaterial()

            selectAllMaterials()

            self._parent.redraw_mainframe()

        except ValueError:
            CTkMessagebox(self._parent, 
                          title = 'Ошибка',
                          message = 'В одно из полей введено недопустимое значение',
                          icon = 'cancel')