import customtkinter as ctk
import json
from settings import *
from convert_to_json import client_to_json
from CTkMessagebox import CTkMessagebox
from dll.database import insertClient, selectAllClients
from tkinter import Misc


# window for adding new client
class AddClientWindow(ctk.CTkToplevel):
    def __init__(self, parent: Misc) -> None:
        super().__init__(master = parent)

        self.title('Добавить читателя')
        self.geometry('350x160')

        self.__nameEntry = ctk.CTkEntry(self,
                                        placeholder_text = 'ФИО',
                                        font = ENTRY_FONT)
        
        self.__birthDayEntry = ctk.CTkEntry(self, 
                                            placeholder_text = 'Дата рождения',
                                            font = ENTRY_FONT)
        
        self.__passportEntry = ctk.CTkEntry(self,
                                            placeholder_text = 'Паспортные данные',
                                            font = ENTRY_FONT)
        
        self.__saveBtn = ctk.CTkButton(self, text = 'Сохранить', font = FONT,
                                       fg_color = BTN_COLOUR,
                                       text_color = BTN_TEXT_COLOUR,
                                       hover_color = HOVER_BTN_COLOUR,
                                       command = self.__save)

        self.__create_layout()
    
    def __show_warning(self) -> None:
        CTkMessagebox(self, 
                          title = 'Внимание',
                          message = 'Необходимо заполнить все поля',
                          icon = 'cancel',
                          option_1 = 'OK',
                          font = FONT)
    
    def _show_success(self) -> None:
        message = CTkMessagebox(self, 
                      title = 'Успешно!',
                      message = 'Читатель успешно добавлен!',
                      icon = 'check',
                      font = FONT)
        
        if message.get() == 'OK':
            self.destroy()

    def __create_layout(self) -> None:
        self.__nameEntry.pack(fill = 'x', padx = 5, pady = 5)
        self.__birthDayEntry.pack(fill = 'x', padx = 5, pady = 5)
        self.__passportEntry.pack(fill = 'x', padx = 5, pady = 5)
        self.__saveBtn.pack(fill = 'x', padx = 5, pady = 5)


    def __save(self) -> None:
        name: str = self.__nameEntry.get()
        birthday: str = self.__birthDayEntry.get()
        passport: str = self.__passportEntry.get()

        if name == '' or birthday == '' or passport == '':
            self.__show_warning()

            return
        
        data: dict = client_to_json(name, birthday, passport)

        with open('./temp/client.json', 'w', encoding = 'utf-8') as file:
            json.dump(data, file, ensure_ascii = False, indent = 4)

        insertClient()

        self._show_success()

        selectAllClients()

