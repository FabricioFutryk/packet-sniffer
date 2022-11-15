import tkinter as tk
from tkinter import ttk
from gui.packet_log import PacketLog
from gui.statistics import Statistics
import sys
from tkinter import messagebox


class GUI(tk.Tk):
    def __init__(self):
        super().__init__()

        self.is_open = True

        self.title("Capturador de paquetes de Red")
        self.geometry("480x220")
        self.resizable(False, False)
        self.config(padx=10, pady=10)

        self.notebook = ttk.Notebook(self)

        self.packet_register = PacketLog(self)
        self.statistics = Statistics(self)

        self.notebook.add(self.packet_register, text="Registro")
        self.notebook.add(self.statistics, text="Estadisticas")

        self.notebook.pack()

        self.protocol('WM_DELETE_WINDOW', self.close)

    def close(self):
        if messagebox.askokcancel('Salir', 'Está seguro que desea salir del programa?'):
            self.destroy()
            sys.exit()
            self.is_open = False

    def render(self):
        self.mainloop()
