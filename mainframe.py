import customtkinter as ctk
from tkinter import Misc


class MainFrame(ctk.CTkScrollableFrame):
    def __init__(self, parent: Misc):
        super().__init__(parent, fg_color = 'white')

