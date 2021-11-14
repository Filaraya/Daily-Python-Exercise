"""
writer a program using GUI program that converts temperatures from Fahrenheit to Celsius.
"""
from tkinter import *

root = Tk()
mainloop ()

def calculate ():
"""convert temp Fahrenheit to Celsius"""
    temp = int (entry.get ())
    temp = 9/5 * temp + 32
    output_label.configure(text = 'The temprature in Fahrenheit: {:.1f}'.format(temp))
    entry.delete(0,END)
root = Tk()
message_label = Label(text='Enter a temprature in Celcius',
font=('Verdana', 16))
output_label = Label(font=('Verdana', 16))
entry = Entry(font=('Verdana', 16), width=4)
calc_button = Button(text='Ok', font=('Verdana', 16),
command=calculate)
message_label.grid(row=0, column=0)
entry.grid(row=0, column=1)
calc_button.grid(row=0, column=2)
output_label.grid(row=1, column=0, columnspan=3)
    
    
mainloop()
