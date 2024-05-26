import customtkinter as ctk
from windows.infoFrames import *
from PIL import Image, ImageTk
from settings import *


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
