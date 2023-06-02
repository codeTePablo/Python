from tkinter import * 
from tkinter import messagebox
import random as rd
# import pyperclip
import json

FONT_NAME = "Courier"
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    password_letters = [rd.choice(letters) for _ in range(rd.randint(8,10))]
    password_numbers = [rd.choice(numbers) for _ in range(rd.randint(2,4))]
    password_symbols = [rd.choice(symbols) for _ in range(rd.randint(2,4))]
    password_list = password_letters + password_numbers + password_symbols
    #
    # shuffle(password_list)
    password = "".join(password_list)
    password_entry.insert(0, password)
    print(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    webside =  website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        webside : {
            "email":email,
            "password":password 
        }
    }

    if len(webside) == 0 or len(password) == 0:
        messagebox.showerror(message="Please fill out webside and password")
        # messagebox.showinfo(title="Save", message=f"You save this: \nWebside: {webside}\nemail: {email}\npassword: {password}")
    else:
        try:
            # 'a' is to create file 
            # 'r' is to read file
            # write in json 
            with open("data.json", "r") as data_file:
                # data_file.write(f"{webside} | {email} | {password}\n") # old format to save data
                data = json.load(data_file) # reading data inside file
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            data.update(new_data) # update old to new data 
            with open("data.json", "w") as data_file:
                json.dump(data, data_file, indent=4) # saving data and insert dict
                # reset fiels of entry
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)

# ---------------------------- SEARCH PASSWORD ------------------------------- #

def find_password():
    webside_to_find =  website_entry.get()
    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showerror(message="None webside")
    else:   
        if webside_to_find in data:
            password = data[webside_to_find]["password"] # 
            messagebox.showinfo(title=webside_to_find, message=f"You password: {password}")
        else:
            messagebox.showinfo(title="Error", message=f"No details for {webside_to_find}")

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

#Labels
website_label = Label(text="Website:")
website_label.grid(row=1, column=0)
email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0)
password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

#Entries
website_entry = Entry(width=35)
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.focus()
email_entry = Entry(width=35)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, "pablo@gmail.com")
password_entry = Entry(width=21)
password_entry.grid(row=3, column=1)

# Buttons
generate_password_button = Button(text="Generate Password", command=generate_password)
generate_password_button.grid(row=3, column=2)
search_website = Button(text="Search", command=find_password)
search_website.grid(row=1, column=2, columnspan=2)
add_button = Button(text="Add", width=36, command=save)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()