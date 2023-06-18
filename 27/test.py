from tkinter import *

window = Tk()
window.title('Leo GUI')
window.minsize(width=500, height=300)

# label
my_label = Label(text="I Am A Label", font=('Helvetica', 24, 'italic'))
# my_label.place(x=0, y=50)
# my_label.pack(side='left')
my_label.grid(row=1, column=1)
my_label['text'] = 'I Am The Table'
my_label.config({
    'text': 'Motownphilly back again.'
})

# Entry
user_input = Entry(width=10)

# user_input.pack()
user_input.grid(row=2, column=2)


def button_clicked():
    my_label.config(text=user_input.get())


# Button
button = Button(text='click me', command=button_clicked)
# button.pack()
button.grid(row=3, column=3)


# Advanced keyword arguments

# Arguments with default values, if function is called without any arguments
# it will use defaults values specified when declaring the func

def my_function(a=1, b=2, c=3):
    # do something a
    # do something with b
    # do something with c
    pass


# *args: Many Positional Arguments, functions with unlimited amounts of arguments,
# this is declared with the use of the asterisk, args naming is optional but conventional.
# args (or whatever named) will be in the form of a tuple (1,2,a,5,3,b, True)
# also known as Unlimited Positional Arguments
def add(*args):
    result = 0
    for n in args:
        result += n
    return result


print(add(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))


# **kwargs: Many Keyword Arguments, same as *args but lets you work with any number of keyword arguments.
# the arguments passed in gets turned into a dict.
def calculate(n, **kwargs):
    print(kwargs)
    # for (key, value) in kwargs.items():
    #     print(key)
    #     print(value)
    n += kwargs['add']
    n *= kwargs['multiply']
    return n


print(calculate(2, add=2, multiply=5))


class Car:
    def __init__(self, **kw):
        self.make = kw.get('make')
        self.model = kw.get('model')
        self.colour = kw.get('colour')

    def get_make(self):
        return self.make

    def get_model(self):
        return self.model

    def get_colour(self):
        return self.colour


my_car = Car(make='Nissan', model='GT-R')
print(my_car.get_make())
print(my_car.get_model())
print(my_car.get_colour())

window.mainloop()
