from tkinter import *

window = Tk()
window.title('Mile to Km Converter')
window.minsize(width=300, height=100)
window.config(padx=20, pady=20)

entry = Entry(width=15)
entry.insert(END, string='0')
entry.grid(column=1, row=0)

label0 = Label(text='Miles')
label0.grid(column=2, row=0)
label0.config(padx=10)

label1 = Label(text='is equal to')
label1.grid(column=0, row=1)
label1.config(padx=10, pady=10)

kilometers_label = Label(text='0')
kilometers_label.grid(column=1, row=1)

label2 = Label(text='Km')
label2.grid(column=2, row=1)

def convert_mile_to_km():
    miles = float(entry.get())
    kilometers = miles * 1.60934
    kilometers_label.config(text=str(kilometers))

button = Button(text='Calculate', command=convert_mile_to_km)
button.grid(column=1, row=2)

window.mainloop()
