# Importing dependencies
from tkinter import *
from tkinter import ttk
import runpy
from tkinter import messagebox
from PIL import Image, ImageTk
import sqlite3
import sys
import subprocess


# Which Student Logged in ?
var = sys.argv
loggedstd = var[-1]


def openquiz():
    confirmation = messagebox.askquestion(
        "Start Quiz?", "Do you want to start the quiz?")
    if confirmation == "yes":
        # app.destroy()
        # runpy.run_path(
        #     r"C:\sandesh\Python\tkinterrr\FirstSem Project\Student's End\startquiz.py")
        subprocess.run(f"py startquiz.py {loggedstd}")


# ------UI window-----
app = Tk()
app.geometry("1920x1080")
app.title("Admin Home ~ EzyQzy")
app.config(bg="white")


# -----ALl images------

# Admin Head
adminicon = PhotoImage(
    file="C:\\sandesh\\Python\\tkinterrr\\FirstSem Project\\Student's End\\Images\\stdhead.png")
# Home Button SELECTED
homebtnimg = PhotoImage(
    file="C:\\sandesh\\Python\\tkinterrr\\FirstSem Project\\Student's End\\Images\\homebtn.png")
# Create Quiz Button SELECTED
quizesbtnimg = PhotoImage(
    file="C:\\sandesh\\Python\\tkinterrr\\FirstSem Project\\Student's End\\Images\\quizesbtn.png")
# Recent Button SELECTED
historybtnimg = PhotoImage(
    file="C:\\sandesh\\Python\\tkinterrr\\FirstSem Project\\Student's End\\Images\\historybtn.png")
# Result Button SELECTED
resultbtnimg = PhotoImage(
    file="C:\\sandesh\\Python\\tkinterrr\\FirstSem Project\\Student's End\\Images\\resultbtn.png")
# Leaderboard Button SELECTED
leaderboardbtnimg = PhotoImage(
    file="C:\\sandesh\\Python\\tkinterrr\\FirstSem Project\\Student's End\\Images\\leaderboardbtn.png")
# Student Button SELECTED
studentbtnimg = PhotoImage(
    file="C:\\sandesh\\Python\\tkinterrr\\FirstSem Project\\Student's End\\Images\\studentsbtn.png")
# Logo
logo = PhotoImage(
    file=r"C:\sandesh\Python\tkinterrr\FirstSem Project - Copy\Khichadi\logo.png")
# Create Icon
quizesIcon = PhotoImage(
    file="C:\\sandesh\\Python\\tkinterrr\\FirstSem Project\\Student's End\\Images\\quizesicon.png")
# dash Icon
homeIcon = PhotoImage(
    file="C:\\sandesh\\Python\\tkinterrr\\FirstSem Project\\Student's End\\Images\\homeicon.png")
# recent Icon
historyIcon = PhotoImage(
    file="C:\\sandesh\\Python\\tkinterrr\\FirstSem Project\\Student's End\\Images\\recent_icon.png")
# result Icon
resultIcon = PhotoImage(
    file="C:\\sandesh\\Python\\tkinterrr\\FirstSem Project\\Student's End\\Images\\result_icon.png")
# laderboard Icon
leaderboardIcon = PhotoImage(
    file="C:\\sandesh\\Python\\tkinterrr\\FirstSem Project\\Student's End\\Images\\leaderboard_icon.png")
# Students Icon
studentsIcon = PhotoImage(
    file="C:\\sandesh\\Python\\tkinterrr\\FirstSem Project\\Student's End\\Images\\studentsicon.png")
# logout Icon
logoutIcon = PhotoImage(
    file="C:\\sandesh\\Python\\tkinterrr\\FirstSem Project\\Student's End\\Images\\logout_icon.png")
# logout Icon
homeIllus = PhotoImage(
    file=r"C:\sandesh\Python\tkinterrr\FirstSem Project - Copy\Khichadi\stdhomeillus.png")
# logout Icon
changepswdimg = PhotoImage(
    file=r"C:\sandesh\Python\tkinterrr\FirstSem Project - Copy\Khichadi\changepwd.png")
# Entry
entrybg = PhotoImage(
    file=r"C:\sandesh\Python\tkinterrr\FirstSem Project - Copy\Khichadi\optionsent.png")
# Entry
updateBut = PhotoImage(
    file=r"C:\sandesh\Python\tkinterrr\FirstSem Project - Copy\Khichadi\updatebtn.png")


# ------------Nav Section----------------------
# Creating a Frame
navframe = Frame(app, bg="#22A5BB", width=1920, height=70, bd=0)
navframe.pack(side="top")
# # Inserting the Gradient Image with Label
# nav = Label(navframe, image=navimg, bd=0)
# nav.pack()
# Logo
navlogo = Label(app, image=logo, bg="#22A5BB")
navlogo.place(x=0, y=0)

# -----------------------------------------------------
# Enroll New Students:


def logoutFun():
    yesorno = messagebox.askquestion(
        "Logout?", "Are you sure you want to Logout?")
    if yesorno == "yes":
        app.destroy()
        runpy.run_path(
            r"C:\sandesh\Python\tkinterrr\FirstSem Project - Copy\Khichadi\start.py")


def enrollNew():
    app.destroy()
    runpy.run_path(
        r"C:\sandesh\Python\tkinterrr\FirstSem Project\Admin Dash\enroll.py")

# ---------------PAGES FUNCTIONS-----------------------
# ----------------Home DIV -----------------


def homeFun():
    homebtn.config(image=homebtnimg, borderwidth=0, bd=0, text='',
                   bg="#2B4320", activebackground="#2B4320", padx=0)
    quizesbtn.config(image=quizesIcon, text="Quizes", font=(
        "Poppins 20"), compound="left", padx=20, borderwidth=0, bd=0, bg="#2B4320", fg="white", activebackground="#2B4320", activeforeground="white")
    historybtn.config(image=historyIcon, text="History", padx=20, font=(
        "Poppins 20"), compound="left", borderwidth=0, bd=0, bg="#2B4320", fg="white", activebackground="#2B4320", activeforeground="white")
    dashFrame = Frame(app, bg="white", width=1080, height=1010)
    dashFrame.place(x=300, y=70)
    header = Label(dashFrame, text="Welcome to EzyQzy!", font="Poppins 40",
                   fg="#2F3646", bg="white")
    header.place(x=300, y=20)

    illus = Label(dashFrame, image=homeIllus, bg="white")
    illus.place(x=80, y=160)
    instruct = Frame(dashFrame, bg="#000234", height=450, width=450)
    instruct.place(x=570, y=140)
    tit = Label(instruct, text="QUICK GUIDE", font=(
        "Harrington", 34, 'bold'), fg="white", bg="#000234")
    tit.place(x=80, y=10)
    tips1 = Label(instruct, text="- Goto the ‘Quizes’ tab to attempt \n the quizes created by the Admin.",
                  font=("Cascadia Code", 16), fg="white", bg="#000234", anchor="e", justify=LEFT)
    tips1.place(x=10, y=120)
    tips2 = Label(instruct, text="- You can view your scores in the \n ‘History’ tab.",
                  font=("Cascadia Code", 16), fg="white", bg="#000234", anchor="e", justify=LEFT)
    tips2.place(x=10, y=230)
    tips3 = Label(instruct, text="Happy Learning!",
                  font=("Cascadia Code", 20), fg="white", bg="#000234",)
    tips3.place(x=120, y=400)

# -----------My History--------------


def quizesFun():
    createQuizFrame = Frame(
        app, bg="white", width=1080, height=1010)
    createQuizFrame.place(x=300, y=70)
    quizesbtn.config(image=quizesbtnimg, padx=0, text="", pady=10)
    homebtn.config(image=homeIcon, text="Home", padx=20, font=(
        "Poppins 20"), compound="left", borderwidth=0, bd=0, bg="#2B4320", fg="white", activebackground="#2B4320", activeforeground="white")
    historybtn.config(image=historyIcon, text="History", padx=20, font=(
        "Poppins 20"), compound="left", borderwidth=0, bd=0, bg="#2B4320", fg="white", activebackground="#2B4320", activeforeground="white")

    header = Label(createQuizFrame, text="Quizes", font="Poppins 40",
                   fg="#2F3646", bg="white")
    header.place(x=13, y=10)

    # connecting with the database:
    conn = sqlite3.connect('quizes.db')
    cur = conn.cursor()
    cur.execute(
        "SELECT name FROM sqlite_master WHERE type='table' AND name != 'sqlite_sequence'")
    tables = list(cur.fetchall())

    i = 100
    for table in tables:
        # cur.execute(f"SELECT * FROM {table}")
        card = Frame(createQuizFrame, bg="Purple", width=400, height=120)
        card.place(x=20, y=i)
        global title
        title = table
        cardtit = Label(card, text=title, font=(
            "Poppins 20"), bg="Purple", fg="White")
        cardtit.place(x=3, y=5)
        cardbtn = Button(card, text="Attempt", font=("Poppins 18"),
                         bd=0, fg="White", bg="Brown", command=openquiz)
        cardbtn.place(x=150, y=70)
        i += 125
# ------------RECENT QUIZ DIV---------------


def historyFun():
    historybtn.config(image=historybtnimg, padx=0, text="", pady=10)
    homebtn.config(image=homeIcon, text="Home", padx=20, font=(
        "Poppins 20"), compound="left", borderwidth=0, bd=0, bg="#2B4320", fg="white", activebackground="#2B4320", activeforeground="white")
    quizesbtn.config(image=quizesIcon, text="Quizes", padx=20, font=("Poppins 20"), compound="left",
                     borderwidth=0, bd=0, bg="#2B4320", fg="white", activebackground="#2B4320", activeforeground="white")

    recentQuizFrame = Frame(app, bg="white", width=1080, height=1010)
    recentQuizFrame.place(x=300, y=70)
    header = Label(recentQuizFrame, text="History", font="Poppins 40",
                   fg="#2F3646", bg="white")
    header.place(x=13, y=10)

    connection = sqlite3.connect(
        'scores.db')
    # Creating cursor:
    cur = connection.cursor()
    # Querying:
    cur.execute(
        "SELECT Quiz_title, Score FROM scorechart WHERE Candidate=?", (loggedstd,))
    rows = cur.fetchall()

    style = ttk.Style()
    style.configure("mystyle.Treeview", highlightthickness=0,
                    bd=0, font=('Calibri', 15))  # Modify the font of the body
    style.configure("mystyle.Treeview.Heading", font=(
        'Calibri', 30, 'bold'))  # Modify the font of the headings
    style.layout("mystyle.Treeview", [('mystyle.Treeview.treearea', {
                 'sticky': 'nswe'})])  # Remove the borders

    # Making the TABLE:
    tree = ttk.Treeview(recentQuizFrame, style="mystyle.Treeview", columns=(
        "Quiz_title", "Score"), height=500, show="headings")
    # tree.column("SID", width=70, anchor=W)
    tree.column("Quiz_title", width=320, anchor="center")
    # tree.column("Candidate", width=320, anchor="center")
    tree.column("Score", width=320, anchor="center")
    tree.heading("Quiz_title", text="Quiz Title")
    # tree.heading("Candidate", text="Candidate")
    tree.heading("Score", text="Score")
    tree.place(x=60, y=100)

    n = len(rows)

    # test fn

    # inserting data into table:
    for row in rows:
        tree.insert("", "end", values=row)

    # Closing the Connection with DB
    connection.close()


# ----------------Side Bar----------------
# Creating a Frame
sideframe = Frame(app, width=300, height=1080, bg="#2B4320", bd=0)
sideframe.pack(side="left")
# # Inserting Gradient Image with Label
# sidebar = Label(sideframe, image=sidenav, bd=0)
# sidebar.pack()
# Admin Icon
adico = Label(app, image=adminicon, bd=0, bg="#2B4320")
adico.place(x=100, y=100)
# Hello Username
# Fetching Username

msg = Label(app, text=f"Hello, @{loggedstd}!", bg="#2B4320",
            font=("Poppins 16"), fg="white")
msg.place(x=70, y=200)

# ----Side Menu----

# Home Button SELECTED
homebtn = Button(app, image=homebtnimg, borderwidth=0, bd=0,
                 bg="#2B4320", activebackground="#2B4320", command=homeFun)
homebtn.place(x=0, y=250)

# Quizes Button
quizesbtn = Button(app, image=quizesIcon, text="Quizes", padx=20, font=(
    "Poppins 20"), compound="left", borderwidth=0, bd=0, bg="#2B4320", fg="white", activebackground="#2B4320", activeforeground="white", command=quizesFun)
quizesbtn.place(x=0, y=310)

# History Button
historybtn = Button(app, image=historyIcon, text="History", padx=20, font=(
    "Poppins 20"), compound="left", borderwidth=0, bd=0, bg="#2B4320", fg="white", activebackground="#2B4320", activeforeground="white", command=historyFun)
historybtn.place(x=0, y=370)


# Logout Button
logoutbtn = Button(app, image=logoutIcon, text="Logout", padx=10, font=(
    "Poppins 20"), compound="left", borderwidth=0, bd=0, bg="#2B4320", fg="white", activebackground="#2B4320", activeforeground="white", command=logoutFun)
logoutbtn.place(x=50, y=640)

# ----------------C A R D S -----------------
header = Label(app, text="Home", font="Poppins 40",
               fg="#2F3646", bg="white")
header.place(x=313, y=80)
homeFun()
# ----Opening the Window-------
app.mainloop()
