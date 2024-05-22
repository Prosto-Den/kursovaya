import customtkinter as ctk
from platform import system
from settings import *
from menu.mainframe import MainFrame
from menu.menu import Menu
import os

if system() == 'Windows':
    windows_flag = True

    from ctypes import windll, byref, sizeof, c_int


class App(ctk.CTk):
    def __init__(self):
        super().__init__(fg_color = 'white')

        # settings
        self.title('Library')
        self.geometry('900x800')
        self.resizable(False, False)
        self.iconbitmap('pictures/icon.ico')

        ctk.set_appearance_mode('Light')

        if windows_flag:
            HWND = windll.user32.GetParent(self.winfo_id())

            windll.dwmapi.DwmSetWindowAttribute(HWND, 35, byref(c_int(TITLEBAR_COLOUR)), sizeof(c_int))

        # create layout
        Menu(self).place(relx = 0, rely = 0, relwidth = 1, relheight = 0.2)
        MainFrame(self).place(relx = 0, rely = 0.2, relwidth = 1, relheight = 0.8)

        self.mainloop()
        os.system('cls')

if __name__ == '__main__':
    App()