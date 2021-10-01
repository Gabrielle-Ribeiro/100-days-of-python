from tkinter import *
from tkinter import messagebox
import random
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 
               'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 
               'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 
               'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters = ""
    for i in range(0, nr_letters):
        password_letters += random.choice(letters)

    password_symbols = ""
    for i in range(0, nr_symbols):
        password_symbols += random.choice(symbols)

    password_numbers = ""
    for i in range(0, nr_numbers):
        password_numbers += random.choice(numbers)

    password = password_letters + password_symbols + password_numbers
    password = "".join(random.sample(password, len(password)))

    password_entry.delete(0, END)
    password_entry.insert(0, password)

# ---------------------------- SAVE PASSWORD ------------------------------- #

def get_entries():
    website_name = website_entry.get()
    username = username_entry.get()
    password = password_entry.get()
    new_data = {
        website_name: {
            "email": username,
            "password": password,
        }
    }

    if len(website_name) == 0 or len(username) == 0 or len(password) == 0:
        messagebox.showinfo(title='Oops', message="Please don't leave any fields empty!")
    else:
        is_ok = messagebox.askokcancel(title=website_name,
                                        message=f'These are the details entered: \nEmail: {username}'
                                                f'\nPassword: {password} \nIs it ok to save?')

        if is_ok:
            try:
                with open("data.json", "r") as file:
                    data = json.load(file)
            except FileNotFoundError:
                with open("data.json", "w") as file:
                    json.dump(new_data, file, indent=4)
            else:
                data.update(new_data)
                with open("data.json", "w") as file:
                    json.dump(data, file, indent=4)
            
        username_entry.delete(0, END)
        username_entry.insert(0, "gabrielleribeiro2010@gmail.com")
        website_entry.delete(0, END)
        password_entry.delete(0, END)

# ---------------------------- SEARCH PASSWORD ------------------------ #

def search_website():
    website_name = website_entry.get()

    if website_name == "":
        messagebox.showinfo(title='Oops', message="Please don't leave Website field empty!")
    else:
        try:
            with open("data.json", "r") as file:
                data = json.load(file)
        except FileNotFoundError:
            messagebox.showinfo(title='Oops', message="There's no website registered yet!")
        else:
            try:
                website_info = data[website_name]
            except KeyError:
                messagebox.showinfo(title='Oops', message=f"{website_name} is not registered yet!")
            else:
                username = website_info["email"]
                password = website_info["password"]
                messagebox.showinfo(title=f'{website_name} info', 
                                    message=f"{website_name} \n\nUsername: {username} \n\nPassword: {password}")





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

website_entry = Entry(width=25)
website_entry.grid(column=1, row=1, sticky=W)
website_entry.focus()

search_button = Button(text="Search", width=13, command=search_website)
search_button.grid(column=2, row=1, sticky=W)

username_label = Label(text="Email/Username:")
username_label.grid(column=0, row=2)

username_entry = Entry(width=45)
username_entry.grid(column=1, row=2, columnspan=2, sticky=W)
username_entry.insert(0, "gabrielleribeiro2010@gmail.com")

password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

password_entry = Entry(width=25)
password_entry.grid(column=1, row=3, sticky=W)

generate_password_button = Button(text="Generate Password", width=13, command=generate_password)
generate_password_button.grid(column=2, row=3, sticky=W)

add_button = Button(text="Add", width=42, command=get_entries)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()