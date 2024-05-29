from windows.addWindows.baseAddWindow import BaseAddWindow
import customtkinter as ctk
from tkinter import Misc
from settings import *
from convert_to_json import material_to_json
import json
from dll.database import insertIntoMaterials, selectAllMaterials


class AddNewsPaperWindow(BaseAddWindow):
    def __init__(self, parent: Misc) -> None:
        super().__init__(parent)

        self.title('Добавить газету')
        self.geometry('500x640')
        self.resizable(False, False)

        self.__number = ctk.CTkEntry(self, placeholder_text = 'Номер выпуска', font = ENTRY_FONT)
        self.__date = ctk.CTkEntry(self, placeholder_text = 'Дата выпуска', font = ENTRY_FONT)

        self._saveBtn.configure(command = self.__save)

        self.__create_layout()

    def __create_layout(self) -> None:
        self._create_base_layout_start()

        self.__number.pack(fill = 'x', padx = 5, pady = 5)
        self.__date.pack(fill = 'x', padx = 5, pady = 5)

        self._create_base_layout_end()

    # save data to the database
    def __save(self) -> None:
        title: str = self._title.get()
        number: int = -1 if self.__number.get() == '' else int(self.__number.get())
        date: str = self.__date.get()
        amount: int = -1 if self._amount.get() == '' else int(self._amount.get())
        fine: float = -1 if self._fine.get() == '' else float(self._fine.get())
        image_path: str = MATERIALS_PICTURE_PATH + self._imageName

        if title == '' or number == -1 or date == '' or amount == -1 or fine == -1:
            self._show_warning()
            return
        
        data: dict = material_to_json(title, 'Газета', amount, fine, image_path,
                       number = number,
                       date = date)

        with open(DATA_PATH + 'material.json', 'w', encoding = 'utf-8') as file:
            json.dump(data, file, indent = 4, ensure_ascii = False)

        # insert data to the database
        insertIntoMaterials()

        self._show_success()

        # receive all item from the database
        selectAllMaterials()

        # update the mainframe
        self._parent.redraw_mainframe()
