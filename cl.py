from tkinter import *

class APP:
    def __init__(self):

        def click():
            quantity = int(self.p_quantity_entry.get())
            buy = int(self.p_sell_entry.get())
            sell = int(self.p_buy_entry.get())
            profit = buy -
            text_d = f'In {quantity} {self.p_name_entry.get()} has a profit of {profit}'
            self.detail_label = Label(text=text_d).grid(row = 3, column = 0)

        def add_placeholder(entry, placeholder):
            entry.insert(0, placeholder)
            entry.config(fg="grey")

            def on_focus_in(event):
                if entry.get() == placeholder:
                    entry.delete(0, END)
                    entry.config(fg="black")

            def on_focus_out(event):
                if entry.get() == "":
                    entry.insert(0, placeholder)
                    entry.config(fg="grey")

            entry.bind("<FocusIn>", on_focus_in)
            entry.bind("<FocusOut>", on_focus_out)

        self.root = Tk()
        self.root.geometry('300x400')

        self.p_name_entry = Entry(self.root)
        self.p_name_entry.grid(row=0, column=0)
        add_placeholder(self.p_name_entry, "Name")

        self.p_buy_entry = Entry(self.root)
        self.p_buy_entry.grid(row=1, column=0)
        add_placeholder(self.p_buy_entry, "Buy")

        self.p_sell_entry = Entry(self.root)
        self.p_sell_entry.grid(row=0, column=1)
        add_placeholder(self.p_sell_entry, "Sell")

        self.p_quantity_entry = Entry(self.root)
        self.p_quantity_entry.grid(row=1, column=1)
        add_placeholder(self.p_quantity_entry, "Quantity")

        self.insert_button = Button(self.root, text='Insert', command=click)
        self.insert_button.grid(row=2, column=0, columnspan=2)

        
        self.root.mainloop()


app_1 = APP()
