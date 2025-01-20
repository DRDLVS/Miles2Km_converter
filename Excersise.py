import tkinter

#Window config
window = tkinter.Tk()
window.title("Grafica")
window.minsize(width=500, height=300)



#Label
my_label = tkinter.Label(text="i am a label")
#my_label.pack()
my_label.grid(column=0, row=0)


def button_clicked():
    new_text = input.get()
    my_label.config(text=new_text)

#Button
my_button = tkinter.Button(text="Click me", command=button_clicked)
#my_button.pack()
my_button.grid(column=1, row=1)

#Button 2
my_button_2 = tkinter.Button(text="Didnt expect me here?")
#my_button_2.pack()
my_button_2.grid(column=3, row=0)

#Input
input = tkinter.Entry(width=15)
#input.pack()
input.grid(column=4, row=3)




window.mainloop()