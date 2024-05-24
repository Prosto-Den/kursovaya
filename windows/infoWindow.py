import customtkinter as ctk
from PIL import Image, ImageTk
from settings import *


# базовая рамка для вывод информации
class BaseInfoFrame(ctk.CTkFrame):
    def __init__(self, parent, data: dict) -> None:
        super().__init__(parent, fg_color = 'white')

        rows = data.__len__() + data['info'].__len__() - 3

        rowIndex = tuple(i for i in range(rows))

        self.rowconfigure(rowIndex, weight = 1, uniform = 'a')
        self.columnconfigure((0, 1), weight = 1, uniform = 'a')

        self.__titleVar = ctk.StringVar(self, data['title'])
        self.__amountVar = ctk.IntVar(self, data['amount'])
        self.__priceVar = ctk.DoubleVar(self, data['price'])
        self.__fineVar = ctk.DoubleVar(self, data['fine'])

        self._title = ctk.CTkEntry(self, textvariable = self.__titleVar, font = ENTRY_FONT)
        self._amount = ctk.CTkEntry(self, textvariable = self.__amountVar, font = ENTRY_FONT)
        self._price = ctk.CTkEntry(self, textvariable = self.__priceVar, font = ENTRY_FONT)
        self._fine = ctk.CTkEntry(self, textvariable = self.__fineVar, font = ENTRY_FONT)

        self._updateBtn = ctk.CTkButton(self, text = 'Обновить', 
                                        font = FONT,
                                        text_color = BTN_TEXT_COLOUR,
                                        fg_color = BTN_COLOUR,
                                        hover_color = HOVER_BTN_COLOUR)
        
        self._deleteBtn = ctk.CTkButton(self, text = 'Удалить',
                                        font = FONT,
                                        text_color = DELETE_BTN_TEXT_COLOUR,
                                        fg_color = BTN_COLOUR,
                                        hover_color = HOVER_BTN_COLOUR)
        

# раска для информации о книге
class BookInfoFrame(BaseInfoFrame):
    def __init__(self, parent, data: dict):
        super().__init__(parent, data)

        authors = ', '.join(data['info']['authors'])

        self.__authorsVar = ctk.StringVar(self, value = authors)
        self.__publisherVar = ctk.StringVar(self, value = data['info']['publisher'])
        self.__publishYearVar = ctk.IntVar(self, value = data['info']['publish_year'])

        self.__authors = ctk.CTkEntry(self, textvariable = self.__authorsVar, font = ENTRY_FONT)
        self.__publisher = ctk.CTkEntry(self, textvariable = self.__publisherVar, font = ENTRY_FONT)
        self.__publishYear = ctk.CTkEntry(self, textvariable = self.__publishYearVar, font = ENTRY_FONT)

        self.__create_layout()

    def __create_layout(self):
        ctk.CTkLabel(self, text = 'Название', fg_color = 'white', font = FONT).grid(row = 0, column = 0, pady = 5)
        ctk.CTkLabel(self, text = 'Авторы', fg_color = 'white', font = FONT).grid(row = 1, column = 0, pady = 5)
        ctk.CTkLabel(self, text = 'Издатель', fg_color = 'white', font = FONT).grid(row = 2, column = 0, pady = 5)
        ctk.CTkLabel(self, text = 'Год издания', fg_color = 'white', font = FONT).grid(row = 3, column = 0, pady = 5)
        ctk.CTkLabel(self, text = 'Количество', fg_color = 'white', font = FONT).grid(row = 4, column = 0, pady = 5)
        ctk.CTkLabel(self, text = 'Цена', fg_color = 'white', font = FONT).grid(row = 5, column = 0, pady = 5)
        ctk.CTkLabel(self, text = 'Штраф', fg_color = 'white', font = FONT).grid(row = 6, column = 0, pady = 5)

        self._title.grid(row = 0, column = 1, pady = 5, padx = 5, sticky = 'ew')
        self.__authors.grid(row = 1, column = 1, pady = 5, padx = 5, sticky = 'ew')
        self.__publisher.grid(row = 2, column = 1, pady = 5, padx = 5, sticky = 'ew')
        self.__publishYear.grid(row = 3, column = 1, pady = 5, padx = 5, sticky = 'ew')
        self._amount.grid(row = 4, column = 1, pady = 5, padx = 5, sticky = 'ew')
        self._price.grid(row = 5, column = 1, pady = 5, padx = 5, sticky = 'ew')
        self._fine.grid(row = 6, column = 1, pady = 5, padx = 5, sticky = 'ew')

        self._updateBtn.grid(row = 7, column = 0, sticky = 'ew', padx = 5)
        self._deleteBtn.grid(row = 7, column = 1, sticky = 'ew', padx = 5)


# раска для информации о газете
class NewsPaperInfoFrame(BaseInfoFrame):
    def __init__(self, parent, data: dict):
        super().__init__(parent, data)

        self.__numberVar = ctk.IntVar(self, data['info']['number'])
        self.__dateVar = ctk.StringVar(self, data['info']['date'])

        self.__number = ctk.CTkEntry(self, textvariable = self.__numberVar, font = FONT)
        self.__date = ctk.CTkEntry(self, textvariable = self.__dateVar, font = FONT)

        self.__create_layout()
    
    def __create_layout(self):
        ctk.CTkLabel(self, text = 'Название', fg_color = 'white', font = FONT).grid(row = 0, column = 0, pady = 5)
        ctk.CTkLabel(self, text = 'Номер выпуска', fg_color = 'white', font = FONT).grid(row = 1, column = 0, pady = 5)
        ctk.CTkLabel(self, text = 'Дата выпуска', fg_color = 'white', font = FONT).grid(row = 2, column = 0, pady = 5)
        ctk.CTkLabel(self, text = 'Количество', fg_color = 'white', font = FONT).grid(row = 3, column = 0, pady = 5)
        ctk.CTkLabel(self, text = 'Цена', fg_color = 'white', font = FONT).grid(row = 4, column = 0, pady = 5)
        ctk.CTkLabel(self, text = 'Штраф', fg_color = 'white', font = FONT).grid(row = 5, column = 0, pady = 5)

        self._title.grid(row = 0, column = 1, pady = 5, padx = 5, sticky = 'ew')
        self.__number.grid(row = 1, column = 1, pady = 5, padx = 5, sticky = 'ew')
        self.__date.grid(row = 2, column = 1, pady = 5, padx = 5, sticky = 'ew')
        self._amount.grid(row = 3, column = 1, pady = 5, padx = 5, sticky = 'ew')
        self._price.grid(row = 4, column = 1, pady = 5, padx = 5, sticky = 'ew')
        self._fine.grid(row = 5, column = 1, pady = 5, padx = 5, sticky = 'ew')

        self._updateBtn.grid(row = 6, column = 0, sticky = 'ew', padx = 5)
        self._deleteBtn.grid(row = 6, column = 1, sticky = 'ew', padx = 5)


class MagazineInfoFrame(BaseInfoFrame):
    def __init__(self, parent, data: dict):
        super().__init__(parent, data)

        self.__numberVar = ctk.IntVar(self, data['info']['number'])
        self.__dateVar = ctk.StringVar(self, data['info']['date'])
        self.__publisherVar = ctk.StringVar(self, value = data['info']['publisher'])

        self.__number = ctk.CTkEntry(self, textvariable = self.__numberVar, font = FONT)
        self.__date = ctk.CTkEntry(self, textvariable = self.__dateVar, font = FONT)
        self.__publisher = ctk.CTkEntry(self, textvariable = self.__publisherVar, font = ENTRY_FONT)

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


# окно с информацией о текстовом материале
class InfoWindow(ctk.CTkToplevel):
    def __init__(self, parent, data):
        super().__init__(master = parent)

        self.geometry('500x700')
        self.title(data['title'])

        image = Image.open(data['image_path']).resize((300, 300))

        self.__materialImage = ImageTk.PhotoImage(image)

        self.__image = ctk.CTkLabel(self, text = '', image = self.__materialImage)

        self.__create_layout(data)

    def __create_layout(self, data: dict):
        self.__image.pack()

        if data['type'] == 'Книга':
            BookInfoFrame(self, data).pack(expand = True, fill = 'both')

        elif data['type'] == 'Газета':
            NewsPaperInfoFrame(self, data).pack(expand = True, fill = 'both')

        elif data['type'] == 'Журнал':
            MagazineInfoFrame(self, data).pack(expand = True, fill = 'both')
