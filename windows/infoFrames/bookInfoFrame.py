from windows.infoFrames.baseInfoFrame import BaseInfoFrame
from settings import *
from convert_to_json import material_to_json
from dll.database import selectAllMaterials, updateMaterial
from CTkMessagebox import CTkMessagebox
import json
import customtkinter as ctk


# рамка для информации о книге
class BookInfoFrame(BaseInfoFrame):
    def __init__(self, parent, data: dict):
        super().__init__(parent, data)

        authors = ', '.join(data['info']['authors'])

        self.__authorsVar = ctk.StringVar(self, value = authors)
        self.__publisherVar = ctk.StringVar(self, value = data['info']['publisher'])
        self.__publishYearVar = ctk.StringVar(self, value = data['info']['publish_year'])

        self.__authors = ctk.CTkEntry(self, textvariable = self.__authorsVar, font = ENTRY_FONT)
        self.__publisher = ctk.CTkEntry(self, textvariable = self.__publisherVar, font = ENTRY_FONT)
        self.__publishYear = ctk.CTkEntry(self, textvariable = self.__publishYearVar, font = ENTRY_FONT)

        self._updateBtn.configure(command = lambda: self.__update(data))

        self.__create_layout()

    def __create_layout(self):
        ctk.CTkLabel(self, text = 'Название', fg_color = 'white', font = FONT).grid(row = 0, column = 0, pady = 5)
        ctk.CTkLabel(self, text = 'Авторы', fg_color = 'white', font = FONT).grid(row = 1, column = 0, pady = 5)
        ctk.CTkLabel(self, text = 'Издатель', fg_color = 'white', font = FONT).grid(row = 2, column = 0, pady = 5)
        ctk.CTkLabel(self, text = 'Год издания', fg_color = 'white', font = FONT).grid(row = 3, column = 0, pady = 5)
        ctk.CTkLabel(self, text = 'Количество', fg_color = 'white', font = FONT).grid(row = 4, column = 0, pady = 5)
        ctk.CTkLabel(self, text = 'Цена', fg_color = 'white', font = FONT).grid(row = 5, column = 0, pady = 5)
        ctk.CTkLabel(self, text = 'Штраф', fg_color = 'white', font = FONT).grid(row = 6, column = 0, pady = 5)

        # размещаем поля ввода
        self._title.grid(row = 0, column = 1, pady = 5, padx = 5, sticky = 'ew')
        self.__authors.grid(row = 1, column = 1, pady = 5, padx = 5, sticky = 'ew')
        self.__publisher.grid(row = 2, column = 1, pady = 5, padx = 5, sticky = 'ew')
        self.__publishYear.grid(row = 3, column = 1, pady = 5, padx = 5, sticky = 'ew')
        self._amount.grid(row = 4, column = 1, pady = 5, padx = 5, sticky = 'ew')
        self._price.grid(row = 5, column = 1, pady = 5, padx = 5, sticky = 'ew')
        self._fine.grid(row = 6, column = 1, pady = 5, padx = 5, sticky = 'ew')

        # размещаем кнопки
        self._updateBtn.grid(row = 7, column = 0, sticky = 'ew', padx = 5)
        self._deleteBtn.grid(row = 7, column = 1, sticky = 'ew', padx = 5)

    def __update(self, data: dict):
        try:
            id: int = data['id']
            type: str = data['type']
            image_path: str = data['image_path']

            title: str = self._titleVar.get() if self._title.get() != '' else data['title']
            authors: list[str] = self.__authorsVar.get().split(',') if self.__authorsVar.get() != '' else data['info']['authors']
            publisher: str = self.__publisherVar.get() if self.__publisherVar.get() != '' else data['info']['publisher']
            publishYear = int(self.__publishYearVar.get())
            amount = int(self._amountVar.get())
            price = float(self._priceVar.get())
            fine = float(self._fineVar.get())

            updated_data: dict = material_to_json(id = id, 
                                   title = title, 
                                   type = type, 
                                   amount = amount, 
                                   price = price, 
                                   fine = fine,
                                   image_path = image_path,
                                   publisher = publisher,
                                   authors = authors,
                                   publish_year = publishYear)

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