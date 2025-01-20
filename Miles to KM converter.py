from tkinter import *

#Window config
window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=300, height=100)

#Label(Blank Space)
my_label = Label(text="")
my_label.grid(column=0, row=0)

#Output Label
output_label = Label(text=0)
output_label.grid(column=2, row=1)


def convert():
    miles = input.get()
    miles_float = float(miles)
    km = round(miles_float * 1.60934)
    output_label.config(text=km)


#Input
input = Entry(width=15)
input.grid(column=2, row=0)

#Label(Miles)
my_label = Label(text="Miles")
my_label.grid(column=3, row=0)

#Label(is equal to)
my_label = Label(text="is equal to")
my_label.grid(column=1, row=1)

#Label(KM)
my_label = Label(text="Km")
my_label.grid(column=3, row=1)

#Button
my_button = Button(text="Calculate", command=convert)
my_button.grid(column=2, row=3)

window.mainloop()
