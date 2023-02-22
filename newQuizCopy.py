# Importing Dependencies
import sys
from tkinter import *
from tkinter import messagebox
import sqlite3
from tkinter import ttk

# Accessing the Title and Subject entered by the Admin
exportedFromDash = sys.argv
subject = exportedFromDash[-1]
title = exportedFromDash[-2]
# print(title + " || "+subject)


# GUI window
newQuizApp = Tk()
newQuizApp.geometry('1520x700')
newQuizApp.title("Add Questions")
newQuizApp.config(bg="white")

# Images
framebg = PhotoImage(
    file=r'C:\sandesh\Python\tkinterrr\FirstSem Project - Copy\Khichadi\framebg.png')
qnsEntBg = PhotoImage(
    file=r'C:\sandesh\Python\tkinterrr\FirstSem Project - Copy\Khichadi\qnsentry.png')
optEntBg = PhotoImage(
    file=r'C:\sandesh\Python\tkinterrr\FirstSem Project - Copy\Khichadi\optionsent.png')
addBtn = PhotoImage(
    file=r'C:\sandesh\Python\tkinterrr\FirstSem Project - Copy\Khichadi\add btn.png')


# Title and Subject
tit = Label(newQuizApp, text="Quiz Title Here", bg="White",
            fg="#000234", font=("Poppins 30"))
tit.place(x=570, y=0)
subj = Label(newQuizApp, text="Subject", bg="White",
             fg="#7A6A6A", font=("Poppins 20"))
subj.place(x=650, y=40)

# Add Question
divText = Label(newQuizApp, text="Add Question",
                bg="White", fg="black", font=("Poppins 24"))
divText.place(x=10, y=55)

# ----Add Question Frame--------
container = Frame(newQuizApp, bg="white", height=200, width=800)
container.place(x=10, y=100)

# --Placing the background rectangle
bglabel = Label(container, image=framebg, bg="white")
bglabel.pack()

# Question ENtry
questionEntBg = Label(container, image=qnsEntBg, bg="#F9ECEC")
questionEntBg.place(x=15, y=10)
questionEnt = Entry(container, width=38, borderwidth=0, bd=0,
                    bg="#D9D9D9", font=("Berlin Sans FB", 18), fg="gray")
questionEnt.place(x=25, y=17)

# Option1:
option1Lab = Label(container, text="Option 1:",
                   font=("Candara 22"), bg="#F9ECEC")
option1Lab.place(x=100, y=95)
option1box = Label(container, image=optEntBg, bg="#F9ECEC")
option1box.place(x=260, y=100)
option1Ent = Entry(container, width=16, borderwidth=0, bd=0,
                   bg="#D9D9D9", font=("Berlin Sans FB", 15), fg="gray")
option1Ent.place(x=270, y=106)

# Option2:
option2Lab = Label(container, text="Option 2:",
                   font=("Candara 22"), bg="#F9ECEC")
option2Lab.place(x=100, y=160)
option2box = Label(container, image=optEntBg, bg="#F9ECEC")
option2box.place(x=260, y=165)
option2Ent = Entry(container, width=16, borderwidth=0, bd=0,
                   bg="#D9D9D9", font=("Berlin Sans FB", 15), fg="gray")
option2Ent.place(x=270, y=171)

# Option3:
option3Lab = Label(container, text="Option 3:",
                   font=("Candara 22"), bg="#F9ECEC")
option3Lab.place(x=100, y=225)
option3box = Label(container, image=optEntBg, bg="#F9ECEC")
option3box.place(x=260, y=230)
option3Ent = Entry(container, width=16, borderwidth=0, bd=0,
                   bg="#D9D9D9", font=("Berlin Sans FB", 15), fg="gray")
option3Ent.place(x=270, y=236)

# Option4:
option4Lab = Label(container, text="Option 4:",
                   font=("Candara 22"), bg="#F9ECEC")
option4Lab.place(x=100, y=290)
option4box = Label(container, image=optEntBg, bg="#F9ECEC")
option4box.place(x=260, y=295)
option4Ent = Entry(container, width=16, borderwidth=0, bd=0,
                   bg="#D9D9D9", font=("Berlin Sans FB", 15), fg="gray")
option4Ent.place(x=270, y=301)

# Correct Option:
correctOptLab = Label(container, text="Answer:",
                      font=("Candara 22"), bg="#F9ECEC")
correctOptLab.place(x=100, y=355)

correctOptCombo = ttk.Combobox(
    container, state='readonly', width=35, font=("Poppins 20", 13, "bold"))
correctOptCombo['values'] = ("Option 1", "Option 2", "Option 3", "Option 4")

correctOptCombo.current()
correctOptCombo.place(x=260, y=360, width=200)


# Clear all Fields:
def clear():
    questionEnt.delete(0, "end")
    option1Ent.delete(0, 'end')
    option2Ent.delete(0, 'end')
    option3Ent.delete(0, 'end')
    option4Ent.delete(0, 'end')
    correctOptCombo.current()
# correctOptCombo.delete()
# Add Func


def fetchqns():
    # Question Listing
    conn = sqlite3.connect('quizes.db')
    cur = conn.cursor()
    cur.execute(f"SELECT * FROM {title}")

    rows = cur.fetchall()
    tree = ttk.Treeview(newQuizApp, columns=(
        "ID", "Questions"), show="headings")
    tree.column("ID", width=50, anchor="center")
    tree.column("Questions", width=300, anchor="center")
    tree.heading("ID", text="ID")
    tree.heading("Questions", text="Questions")
    tree.place(x=700, y=100)

    # inserting data into table:
    for row in rows:
        tree.insert("", "end", values=row)
    conn.commit()
    conn.close()


fetchqns()


def addQns():
    try:
        conn = sqlite3.connect('quizes.db')
        cur = conn.cursor()
        cur.execute(f"INSERT INTO {title}(Questions, Option1, Option2, Option3, Option4, Answer) VALUES(?,?,?,?,?,?)",
                    (questionEnt.get(), option1Ent.get(), option2Ent.get(), option3Ent.get(), option4Ent.get(), correctOptCombo.get()))
        conn.commit()
        conn.close()
        clear()
        fetchqns()
    except:
        messagebox.showerror("Error", "Something went Wrong!")
    # clear()


# Button
btn = Button(container, image=addBtn, bg="#CACCD2", bd=0,
             borderwidth=0, activebackground="#CACCD2", command=addQns)
btn.place(x=280, y=415)

newQuizApp.mainloop()
