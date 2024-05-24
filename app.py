import customtkinter as ctk
from platform import system
from settings import *
from menu import MainFrame
from menu import Menu
from dll import connectToDB, disconnectFromDB, selectAllMaterials


if system() == 'Windows':
    windows_flag = True

    from ctypes import windll, byref, sizeof, c_int


class App(ctk.CTk):
    def __init__(self):
        super().__init__(fg_color = 'white')

        # settings
        self.title('Библиотека')
        self.geometry('900x800')
        self.resizable(False, False)
        self.iconbitmap('pictures/icon.ico')

        ctk.set_appearance_mode('Light')

        if windows_flag:
            HWND = windll.user32.GetParent(self.winfo_id())

            windll.dwmapi.DwmSetWindowAttribute(HWND, 35, byref(c_int(TITLEBAR_COLOUR)), sizeof(c_int))

        # establish connection with dataBase
        connectToDB()

        selectAllMaterials()

        # create layout
        self.menu = Menu(self)
        self.mainframe =  MainFrame(self)

        self.__create_layout()

        self.mainloop()

        # disconnect from database
        disconnectFromDB()

    def __create_layout(self):
        self.menu.place(relx = 0, rely = 0, relwidth = 1, relheight = 0.2)
        self.mainframe.place(relx = 0, rely = 0.2, relwidth = 1, relheight = 0.8)

    def redraw_mainframe(self):
        self.mainframe.place_forget()

        self.mainframe = MainFrame(self)

        self.mainframe.place(relx = 0, rely = 0.2, relwidth = 1, relheight = 0.8)



if __name__ == '__main__':
    App()