from windows.baseAddWindow import BaseAddWindow
import customtkinter as ctk
from settings import *
from convert_to_json import to_json
import json

class AddMagazineWindow(BaseAddWindow):
    def __init__(self):
        super().__init__()

        self.title('Добавить журнал')
        self.geometry('500x670')
        self.resizable(False, False)

        self.__number = ctk.CTkEntry(self, placeholder_text = 'Номер выпуска', font = ENTRY_FONT)
        self.__date = ctk.CTkEntry(self, placeholder_text = 'Дата выпуска', font = ENTRY_FONT)
        self.__publisher = ctk.CTkEntry(self, placeholder_text = 'Издательство', font = ENTRY_FONT)

        self.__create_layout()
    
    def __create_layout(self):
        self._create_base_layout_start()

        self.__number.pack(fill = 'x', padx = 5, pady = 5)
        self.__date.pack(fill = 'x', padx = 5, pady = 5)
        self.__publisher.pack(fill = 'x', padx = 5, pady = 5)

        self._create_base_layout_end()

    def __save(self):
        title: str = self._title.get()
        number: int = -1 if self.__number.get() == '' else int(self.__number.get())
        date: str = self.__date.get()
        publisher = self.__publisher.get()
        amount: int = -1 if self._amount.get() == '' else int(self._amount.get())
        price: float = -1 if self._price.get() == '' else float(self._price.get())
        fine: float = -1 if self._fine.get() == '' else float(self._fine.get())
        image_path: str = MATERIALS_PICTURE_PATH + self.__picture_name

        if title == '' or number == -1 or date == '' or publisher == '' or amount == -1 or price == -1 or fine == -1:
            self._show_warning()
            return
        
        data = to_json(title, 'Журнал', amount, price, fine, image_path, 
                       number = number, date = date, publisher = publisher)
        
        with open(DATA_PATH + 'material.json', 'w', encoding = 'utf-8') as file:
            json.dump(data, file, indent = 4, ensure_ascii = False)