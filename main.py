"""
Imports Needed: Tkinter

This program is a simple weight conversion application.

Instructions: Choose your weight type from both drop down menus and enter a
number to be converted. Based on users choice and input, a conversion will
be applied and displayed on the application.
"""

from tkinter import *
from tkinter import ttk

root = Tk()
root.geometry("600x400")


def convert():
    """
    This function holds the conversions for all types of conversions listed.

    Input:  User input
            Drop menu selections

    Output: Conversion depending on drop menu selection

    """
    try:
        warning.config(text="")
        result = int(user_input1.get())
        # POUNDS

        # Pounds to Ounces & Ounces to Pounds
        if drop_menu1.get() == "Pounds" and drop_menu2.get() == "Ounces":
            pounds_to_ounces = result * 16
            answer.config(text=pounds_to_ounces)

        # Pounds to Grams & Grams to Pounds
        elif drop_menu1.get() == "Pounds" and drop_menu2.get() == "Grams":
            pounds_to_grams = result * 454
            answer.config(text=pounds_to_grams)

        # Pounds to Kilograms & Kilograms to Pounds
        elif drop_menu1.get() == "Pounds" and drop_menu2.get() == "Kilograms":
            pounds_to_kilograms = result / 2.205
            answer.config(text=pounds_to_kilograms)

        # GRAMS

        # Grams to Ounces
        elif drop_menu1.get() == "Grams" and drop_menu2.get() == "Ounces":
            grams_to_ounces = result / 28.35
            answer.config(text=grams_to_ounces)

        # Grams to Pounds
        elif drop_menu1.get() == "Grams" and drop_menu2.get() == "Pounds":
            grams_to_pounds = result / 454
            answer.config(text=grams_to_pounds)

        # Grams to Kilograms
        elif drop_menu1.get() == "Grams" and drop_menu2.get() == "Kilograms":
            grams_to_kilograms = result / 1000
            answer.config(text=grams_to_kilograms)

        # KILOGRAMS

        # Kilograms to Grams
        elif drop_menu1.get() == "Kilograms" and drop_menu2.get() == "Grams":
            kilograms_to_grams = result * 1000
            answer.config(text=kilograms_to_grams)

        # Kilograms to Ounces
        elif drop_menu1.get() == "Kilograms" and drop_menu2.get() == "Ounces":
            kilograms_to_ounces = result * 35.274
            answer.config(text=kilograms_to_ounces)

        elif drop_menu1.get() == "Kilograms" and drop_menu2.get() == "Pounds":
            kilograms_to_pounds = result / 2.205
            answer.config(text=kilograms_to_pounds)



        # OUNCES
        elif drop_menu1.get() == "Ounces" and drop_menu2.get() == "Millililiters":
            ounces_to_milliliters = result * 29.574
            answer.config(text=ounces_to_milliliters)

        elif drop_menu1.get() == "Ounces" and drop_menu2.get() == "Quarts":
            ounces_to_quarts = result / 32
            answer.config(text=ounces_to_quarts)

        elif drop_menu1.get() == "Ounces" and drop_menu2.get() == "Cups":
            ounces_to_cups = result / 8.115
            answer.config(text=ounces_to_cups)

        elif drop_menu1.get() == "Ounces" and drop_menu2.get() == "Tablespoons":
            ounces_to_tablespoons = result * 2
            answer.config(text=ounces_to_tablespoons)

        else:
            warning.config(text="Invalid Selection")

    except ValueError:
        print("Please enter a valid number")
        warning.config(text=("Cannot convert", drop_menu1.get(), "to",
                             drop_menu2.get()))


# Title of program
header = Label(root,
               text="Weight Converter",
               anchor="w",
               font=("Arial", 50))
header.pack()

# Options for weight conversions
weight_options = ["Pounds",
                  "Ounces",
                  "Kilograms",
                  "Grams"]
# User input
user_input1 = Entry(root)
user_input1.pack()

# Drop down menu (1)
drop_menu1 = ttk.Combobox(root, value=weight_options)
drop_menu1.current(0)
drop_menu1.bind("<<ComboboxSelected>>")
drop_menu1.pack(pady=5)

# 'Convert to' text widget
header = Label(root,
               text="Convert To",
               font=("Arial", 30))
header.pack()

# Drop down menu (1)
drop_menu2 = ttk.Combobox(root, value=weight_options)
drop_menu2.current(0)
drop_menu2.bind("<<ComboboxSelected>>")
drop_menu2.pack(pady=5)

# Button to start conversion
convert_button = Button(root,
                        text="Convert",
                        command=convert,
                        pady="4")
convert_button.pack()

# Label where answer is displayed
answer = Label(root,
               text="0",
               font=("Helvetica", 18))
answer.pack()

warning = Label(root,
                text="",
                font=("Helvetica", 18))
warning.pack()

# Main loop call
root.mainloop()
