import tkinter as tk
from tkinter import ttk


class PacketLog(tk.Frame):
    def __init__(self, root):
        super().__init__(root)

        self.text = tk.Text(self, state=tk.DISABLED, height=9)

        self.text.tag_config('TCP', foreground='blue')
        self.text.tag_config('UDP', foreground='red')
        self.text.tag_config('ICMP', foreground='orange')

        self.text.tag_config(
            'activeFlag', background="green", foreground='white')
        self.text.tag_config(
            'disabledFlag', background="red", foreground='white')

        self.text.bind("<1>", lambda event: self.text.focus_set())

        self.autoscroll = tk.BooleanVar(self)
        self.autoscroll.set(True)
        self.checkbox = ttk.Checkbutton(self,
                                        text="Autoscroll", variable=self.autoscroll)

        self.text.pack()
        self.checkbox.pack(anchor=tk.W)
