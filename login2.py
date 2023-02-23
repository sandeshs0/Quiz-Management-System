from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox




# creating the login window
root = Tk()
root.geometry("800x800")
root.resizable(False, False)
root.title("Login As Admin")

uname = StringVar()
pas = StringVar()
# def Login():
#     global contd


def SignUp():
    global contd
# messagebox


def Login():

    if uname.get() == "" or pas.get() == "":
        messagebox.showerror("Error", "All fields are required", parent=root)
    elif uname.get() == "Puja469" and pas.get() == "123456":
        messagebox.showinfo("Successfull", f"Welcome, {uname.get()}")

    else:
        messagebox.showerror("Error", "Invalid Username or Password")


photo = PhotoImage(file="C:\\Programing\\Projects\\quizapp\\idea.png")


p = Label(root, text=" Quizify", image=photo, compound=LEFT, font=(
    "Poppins", 28, "bold")).pack(side=BOTTOM, anchor=NW, padx=250)
ima_1 = PhotoImage(file="C:\\Programing\\Projects\\quizapp\\puja(1).png")
p_2 = Label(root, image=ima_1).place(x=330, y=30)

# text
text = Label(root, text="   ADMIN  ", font=(
    "Poppins", 21, "bold"), fg="black", ).place(x=330, y=180)

# login frame
login_frame = Frame(root, bg="white")
login_frame.place(x=180, y=250, height=350, width=450)

# username
user_name = Label(login_frame, text="Username:",
                  font=("Poppins regular", 17,), bg='white')
user_name.place(x=20, y=50)

user_entry = Entry(login_frame, bg="light grey", textvariable=uname)
user_entry.place(x=160, y=60, width=200, height=30)

# password
pass_name = Label(login_frame, text="Password:",
                  font=("Poppins regular", 17,), bg='white')
pass_name.place(x=20, y=135)

pass_entry = Entry(login_frame, bg="light grey", textvariable=pas)
pass_entry.place(x=160, y=140, width=200, height=30)

# login button
log_btn = PhotoImage(file="C:\\Programing\\Projects\\quizapp\Rectangle 1.png")

# creating a button and passing the image
button = Button(login_frame, image=log_btn, command=Login,
                borderwidth=0, bg="white", activebackground="white")
button. place(x=150, y=230)


# text

text_1 = Label(root, text="Don't have an account?", font=(
    "Poppins ", 16, "bold"), fg="black").place(x=210, y=640)

# signup button
sign_btn = PhotoImage(
    file="C:\\Programing\\Projects\\quizapp\\Rectangle 2.png")

button = Button(root, image=sign_btn, command=SignUp,
                borderwidth=0, bg="white", activebackground="white")
button.place(x=470, y=630)


root.mainloop()

 