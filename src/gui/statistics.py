import tkinter as tk


class Statistics(tk.Frame):
    def __init__(self, root):
        super().__init__(root)
        self.config(padx=5)
        self.originsValues = set()
        self.destinationValues = set()

        self.maxTTL = None
        self.minTTL = None
        self.packet_count = 0

        self.minTTL_text = tk.StringVar(value='Min. TTL: 0')
        self.maxTTL_text = tk.StringVar(value='Max. TTL: 0')
        self.packet_count_text = tk.StringVar(value='N° Paquetes: 0')

        tk.Label(self, textvariable=self.packet_count_text).place(
            x="445", y="10", anchor=tk.E)
        tk.Label(self, textvariable=self.maxTTL_text).place(
            x="445", y="30", anchor=tk.E)
        tk.Label(self, textvariable=self.minTTL_text).place(
            x="445", y="50", anchor=tk.E)

        self.originsFrame = tk.LabelFrame(
            self, text="Orígenes", padx=5, pady=2)
        self.origins = tk.Listbox(self.originsFrame, height=9)

        self.destinationFrame = tk.LabelFrame(
            self, text="Destinos", padx=5, pady=2)
        self.destination = tk.Listbox(self.destinationFrame, height=9)

        self.origins.pack()
        self.destination.pack()
        self.originsFrame.grid(column=0, row=0)
        self.destinationFrame.grid(column=1, row=0)

    def refresh(self):
        self.minTTL_text.set(f'Min. TTL: {self.minTTL}')
        self.maxTTL_text.set(f'Max. TTL: {self.maxTTL}')
        self.packet_count_text.set(f'N° Paquetes: {self.packet_count}')

        self.origins.delete(0, tk.END)
        self.origins.insert(0, *self.originsValues)

        self.destination.delete(0, tk.END)
        self.destination.insert(0, *self.destinationValues)
