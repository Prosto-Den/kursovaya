import customtkinter as ctk


class AddClientWindow(ctk.CTkToplevel):
    def __init__(self, type: str) -> None:
        super().__init__()

        # build the layout
        if type == 'Клиента':
            self.__create_client_layout()

        elif type == 'Поставщика':
            self.__create_provider_layout()

        # set the focus 
        self.focus()
        self.grab_set()

    def __create_client_layout(self) -> None:
        self.name = ctk.CTkEntry(self)
        self.birthday = ctk.CTkEntry(self)
        self.passport = ctk.CTkEntry(self)

        self.name.pack()
        self.birthday.pack()
        self.passport.pack()

    def __create_provider_layout(self) -> None:
        self.name = ctk.CTkEntry(self)
        self.address = ctk.CTkEntry(self)
        self.phone = ctk.CTkEntry(self)

        self.name.pack()
        self.address.pack()
        self.phone.pack()

    def __create_order_layout(self) -> None:
        pass