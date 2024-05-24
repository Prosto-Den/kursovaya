import customtkinter as ctk
from tkinter import Misc
from PIL import Image, ImageTk
from windows import InfoWindow


class Cell(ctk.CTkFrame):
    def __init__(self, parent: Misc, data: dict):
        super().__init__(parent, fg_color = 'white',
                         border_color = 'black', border_width = 1, width = 300, height = 300)

        image = ImageTk.PhotoImage(Image.open(data['image_path']).resize((200, 200)))

        self.image = ctk.CTkLabel(self, text = '', image = image)
        self.label = ctk.CTkLabel(self, text = data['title'])

        self.image.pack(pady = 5)
        self.label.pack()

        self.image.bind('<Button-1>', lambda _: InfoWindow(self, data))
        self.label.bind('<Button-1>', lambda _: InfoWindow(self, data))
        self.bind('<Button-1>', lambda _: InfoWindow(self, data))