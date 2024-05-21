import customtkinter as ctk
from tkinter import Misc
from PIL.ImageTk import PhotoImage
from settings import *
from add_window import AddMaterialWindow
from add_client import AddClientWindow

class SideFrame(ctk.CTkFrame):
    def __init__(self, parent: Misc, 
                 start_pos: float, 
                 end_pos: float,
                 menu_image: PhotoImage) -> None:
        super().__init__(parent)

        self.__parent = parent

        # frame settings
        self.__width: float = abs(start_pos - end_pos)
        self.__rely: float = 0.05
        self.__relheight: float = 0.9

        # btn settings
        self.__add_var = ctk.StringVar(self, 'Добавить')

        # animation settings
        self.__start_pos: float = start_pos
        self.__end_pos: float = end_pos
        self.__pos: float = self.__start_pos
        self.__in_start_pos: bool = True

        # create and show layout
        self.__create_layout(menu_image)

        self.place(relx = self.__start_pos, rely = self.__rely, relwidth = self.__width, relheight = self.__relheight)

    # animate frame
    def animate(self):
        if self.__in_start_pos:
            self.__animate_forward()
            self.__in_start_pos = False

        else:
            self.__animate_backward()
            self.__in_start_pos = True

    # forward animation
    def __animate_forward(self):
        if self.__pos > self.__end_pos:
            self.__pos -= 0.01
            self.place(relx = self.__pos, rely = self.__rely, relwidth = self.__width, relheight = self.__relheight)
            self.after(10, self.__animate_forward)

    # backward animation
    def __animate_backward(self):
        if self.__pos < self.__start_pos:
            self.__pos += 0.01
            self.place(relx = self.__pos, rely = self.__rely, relwidth = self.__width, relheight = self.__relheight)
            self.after(10, self.__animate_backward)

        self.place()

    # create layout
    def __create_layout(self, menu_image: PhotoImage):

        # close menu btn
        ctk.CTkButton(self,
                      text = '',
                      image = menu_image,
                      command = self.animate,
                      fg_color = BTN_COLOUR,
                      hover_color = HOVER_BTN_COLOUR).place(relx = 0, rely = 0, relwidth = 0.2, relheight = 0.05)
        
        # add material btn
        ctk.CTkOptionMenu(self, 
                          variable = self.__add_var,
                          values = ADD_VALUES,
                          text_color = BTN_TEXT_COLOUR,
                          fg_color = BTN_COLOUR,
                          button_color = OPTION_BTN_COLOUR,
                          button_hover_color = HOVER_OPTION_BTN_COLOUR,
                          dropdown_hover_color = HOVER_BTN_COLOUR,
                          font = FONT,
                          command = self.__add_material).place(relx = 0, rely = 0.08, relwidth = 1, relheight = 0.05)
        
    def __add_material(self, type: str):
        self.__add_var.set('Добавить')

        if type in ADD_VALUES[:3]:
            AddMaterialWindow(self.__parent, type)
        else:
            AddClientWindow(type)
