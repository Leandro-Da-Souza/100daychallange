from tkinter import *

window = Tk()
window.title('Mile To Km Converter')
window.config(padx=20, pady=20)

user_input = Entry(width=7)
user_input.grid(row=1, column=2)
miles_label = Label(text='Miles')
miles_label.grid(row=1, column=3)

is_equal_to_label = Label(text='is equal to')
is_equal_to_label.grid(row=2, column=1)
convert_label = Label(text="0")
convert_label.grid(row=2, column=2)
km_label = Label(text='Km')
km_label.grid(row=2, column=3)


def handle_click():
    miles = user_input.get()
    try:
        miles = float(miles)
    except ValueError:
        print('Please input a number')
        return
    kilometer = round(miles * 1.609)
    convert_label.config(text=f"{kilometer}")


button = Button(text='Calculate', command=handle_click)
button.grid(row=3, column=2)

window.mainloop()
