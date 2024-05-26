import customtkinter as ctk
from settings import *
from CTkMessagebox import CTkMessagebox
from dll.database import selectAllMaterials, deleteMaterial


# базовая рамка
class BaseInfoFrame(ctk.CTkFrame):
    def __init__(self, parent, data: dict) -> None:
        super().__init__(parent, fg_color = 'white')

        self._parent = parent

        rows = data.__len__() + data['info'].__len__() - 3

        rowIndex = tuple(i for i in range(rows))

        self.rowconfigure(rowIndex, weight = 1, uniform = 'a')
        self.columnconfigure((0, 1), weight = 1, uniform = 'a')

        # переменные для хранения информации
        self._titleVar = ctk.StringVar(self, data['title'])
        self._amountVar = ctk.StringVar(self, data['amount'])
        self._priceVar = ctk.StringVar(self, round(data['price'], 2))
        self._fineVar = ctk.StringVar(self, round(data['fine'], 2))

        # поля ввода
        self._title = ctk.CTkEntry(self, textvariable = self._titleVar, font = ENTRY_FONT)
        self._amount = ctk.CTkEntry(self, textvariable = self._amountVar, font = ENTRY_FONT)
        self._price = ctk.CTkEntry(self, textvariable = self._priceVar, font = ENTRY_FONT)
        self._fine = ctk.CTkEntry(self, textvariable = self._fineVar, font = ENTRY_FONT)

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
    
    # для удаления элемента их бд
    def _delete(self, data: dict):
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