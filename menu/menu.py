import customtkinter as ctk
from tkinter import Misc
from PIL import Image, ImageTk
from settings import BTN_COLOUR, HOVER_BTN_COLOUR
from menu.sideframe import SideFrame
from windows import FilterWindow


class Menu(ctk.CTkFrame):
    def __init__(self, parent: Misc) -> None:
        super().__init__(parent, corner_radius = 0)

        self.columnconfigure((0, 1, 2, 3, 4, 5), weight = 1, uniform = 'a')
        self.rowconfigure(0, weight = 1)

        filter_image = ImageTk.PhotoImage(Image.open('pictures/filters.png').resize((20, 20)))
        menu_image = ImageTk.PhotoImage(Image.open('pictures/menu.png').resize((40, 40)))

        self.menu = SideFrame(parent, 1, 0.7, menu_image)

        self.__search = ctk.CTkEntry(self, textvariable = parent.searchVar)

        self.__search.bind('<KeyRelease>', lambda _: parent.redraw_mainframe())

        self.__search.grid(row = 0, column = 0, columnspan = 3, sticky = 'ew', padx = 5)

        ctk.CTkButton(self, 
                      text = '', 
                      image = filter_image,
                      width = 30,
                      fg_color = BTN_COLOUR,
                      hover_color = HOVER_BTN_COLOUR,
                      command = lambda: FilterWindow(parent)).grid(row = 0, column = 3, sticky = 'w')
        
        ctk.CTkButton(self,
                      text = '',
                      image = menu_image,
                      width = 30,
                      fg_color = BTN_COLOUR,
                      hover_color = HOVER_BTN_COLOUR,
                      command = self.menu.animate).grid(row = 0, column = 5, sticky = 'e', padx = 5)
    
