import customtkinter as ctk
from settings import *
from CTkMessagebox import CTkMessagebox
from dll.database import selectAllMaterials, deleteMaterial
from tkinter import Misc


# базовая рамка
class BaseInfoFrame(ctk.CTkFrame):
    def __init__(self, parent: Misc, data: dict) -> None:
        super().__init__(parent, fg_color = 'white')

        self._parent: Misc = parent

        rows = len(data) + len(data['info']) - 6

        rowIndex = tuple(i for i in range(rows))

        self.rowconfigure(rowIndex, weight = 1, uniform = 'a')
        self.columnconfigure((0, 1, 2, 3), weight = 1, uniform = 'a')

        # переменные для хранения информации
        self._titleVar = ctk.StringVar(self, data['title'])
        self._amountVar = ctk.StringVar(self, data['amount'])
        self._fineVar = ctk.StringVar(self, round(data['fine'], 2))
        self._roomVar = ctk.StringVar(self, data['room_id'])
        self._rackVar = ctk.StringVar(self, data['rack_id'])
        self._shelfVar = ctk.StringVar(self, data['shelf_id'])

        # поля ввода
        self._title = ctk.CTkEntry(self, textvariable = self._titleVar, font = ENTRY_FONT)
        self._amount = ctk.CTkEntry(self, textvariable = self._amountVar, font = ENTRY_FONT)
        self._fine = ctk.CTkEntry(self, textvariable = self._fineVar, font = ENTRY_FONT)
        self._room = ctk.CTkEntry(self, textvariable = self._roomVar, font = ENTRY_FONT)
        self._rack = ctk.CTkEntry(self, textvariable = self._rackVar, font = ENTRY_FONT)
        self._shelf = ctk.CTkEntry(self, textvariable = self._shelfVar, font = ENTRY_FONT)


        # кнопки
        self._updateBtn = ctk.CTkButton(self, text = 'Обновить', 
                                        font = FONT,
                                        text_color = BTN_TEXT_COLOUR,
                                        fg_color = BTN_COLOUR,
                                        hover_color = HOVER_BTN_COLOUR)
        
        self._deleteBtn = ctk.CTkButton(self, text = 'Удалить',
                                        font = FONT,
                                        text_color = DELETE_BTN_TEXT_COLOUR,
                                        fg_color = BTN_COLOUR,
                                        hover_color = HOVER_BTN_COLOUR,
                                        command = lambda: self._delete(data))
    
    # для удаления элемента из бд
    def _delete(self, data: dict) -> None:
        id = data['id']

        message = CTkMessagebox(self._parent, title = f'Удалить {data["title"]}?',
                                message = 'Вы уверены, что хотите удалить материал из базы данных? Отменить действие будет невозможно!',
                                option_1 = 'Да',
                                option_2 = 'Нет',
                                icon = 'warning')
        
        if message.get() == 'Да':
            deleteMaterial(id)

            selectAllMaterials()

            self._parent.redraw_mainframe()

            self._parent.destroy()