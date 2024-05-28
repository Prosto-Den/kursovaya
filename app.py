import customtkinter as ctk
from platform import system
from settings import *
from menu import MainFrame
from menu import Menu
from dll import connectToDB, disconnectFromDB, selectAllMaterials, selectAllClients, selectAllClientMaterial, selectAllDebtors
import os


if system() == 'Windows':
    windows_flag = True

    from ctypes import windll, byref, sizeof, c_int


# main app class
class App(ctk.CTk):
    def __init__(self) -> None:
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

        self.searchVar = ctk.StringVar(self)
        self.bookVar = ctk.BooleanVar(self, value = True)
        self.newsVar = ctk.BooleanVar(self, value = True)
        self.magazineVar = ctk.BooleanVar(self, value = True)

        self.searchOption = ctk.IntVar(self)

        # establish connection with dataBase
        if connectToDB() == -1:
            disconnectFromDB()

            exit()

        # update file with materials
        selectAllMaterials()

        # update file with clients
        selectAllClients()

        # update file with borrowed materials
        selectAllClientMaterial()

        # update file with debtors
        selectAllDebtors()

        # create layout
        self.mainframe = MainFrame(self)
        self.menu = Menu(self)

        self.__create_layout()

        self.mainloop()

        # disconnect from database
        disconnectFromDB()

        # delete temporary files
        if 'material.json' in os.listdir(DATA_PATH):
            os.remove(DATA_PATH + 'material.json')

        if 'client.json' in os.listdir(DATA_PATH):
            os.remove(DATA_PATH + 'client.json')

    # place widgets on the window
    def __create_layout(self) -> None:
        self.menu.place(relx = 0, rely = 0, relwidth = 1, relheight = 0.2)
        self.mainframe.place(relx = 0, rely = 0.2, relwidth = 1, relheight = 0.8)

    # redraw mainframe
    def redraw_mainframe(self) -> None:
        self.mainframe.place_forget()
        self.menu.place_forget()

        self.mainframe = MainFrame(self)
        self.menu = Menu(self)

        self.__create_layout()


if __name__ == '__main__':
    App()