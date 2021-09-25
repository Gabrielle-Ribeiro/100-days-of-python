from tkinter import *

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

canvas = Canvas(width=200, height=200)
password_logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=password_logo)
canvas.grid(column=1, row=0)

website_label = Label(text="Website:")
website_label.grid(column=0, row=1)

website_entry = Entry(width=45)
website_entry.grid(column=1, row=1, columnspan=2, sticky=W)

username_label = Label(text="Email/Username:")
username_label.grid(column=0, row=2)

username_entry = Entry(width=45)
username_entry.grid(column=1, row=2, columnspan=2, sticky=W)

password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

password_entry = Entry(width=25)
password_entry.grid(column=1, row=3, sticky=W)

generate_password_button = Button(text="Generate Password", width=13)
generate_password_button.grid(column=2, row=3, sticky=W)

add_button = Button(text="Add", width=42)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()