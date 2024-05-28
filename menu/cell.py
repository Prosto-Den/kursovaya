import customtkinter as ctk
import json
from PIL import Image, ImageTk
from windows import InfoWindow
from tkinter import Misc


# cell on the mainframe
class Cell(ctk.CTkFrame):
    def __init__(self, parent: Misc, item: str):
        super().__init__(parent, fg_color = 'white',
                         border_color = 'black', border_width = 1, 
                         width = 300, height = 300)

        with open('./temp/selectAllMaterials.json', encoding = 'utf-8') as file:
            data = dict(json.load(file))[item]

        self.__parent = parent

        image = ImageTk.PhotoImage(Image.open(data['image_path']).resize((200, 250)))

        self.image = ctk.CTkLabel(self, text = '', image = image)
        self.label = ctk.CTkLabel(self, text = data['title'])

        self.image.pack()
        self.label.pack()

        self.image.bind('<Button-1>', lambda _: InfoWindow(self.__parent, item))
        self.label.bind('<Button-1>', lambda _: InfoWindow(self.__parent, item))
        self.bind('<Button-1>', lambda _: InfoWindow(self.__parent, item))