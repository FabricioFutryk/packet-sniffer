import tkinter as tk


class Statistics(tk.Frame):
    def __init__(self, root):
        super().__init__(root)
        self.config(padx=5)
        self.originsValues = set()
        self.destinationValues = set()

        self.maxTTL = None
        self.minTTL = None

        self.minTTL_text = tk.StringVar(value='Min. TTL: 0')
        self.maxTTL_text = tk.StringVar(value='Max. TTL: 0')

        tk.Label(self, textvariable=self.maxTTL_text).place(x="375", y="10")
        tk.Label(self, textvariable=self.minTTL_text).place(x="375", y="30")

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

        self.origins.delete(0, tk.END)
        self.origins.insert(0, *self.originsValues)

        self.destination.delete(0, tk.END)
        self.destination.insert(0, *self.destinationValues)
