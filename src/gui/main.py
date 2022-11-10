import tkinter as tk
from tkinter import ttk
from gui.packet_log import PacketLog
from gui.statistics import Statistics


class GUI(tk.Tk):
    def __init__(self):
        super().__init__()

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

    def render(self):
        self.mainloop()
