import customtkinter as ctk
from settings import *
from PIL import Image, ImageTk
from tkinter.filedialog import askopenfile
from CTkMessagebox import CTkMessagebox
import os
import shutil

class BaseAddWindow(ctk.CTkToplevel):
    def __init__(self):
        super().__init__()

        picture = Image.open(MATERIALS_PICTURE_PATH + 'default.png').resize((300, 300))
        self.__materialImage = ImageTk.PhotoImage(picture)
        self._imageName = 'default.png'

        self._image = ctk.CTkLabel(self, text = '', image = self.__materialImage)
        self._imageBtn = ctk.CTkButton(self, 
                                      text = 'Выбрать изображение', 
                                      font = FONT,
                                      text_color = BTN_TEXT_COLOUR,
                                      fg_color = BTN_COLOUR,
                                      hover_color = HOVER_BTN_COLOUR, 
                                      command = self._select_image)
        
        self._title = ctk.CTkEntry(self, placeholder_text = 'Название', font = ENTRY_FONT)
        self._amount = ctk.CTkEntry(self, placeholder_text = 'Количество', font = ENTRY_FONT)
        self._price = ctk.CTkEntry(self, placeholder_text = 'Цена', font = ENTRY_FONT)
        self._fine = ctk.CTkEntry(self, placeholder_text = 'Штраф', font = ENTRY_FONT)
        self._saveBtn = ctk.CTkButton(self, 
                                      text = 'Сохранить', 
                                      font = FONT,
                                      text_color = BTN_TEXT_COLOUR,
                                      fg_color = BTN_COLOUR,
                                      hover_color = HOVER_BTN_COLOUR)

    # choose the image from your computer
    def _select_image(self) -> None:
        file_path = askopenfile(filetypes = [('JPG files', ['*jpeg', '*jpg']), 
                                             ('PNG files', '*png'), 
                                             ('Image files', ['*jpg', '*jpeg', '*png'])])

        # if window was closen then do nothig
        if file_path is None:
            return
        
        else:
            self._imageName = file_path.name.split('/')[-1]

            # если файл с таким названием уже есть в папке - спрашиваем, нужно ли его копировать
            if self._imageName in os.listdir(MATERIALS_PICTURE_PATH):
                message = CTkMessagebox(self, title = 'Внимание',
                                        message = 'Файл с таким названием уже есть в папке. Заменить его?',
                                        option_1 = 'Да',
                                        option_2 = 'Нет',
                                        icon = 'warning')
                
                if message.get() == 'Да':
                    shutil.copy(file_path.name, MATERIALS_PICTURE_PATH)

            else:
                shutil.copy(file_path.name, MATERIALS_PICTURE_PATH)

            path = MATERIALS_PICTURE_PATH + self._imageName

            image = Image.open(path).resize((300, 300))
            self.__materialImage = ImageTk.PhotoImage(image)

            self._image.configure(image = self.__materialImage) 

    def _show_warning(self) -> None:
        CTkMessagebox(self, 
                          title = 'Внимание',
                          message = 'Необходимо заполнить все поля',
                          icon = 'cancel',
                          option_1 = 'OK',
                          font = FONT)
    
    # create start base layout (similar to all windows)
    def _create_base_layout_start(self):
        self._image.pack(fill = 'x', padx = 5, pady = 5)
        self._imageBtn.pack(fill = 'x', padx = 5, pady = 5)
        self._title.pack(fill = 'x', padx = 5, pady = 5)

    # create end base layout (similar to all windows)
    def _create_base_layout_end(self):
        self._amount.pack(fill = 'x', padx = 5, pady = 5)
        self._price.pack(fill = 'x', padx = 5, pady = 5)
        self._fine.pack(fill = 'x', padx = 5, pady = 5)

        self._saveBtn.pack(fill = 'x', padx = 5, pady = 5)
