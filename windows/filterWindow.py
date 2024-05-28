import customtkinter as ctk
from settings import *


class FilterWindow(ctk.CTkToplevel):
    def __init__(self, parent):
        super().__init__(master = parent)

        self.__parent = parent

        self.title('Фильтры')
        self.geometry('400x100')
        self.resizable(False, False)

        self.rowconfigure(0, weight = 1)
        self.columnconfigure((0, 1, 2, 3), weight = 1, uniform = 'a')

        self.__create_layout()
    
    def __create_layout(self):
        ctk.CTkLabel(self, text = 'По типу', font = FONT).grid(row = 0, column = 0, sticky = 'n')

        ctk.CTkCheckBox(self, text = 'Книга', 
                        variable = self.__parent.bookVar,
                        fg_color = CHECK_BOX_COLOUR,
                        hover_color = HOVER_CHECK_BOX_COLOUR,
                        font = ENTRY_FONT, 
                        command = self.__parent.redraw_mainframe).grid(row = 0, column = 1, sticky = 'n', pady = 5)
        
        ctk.CTkCheckBox(self, text = 'Газета', 
                        variable = self.__parent.newsVar,
                        fg_color = CHECK_BOX_COLOUR,
                        hover_color = HOVER_CHECK_BOX_COLOUR,
                        font = ENTRY_FONT, 
                        command = self.__parent.redraw_mainframe).grid(row = 0, column = 2, sticky = 'n', pady = 5)
        
        ctk.CTkCheckBox(self, text = 'Журнал', 
                        variable = self.__parent.magazineVar,
                        fg_color = CHECK_BOX_COLOUR,
                        hover_color = HOVER_CHECK_BOX_COLOUR,
                        font = ENTRY_FONT, 
                        command = self.__parent.redraw_mainframe).grid(row = 0, column = 3, sticky = 'n', pady = 5)
