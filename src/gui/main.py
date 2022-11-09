import tkinter as tk
from tkinter import font


class GUI(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Capturador de paquetes de Red")
        self.geometry("475x220")
        self.resizable(False, False)
        self.config(padx=10, pady=10)

        self.text = tk.Text(self, state=tk.DISABLED)

        self.text.pack()

        self.text.tag_config('TCP', foreground='blue')
        self.text.tag_config('UDP', foreground='red')
        self.text.tag_config('ICMP', foreground='orange')

        self.text.tag_config(
            'activeFlag', background="green", foreground='white')
        self.text.tag_config(
            'disabledFlag', background="red", foreground='white')

        self.text.bind("<1>", lambda event: self.text.focus_set())

    def render(self):
        self.mainloop()
