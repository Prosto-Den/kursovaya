import customtkinter as ctk
from tkinter import Misc
from PIL.ImageTk import PhotoImage
from settings import *
from windows import AddBookWindow, AddMagazineWindow, AddNewsPaperWindow
from windows import AddClientWindow, ClientsWindow
from windows import BorrowWindows
from windows import BorrowedBooksWindow
from windows import DebtorsWindow


# боковое меню
class SideFrame(ctk.CTkFrame):
    def __init__(self, parent: Misc, 
                 start_pos: float, 
                 end_pos: float,
                 menu_image: PhotoImage) -> None:
        super().__init__(parent)

        self._parent: Misc = parent

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

        else:
            self.__animate_backward()

    # forward animation
    def __animate_forward(self):
        if self.__pos > self.__end_pos:
            self.__pos -= 0.01
            self.place(relx = self.__pos, rely = self.__rely, relwidth = self.__width, relheight = self.__relheight)
            self.after(10, self.__animate_forward)
        
        self.__in_start_pos = False

    # backward animation
    def __animate_backward(self):
        if self.__pos < self.__start_pos:
            self.__pos += 0.01
            self.place(relx = self.__pos, rely = self.__rely, relwidth = self.__width, relheight = self.__relheight)
            self.after(10, self.__animate_backward)

        self.__in_start_pos = True

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
                          command = self.__open_add_window).place(relx = 0, rely = 0.08, relwidth = 1, relheight = 0.05)

        # Просмотр информации о зарегистрированных читателях
        ctk.CTkButton(self,
                      text = 'Читатели',
                      text_color = BTN_TEXT_COLOUR,
                      fg_color = BTN_COLOUR,
                      hover_color = HOVER_BTN_COLOUR,
                      font = FONT,
                      command = lambda: ClientsWindow(self._parent)).place(relx = 0, rely = 0.16, relwidth = 1, relheight = 0.05)
        
        # Выдача книги читателю
        ctk.CTkButton(self,
                      text = 'Выдать книгу',
                      text_color = BTN_TEXT_COLOUR,
                      fg_color = BTN_COLOUR,
                      hover_color = HOVER_BTN_COLOUR,
                      font = FONT,
                      command = lambda: BorrowWindows(self._parent)).place(relx = 0, rely = 0.24, relwidth = 1, relheight = 0.05)
        
        # Просмотр всех отданных книг
        ctk.CTkButton(self,
                      text = 'Отданные книги',
                      text_color = BTN_TEXT_COLOUR,
                      fg_color = BTN_COLOUR,
                      hover_color = HOVER_BTN_COLOUR,
                      font = FONT,
                      command = lambda: BorrowedBooksWindow(self._parent)).place(relx = 0, rely = 0.32, relwidth = 1, relheight = 0.05)
        
        # Просмотр должников
        ctk.CTkButton(self,
                      text = 'Должники',
                      text_color = BTN_TEXT_COLOUR,
                      fg_color = BTN_COLOUR,
                      hover_color = HOVER_BTN_COLOUR,
                      font = FONT,
                      command = lambda: DebtorsWindow(self._parent)).place(relx = 0, rely = 0.4, relwidth = 1, relheight = 0.05)
    
    
    # open window to add the material
    def __open_add_window(self, type: str):
        self.__add_var.set('Добавить')

        if type == ADD_VALUES[0]:
            AddBookWindow(self._parent)

        elif type == ADD_VALUES[1]:
            AddMagazineWindow(self._parent)
        
        elif type == ADD_VALUES[2]:
            AddNewsPaperWindow(self._parent)
        
        elif type == ADD_VALUES[3]:
            AddClientWindow(self._parent)

        self.__animate_backward()
