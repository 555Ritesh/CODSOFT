# TASK-3 :- PASSWORD GENERATOR


import random
import string
from tkinter import *
import tkinter as tk  # Add this line to import tkinter module
from tkinter import messagebox

def generate_random_password():
    password = ""
    for _ in range(password_length.get()):
        char_type = random.choice(all_combinations)
        password += random.choice(char_type)

    generated_password.set(password)

def copy_to_clipboard():
    root.clipboard_clear()
    root.clipboard_append(generated_password.get())
    root.update()
    messagebox.showinfo("Copied", "Password copied to clipboard.")

root = Tk()
root.geometry("350x350")
root.title("Random Password Generator")

all_combinations = [string.punctuation, string.ascii_uppercase, string.digits, string.ascii_lowercase]

password_length = IntVar()
password_label = Label(root, text='Enter Password Length', font='Comfortaa 12 bold').pack(pady=10)
password_entry = Spinbox(root, from_=4, to_=32, textvariable=password_length, width=20, font='arial 16').pack()

generate_button = Button(root, command=generate_random_password, text="Generate Password", font="Arial 10", bg='#B2FE03', fg='black', activebackground="teal", padx=5, pady=5).pack(pady=20)

generated_password_label = Label(root, text='Random Generated Password', font='Comfortaa 12 bold').pack(pady="30 10")
generated_password = StringVar()
generated_password_entry = Entry(root, textvariable=generated_password, width=20, font='arial 16').pack()

copy_button = Button(root, text='Copy to Clipboard', command=copy_to_clipboard, font="Arial 10", bg='#FEEB03', fg='black', activebackground="teal", padx=5, pady=5).pack(pady=20)

root.mainloop()


