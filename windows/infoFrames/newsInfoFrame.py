from windows.infoFrames.baseInfoFrame import BaseInfoFrame
from settings import *
from dll.database import selectAllMaterials, updateMaterial
from convert_to_json import material_to_json
from CTkMessagebox import CTkMessagebox
import customtkinter as ctk
import json


# рамка для информации о газете
class NewsPaperInfoFrame(BaseInfoFrame):
    def __init__(self, parent, data: dict) -> None:
        super().__init__(parent, data)

        self.__numberVar = ctk.StringVar(self, data['info']['number'])
        self.__dateVar = ctk.StringVar(self, data['info']['date'])

        self.__number = ctk.CTkEntry(self, textvariable = self.__numberVar, font = FONT)
        self.__date = ctk.CTkEntry(self, textvariable = self.__dateVar, font = FONT)

        self._updateBtn.configure(command = lambda: self.__update(data))

        self.__create_layout()
    
    # place the widgets on the frame
    def __create_layout(self):
        ctk.CTkLabel(self, text = 'Название', fg_color = 'white', font = FONT).grid(row = 0, column = 0, pady = 5)
        ctk.CTkLabel(self, text = 'Номер выпуска', fg_color = 'white', font = FONT).grid(row = 1, column = 0, pady = 5)
        ctk.CTkLabel(self, text = 'Дата выпуска', fg_color = 'white', font = FONT).grid(row = 2, column = 0, pady = 5)
        ctk.CTkLabel(self, text = 'Количество', fg_color = 'white', font = FONT).grid(row = 3, column = 0, pady = 5)
        ctk.CTkLabel(self, text = 'Штраф', fg_color = 'white', font = FONT).grid(row = 4, column = 0, pady = 5)

        ctk.CTkLabel(self, text = 'Зал', font = FONT).grid(row = 1, column = 2)
        ctk.CTkLabel(self, text = 'Стеллаж', font = FONT).grid(row = 2, column = 2)
        ctk.CTkLabel(self, text = 'Полка', font = FONT).grid(row = 3, column = 2)

        self._title.grid(row = 0, column = 1, pady = 5, padx = 5, sticky = 'ew')
        self.__number.grid(row = 1, column = 1, pady = 5, padx = 5, sticky = 'ew')
        self.__date.grid(row = 2, column = 1, pady = 5, padx = 5, sticky = 'ew')
        self._amount.grid(row = 3, column = 1, pady = 5, padx = 5, sticky = 'ew')
        self._fine.grid(row = 4, column = 1, pady = 5, padx = 5, sticky = 'ew')

        self._room.grid(row = 1, column = 3, pady = 5, padx = 5, sticky = 'ew')
        self._rack.grid(row = 2, column = 3, pady = 5, padx = 5, sticky = 'ew')
        self._shelf.grid(row = 3, column = 3, pady = 5, padx = 5, sticky = 'ew')

        self._updateBtn.grid(row = 5, column = 0, sticky = 'ew', padx = 5, columnspan = 2)
        self._deleteBtn.grid(row = 5, column = 2, sticky = 'ew', padx = 5, columnspan = 2)

    # update data in the database
    def __update(self, data: dict):
        try:
            id = data['id']
            type = data['type']
            image_path = data['image_path']

            title: str = self._titleVar.get()
            number = int(self.__numberVar.get())
            date: str = self.__dateVar.get()
            amount = int(self._amountVar.get())
            fine = float(self._fineVar.get())

            room = int(self._roomVar.get())
            rack = int(self._rackVar.get())
            shelf = int(self._shelf.get())

            updated_data = material_to_json(id = id, 
                                   title = title, 
                                   type = type, 
                                   amount = amount,  
                                   fine = fine,
                                   image_path = image_path,
                                   room = room,
                                   rack = rack,
                                   shelf = shelf,
                                   number = number,
                                   date = date)

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