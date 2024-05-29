from windows.addWindows.baseAddWindow import BaseAddWindow
import customtkinter as ctk
from tkinter import Misc
from settings import *
import json
from convert_to_json import material_to_json
from dll.database import insertIntoMaterials, selectAllMaterials


class AddBookWindow(BaseAddWindow):
    def __init__(self, parent: Misc) -> None:
        super().__init__(parent)

        self.title('Добавить книгу')
        self.geometry('500x700')
        self.resizable(False, False)
        
        self.__authors = ctk.CTkEntry(self, placeholder_text = 'Автор(ы)', font = ENTRY_FONT)
        self.__publisher = ctk.CTkEntry(self, placeholder_text = 'Издательство', font = ENTRY_FONT)
        self.__publishYear = ctk.CTkEntry(self, placeholder_text = 'Год издания', font = ENTRY_FONT)

        self._saveBtn.configure(command = self.__save)

        self.__createLayout()

    # show widgets on the screen
    def __createLayout(self) -> None:
        self._create_base_layout_start()

        self.__authors.pack(fill = 'x', padx = 5, pady = 5)
        self.__publisher.pack(fill = 'x', padx = 5, pady = 5)
        self.__publishYear.pack(fill = 'x', padx = 5, pady = 5)

        self._create_base_layout_end()

    # save the data to the database
    def __save(self) -> None:
        title: str = self._title.get()
        authors: list[str] = self.__authors.get().split(', ')
        publisher: str = self.__publisher.get()
        publish_year: int = -1 if self.__publishYear.get() == '' else int(self.__publishYear.get())
        amount: int = -1 if self._amount.get() == '' else int(self._amount.get())
        fine: float = -1 if self._fine.get() == '' else round(float(self._fine.get()), 2)
        image_path: str = MATERIALS_PICTURE_PATH + self._imageName


        if title == '' or authors == '' or publisher == '' or publish_year == -1 or amount == -1 or fine == -1:
            self._show_warning()
            return

        data: dict = material_to_json(title, 'Книга', amount, fine, image_path,
                authors = authors, 
                publisher = publisher,
                publish_year = publish_year)
        
        with open(DATA_PATH + 'material.json', 'w', encoding = 'utf-8') as file:
            json.dump(data, file, indent = 4, ensure_ascii = False)

        # insert data
        insertIntoMaterials()

        self._show_success()

        # receive data from database
        selectAllMaterials()

        # redraw mainframe
        self._parent.redraw_mainframe()

