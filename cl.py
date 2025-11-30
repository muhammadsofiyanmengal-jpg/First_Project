from tkinter import *
import pandas as pd
import os

class APP:
    def __init__(self):

        def click():
            quantity = int(self.p_quantity_entry.get())
            buy = int(self.p_sell_entry.get())
            sell = int(self.p_buy_entry.get())
            profit = buy - sell
            name = self.p_name_entry.get()
            text_d = f'Added {quantity} of {name}'
            self.detail_label = Label(text=text_d).grid(row = 3, column = 0)
        def add_to_csv():

            quantity = int(self.p_quantity_entry.get())
            buy = int(self.p_buy_entry.get())
            sell = int(self.p_sell_entry.get())
            profit = sell - buy
            name = self.p_name_entry.get()
            filename = 'data.csv'
            # Determine next serial number
            if os.path.exists(self.filename):
                old_df = pd.read_csv(self.filename)
                serial_no = old_df["Serial"].max() + 1 if len(old_df) > 0 else 1
            else:
                serial_no = 1

            # Create new row
            new_row = {
                "Serial": serial_no,
                "Name": name,
                "Buy": buy,
                "Sell": sell,
                "Quantity": quantity,
                "Profit": profit
            }

            new_df = pd.DataFrame([new_row])  # <-- Correct dataframe

            # Save to CSV
            if os.path.exists(self.filename):
                new_df.to_csv(self.filename, mode="a", index=False, header=False)
            else:
                new_df.to_csv(self.filename, index=False)

            Label(self.root, text=f"Saved (Serial {serial_no})").grid(row=6, column=0, columnspan=2)

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
        self.p_buy_entry.grid(row=0, column=1)
        add_placeholder(self.p_buy_entry, "Buy")

        self.p_sell_entry = Entry(self.root)
        self.p_sell_entry.grid(row=1, column=0)
        add_placeholder(self.p_sell_entry, "Sell")

        self.p_quantity_entry = Entry(self.root)
        self.p_quantity_entry.grid(row=1, column=1)
        add_placeholder(self.p_quantity_entry, "Quantity")

        self.insert_button = Button(self.root, text='Insert', command=click)
        self.insert_button.grid(row=2, column=0, columnspan=2)

        
        self.root.mainloop()


app_1 = APP()
