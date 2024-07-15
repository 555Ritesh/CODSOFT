# CONTACT BOOK


from tkinter import *
from tkinter import messagebox

root = Tk()
root.geometry('600x550')  
root.config(bg='#FBFF00')
root.title('Contact Book')
root.resizable(0, 0)

contactlist = [
    ['Navnath Gite', '785254712'],
    ['Harsh Gaikwad', '902355222'],
    ['Balasaheb Hinge', '89124563'],
    ['Vishvesh Chavan', '56345246'],
    ['Sanket Dadali', '5846945'],
    ['Krushnakant Babalsure', '941246673']

]

Name = StringVar()
Number = StringVar()

frame = Frame(root)
frame.pack(side=RIGHT)

scroll = Scrollbar(frame, orient=VERTICAL)
select = Listbox(frame, yscrollcommand=scroll.set, font=('Times new roman', 16),
                 bg="#f0fffc", width=20, height=20, borderwidth=3, relief="groove")
scroll.config(command=select.yview)
scroll.pack(side=RIGHT, fill=Y)
select.pack(side=LEFT, fill=BOTH, expand=1)


def Selected():
    if len(select.curselection()) == 0:
        messagebox.showerror("Error", "Please Select the Name")
    else:
        return int(select.curselection()[0])


def AddContact():
    if Name.get() != "" and Number.get() != "":
        contactlist.append([Name.get(), Number.get()])
        Select_set()
        EntryReset()
        messagebox.showinfo("Confirmation", "Successfully Add New Contact")
    else:
        messagebox.showerror("Error", "Please fill in the information")


def UpdateDetail():
    if Name.get() and Number.get():
        contactlist[Selected()] = [Name.get(), Number.get()]
        messagebox.showinfo("Confirmation", "Successfully Update Contact")
        EntryReset()
        Select_set()
    elif not (Name.get()) and not (Number.get()) and not (len(select.curselection()) == 0):
        messagebox.showerror("Error", "Please fill in the information")
    else:
        if len(select.curselection()) == 0:
            messagebox.showerror("Error", "Please Select the Name and \n press Load button")
        else:
            message1 = """To Load the all information of \n 
                          selected row press Load button\n.
                          """
            messagebox.showerror("Error", message1)


def EntryReset():
    Name.set('')
    Number.set()


def Delete_Entry():
    if len(select.curselection()) != 0:
        result = messagebox.askyesno('Confirmation', 'You Want to Delete Contact\n Which you selected')
        if result:
            del contactlist[Selected()]
            Select_set()
    else:
        messagebox.showerror("Error", 'Please select the Contact')


def VIEW():
    NAME, PHONE = contactlist[Selected()]
    Name.set(NAME)
    Number.set(PHONE)


def EXIT():
    root.destroy()


def Select_set():
    contactlist.sort()
    select.delete(0, END)
    for name, phone in contactlist:
        select.insert(END, name)


Select_set()

Label(root, text='Name :', font=("Times new roman", 20, "bold"),bg='#FBFF00').place(x=20, y=20)
Entry(root, textvariable=Name, width=25).place(x=180, y=30)  
Label(root, text='Contact No :', font=("Times new roman", 20, "bold"), bg='#FBFF00').place(x=20, y=70)
Entry(root, textvariable=Number, width=25).place(x=180, y=80)  

button_width = 8 
Button(root, text="ADD", font='verdana 15 bold', bg='#5DFF00', command=AddContact, padx=10, pady=8,
       width=button_width).place(x=50, y=140)
Button(root, text="EDIT", font='verdana 15 bold', bg='#5DFF00', command=UpdateDetail, padx=10, pady=8,
       width=button_width).place(x=50, y=200)
Button(root, text="DELETE", font='verdana 15 bold', bg='#5DFF00', command=Delete_Entry, padx=10, pady=8,
       width=button_width).place(x=50, y=260)
Button(root, text="VIEW", font='verdana 15 bold', bg='#5DFF00', command=VIEW, padx=10, pady=8,
       width=button_width).place(x=50, y=320)
Button(root, text="RESET", font='verdana 15 bold', bg='#5DFF00', command=EntryReset, padx=10, pady=8,
       width=button_width).place(x=50, y=380)
Button(root, text="EXIT", font='verdana 15 bold', bg='#FF0000', command=EXIT, padx=10, pady=8,
       width=button_width).place(x=50, y=460)

root.mainloop()


