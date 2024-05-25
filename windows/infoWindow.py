import customtkinter as ctk
from PIL import Image, ImageTk
from settings import *
from dll.database import selectAllMaterials, updateMaterial, deleteMaterial
from CTkMessagebox import CTkMessagebox
from convert_to_json import to_json
import json


# базовая рамка для вывода информации
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

# раска для информации о книге
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
            id = data['id']
            type = data['type']
            image_path = data['image_path']

            title = self._titleVar.get() if self._title.get() != '' else data['title']
            authors = self.__authorsVar.get().split(',') if self.__authorsVar.get() != '' else data['info']['authors']
            publisher = self.__publisherVar.get() if self.__publisherVar.get() != '' else data['info']['publisher']
            publishYear = int(self.__publishYearVar.get())
            amount = int(self._amountVar.get())
            price = float(self._priceVar.get())
            fine = float(self._fineVar.get())

            updated_data = to_json(id = id, 
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


# раска для информации о газете
class NewsPaperInfoFrame(BaseInfoFrame):
    def __init__(self, parent, data: dict):
        super().__init__(parent, data)

        self.__numberVar = ctk.StringVar(self, data['info']['number'])
        self.__dateVar = ctk.StringVar(self, data['info']['date'])

        self.__number = ctk.CTkEntry(self, textvariable = self.__numberVar, font = FONT)
        self.__date = ctk.CTkEntry(self, textvariable = self.__dateVar, font = FONT)

        self._updateBtn.configure(command = lambda: self.__update(data))

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

    def __update(self, data: dict):
        try:
            id = data['id']
            type = data['type']
            image_path = data['image_path']

            title = self._titleVar.get() if self._title.get() != '' else data['title']
            number = int(self.__numberVar.get())
            date = self.__dateVar.get() if self.__dateVar.get() != '' else data['info']['date']
            amount = int(self._amountVar.get())
            price = float(self._priceVar.get())
            fine = float(self._fineVar.get())

            updated_data = to_json(id = id, 
                                   title = title, 
                                   type = type, 
                                   amount = amount, 
                                   price = price, 
                                   fine = fine,
                                   image_path = image_path,
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


class MagazineInfoFrame(BaseInfoFrame):
    def __init__(self, parent, data: dict):
        super().__init__(parent, data)

        self.__numberVar = ctk.StringVar(self, data['info']['number'])
        self.__dateVar = ctk.StringVar(self, data['info']['date'])
        self.__publisherVar = ctk.StringVar(self, value = data['info']['publisher'])

        self.__number = ctk.CTkEntry(self, textvariable = self.__numberVar, font = FONT)
        self.__date = ctk.CTkEntry(self, textvariable = self.__dateVar, font = FONT)
        self.__publisher = ctk.CTkEntry(self, textvariable = self.__publisherVar, font = ENTRY_FONT)

        self._updateBtn.configure(command = lambda: self.__update(data))

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

    def __update(self, data: dict):
        try:
            id = data['id']
            type = data['type']
            image_path = data['image_path']

            title = self._titleVar.get() if self._title.get() != '' else data['title']
            number = int(self.__numberVar.get())
            date = self.__dateVar.get() if self.__dateVar.get() != '' else data['info']['date']
            publisher = self.__publisher.get() if self.__publisher.get() != '' else data['info']['publisher']
            amount = int(self._amountVar.get())
            price = float(self._priceVar.get())
            fine = float(self._fineVar.get())

            updated_data = to_json(id = id, 
                                   title = title, 
                                   type = type, 
                                   amount = amount, 
                                   price = price, 
                                   fine = fine,
                                   image_path = image_path,
                                   number = number,
                                   date = date,
                                   publisher = publisher)

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

# окно с информацией о текстовом материале
class InfoWindow(ctk.CTkToplevel):
    def __init__(self, parent, data):
        super().__init__(master = parent)

        self.__parent = parent

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

    def redraw_mainframe(self):
        self.__parent.redraw_mainframe()
