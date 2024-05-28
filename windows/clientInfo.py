import customtkinter as ctk
import re
from settings import *
from CTkMessagebox import CTkMessagebox


class InfoClient(ctk.CTkToplevel):
    def __init__(self, parent, data: dict):
        super().__init__(master = parent)

        self.title(data['name'])
        self.geometry('300x300')

        self.rowconfigure((0, 1, 2, 3), weight = 1, uniform = 'a')
        self.columnconfigure((0, 1), weight = 1, uniform = 'a')

        birthday = data['birthday'].split('-')[::-1]

        self.__nameVar = ctk.StringVar(self, value = data['name'])
        self.__birthdayVar = ctk.StringVar(self, value = '/'.join(birthday))
        self.__passportVar = ctk.StringVar(self, value = data['passport'])

        self.__id = data['id']
        self.__nameEntry = ctk.CTkEntry(self, textvariable = self.__nameVar, font = ENTRY_FONT)
        self.__birthdayEntry = ctk.CTkEntry(self, textvariable = self.__birthdayVar, font = FONT)
        self.__passportEntry = ctk.CTkEntry(self, textvariable = self.__passportVar, font = ENTRY_FONT)

        self.__create_layout()

    def __create_layout(self):
        ctk.CTkLabel(self, text = 'ФИО', font = FONT).grid(row = 0, column = 0, sticky = 'ew', padx = 5, pady = 5)
        ctk.CTkLabel(self, text = 'Дата рождения', font = FONT).grid(row = 1, column = 0, sticky = 'ew', padx = 5, pady = 5)
        ctk.CTkLabel(self, text = 'Номер паспорта', font = FONT).grid(row = 2, column = 0, sticky = 'ew', padx = 5, pady = 5)

        self.__nameEntry.grid(row = 0, column = 1, sticky = 'ew', padx = 5, pady = 5)
        self.__birthdayEntry.grid(row = 1, column = 1, sticky = 'ew', padx = 5, pady = 5)
        self.__passportEntry.grid(row = 2, column = 1, sticky = 'ew', padx = 5, pady = 5)

        ctk.CTkButton(self, text = 'Обновить', font = FONT, 
                      fg_color = BTN_COLOUR, text_color = BTN_TEXT_COLOUR,
                      hover_color = HOVER_BTN_COLOUR, command = self.__update).grid(row = 3, column = 0, sticky = 'news', padx = 5, pady = 5)
        
        ctk.CTkButton(self, text = 'Удалить', font = FONT, 
                      fg_color = BTN_COLOUR, text_color = DELETE_BTN_TEXT_COLOUR,
                      hover_color = HOVER_BTN_COLOUR).grid(row = 3, column = 1, sticky = 'news', padx = 5, pady = 5)
        
    def __update(self):
        name: str = self.__nameVar.get()
        birthday: str = self.__birthdayVar.get()
        passport: str = self.__passportVar.get()
        error_flag: bool = False

        if name == '' or birthday == '' or passport == '':
            CTkMessagebox(self, 
                          title = 'Внимание',
                          message = 'Необходимо заполнить все поля',
                          icon = 'cancel',
                          option_1 = 'OK',
                          font = FONT)
            return

        if not re.match(r'\d{2}/\d{2}/\d{4}', birthday) or not len(birthday) == 10:
            CTkMessagebox(self, 
                          title = 'Внимание',
                          message = 'В поле "Дата рождения" введено недопустимое значение',
                          icon = 'cancel',
                          option_1 = 'OK',
                          font = FONT)
            
            error_flag = True
            
        if not re.match(r'\d{4} \d{8}', passport) or not len(passport) == 11:
            CTkMessagebox(self, 
                          title = 'Внимание',
                          message = 'В поле "Паспорт" введено недопустимое значение',
                          icon = 'cancel',
                          option_1 = 'OK',
                          font = FONT)
            
            error_flag = True

        if error_flag:
            return
        

