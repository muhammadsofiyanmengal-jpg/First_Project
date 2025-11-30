from tkinter import *
import pandas as pd
import os

class APP:
    def __init__(self):
        
        def add_to_csv():
            name = self.p_name_entry.get()
            buy = self.p_buy_entry.get()
            sell = self.p_sell_entry.get()
            quantity = self.p_quantity_entry.get()

            # Check if any field is empty or still has placeholder
            if not name or not buy or not sell or not quantity \
               or name == "Name" or buy == "Buy" or sell == "Sell" or quantity == "Quantity":
                Label(self.root, text="All fields must be filled correctly!").grid(row=3, column=0)
                return  # Stop function

            # Try converting to integers safely
            try:
                buy_val = int(buy)
                sell_val = int(sell)
                quantity_val = int(quantity)
            except ValueError:
                Label(self.root, text="Buy, Sell, and Quantity must be numbers!").grid(row=3, column=0)
                return

            profit = (sell_val - buy_val) * quantity_val
            filename = "data.csv"
            text_d = f"Added {quantity_val} of {name}"
            Label(self.root, text=text_d).grid(row=3, column=0)

            # Determine next serial number
            if os.path.exists(filename):
                old_df = pd.read_csv(filename)
                if "Serial" in old_df.columns and len(old_df) > 0:
                    serial_no = old_df["Serial"].max() + 1
                else:
                    serial_no = 1
            else:
                serial_no = 1

            # Create new row
            new_row = {
                "Serial": serial_no,
                "Name": name,
                "Buy": buy_val,
                "Sell": sell_val,
                "Quantity": quantity_val,
                "Profit": profit
            }

            new_df = pd.DataFrame([new_row])

            # Save to CSV
            if os.path.exists(filename):
                new_df.to_csv(filename, mode="a", index=False, header=False)
            else:
                new_df.to_csv(filename, index=False)

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

        self.insert_button = Button(self.root, text='Insert', command=add_to_csv, bg="green", fg="white")
        self.insert_button.grid(row=2, column=0, columnspan=2)

        
        self.root.mainloop()


app_1 = APP()
