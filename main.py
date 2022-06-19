import json
from tkinter import *
from tkinter import messagebox
from random import randint, shuffle, choice
import pyperclip


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letter = [choice(letters) for _ in range(randint(8, 10))]

    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]

    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letter + password_symbols + password_numbers

    shuffle(password_list)

    passwd = "".join(password_list)

    password_entry.delete(0, END)
    password_entry.insert(0, passwd)
    pyperclip.copy(passwd)


# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    webx = website_entry.get()
    emailx = email_entry.get()
    passwordx = password_entry.get()

    json_data = {
        webx: {
            "Email": emailx,
            "Password": passwordx
        }
    }

    if len(webx) == 0 or len(passwordx) == 0 or len(emailx) == 0:
        messagebox.showinfo(title="Opps", message="please make sure you haven't left any filed left empty")

    else:
        try:
            with open('data.json', mode='r') as data_file:
                data = json.load(data_file)

        except FileNotFoundError:
            with open('data.json', mode='w') as data_file:
                json.dump(json_data, data_file, indent=4)

        else:
            data.update(json_data)

            with open('data.json', mode='w') as data_file:
                json.dump(data, data_file, indent=4)

        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)
            email_entry.delete(0, END)


# ---------------------------- FIND PASSWORD ------------------------------- #

def find_password():
    webx = website_entry.get()
    try:
        with open('data.json', "r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="This file didn't Exist")

    else:
        if webx in data:
            Email = data[webx]["Email"]
            Password = data[webx]["Password"]

            messagebox.showinfo(title=webx, message=f"Email : {Email}\nPassword : {Password}")

        else:
            messagebox.showinfo(title="Error", message="This data didn't Exist")


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
img = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=img)
canvas.grid(row=0, column=1)

# label

website = Label(text="Website :")
website.grid(row=1, column=0)

email = Label(text="Email/Username :")
email.grid(row=2, column=0)

password = Label(text="Password :")
password.grid(row=3, column=0)

# Entry

website_entry = Entry(width=35)
website_entry.focus()
website_entry.grid(row=1, column=1)

email_entry = Entry(width=35)
email_entry.grid(row=2, column=1)

password_entry = Entry(width=35)
password_entry.grid(row=3, column=1)

# Button

generate_password_button = Button(text="Generate Password", command=generate_password)
generate_password_button.grid(row=3, column=2)

search_button = Button(text="Search", width=14, command=find_password)
search_button.grid(row=1, column=2)

add_button = Button(text="Add", width=20, command=save)
add_button.grid(row=4, column=1)

window.mainloop()
