"""
Password Manager
"""
from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def pass_gen():
    pass_list_l = [choice(letters) for _ in range(randint(5, 8))]
    pass_list_n = [choice(numbers) for _ in range(randint(2, 5))]
    pass_list_s = [choice(symbols) for _ in range(randint(2, 4))]
    pass_list = pass_list_l + pass_list_s + pass_list_n
    shuffle(pass_list)
    password = "".join(pass_list)
    pass_box.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_pass():
    passw = pass_box.get()
    email = email_box.get()
    website = web_box.get()
    new_data = {
        website: {
            "email": email,
            "password": passw,
        }
    }

    if passw == "" or email == "" or website == "":
        messagebox.showinfo(title="Error", message="one or more text boxes are empty")
    else:
        is_ok = messagebox.askokcancel(title=website,
                                       message=f"These are the details entered:\nEmail: {email}\nPassword: {passw}\n\nIs it OK to save?")
        if is_ok:
            try:
                with open("data.json", "r") as f:
                    data = json.load(f)
                    data.update(new_data)
            except FileNotFoundError:
                with open("data.json", "w") as f:
                    json.dump(new_data, f, indent=4)
            else:
                with open("data.json", "w") as f:
                    json.dump(data, f, indent=4)
            finally:
                pass_box.delete(0, END)
                web_box.delete(0, END)


# ---------------------------- Search Website ------------------------------- #
def search():
    try:
        with open("data.json", "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="There are no saved passwords.")
    else:
        if web_box.get() in data:
            data_pass = data[web_box.get()]["password"]
            data_email = data[web_box.get()]["email"]
            messagebox.showinfo(title=f"{web_box.get()}",
                                message=f"the login info for the website {web_box.get()} is: \nEmail/Username: {data_email} \nPassword: {data_pass}")
        else:
            messagebox.showinfo(title="Error", message=f"There is no saved password for the website {web_box.get()} check spelling and try again.")




# ---------------------------- UI SETUP ------------------------------- #
# window initialization
window = Tk()
window.title("Password Manager")
window.config(padx=40, pady=40)

# canvas initialization
canvas = Canvas(width=200, height=200)
logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(column=1, row=0)

# Labels
web_label = Label(text="Website:")
web_label.grid(column=0, row=1)

email_label = Label(text="Email/Username:")
email_label.grid(column=0, row=2)

pass_label = Label(text="Password")
pass_label.grid(column=0, row=3)

# Text boxes
web_box = Entry(width=21)
web_box.focus()
web_box.grid(column=1, row=1)

email_box = Entry(width=35)
email_box.insert(0, "gg@gmail.com")
email_box.grid(column=1, row=2, columnspan=2)

pass_box = Entry(width=21)
pass_box.grid(column=1, row=3)

# button
add_button = Button(text="Add", width=36, command=save_pass)
add_button.grid(column=1, row=4, columnspan=2)

add_button = Button(text="Generate", width=11, command=pass_gen)
add_button.grid(column=2, row=3)

add_button = Button(text="Search", width=11, command=search)
add_button.grid(column=2, row=1)

window.mainloop()
