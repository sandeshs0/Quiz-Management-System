# Importing dependencies
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk

# ------UI window-----
app = Tk()
app.geometry("1920x1080")
app.title("Admin Dashboard ~ EzyQzy")
app.config(bg="white")

# -----ALl images------

# Nav Bar Gradient
navimg = PhotoImage(
    file="C:\\sandesh\\Python\\tkinterrr\\FirstSem Project\\Admin Dash\\Images\\nav.png")
# Side Bar Gradient
sidenav = PhotoImage(
    file="C:\\sandesh\\Python\\tkinterrr\\FirstSem Project\\Admin Dash\\Images\\sidebar.png")
# Admin Head
adminicon = PhotoImage(
    file="C:\\sandesh\\Python\\tkinterrr\\FirstSem Project\\Admin Dash\\Images\\adminhead.png")
# Dashboard Button SELECTED
dashbtnimg = PhotoImage(
    file="C:\\sandesh\\Python\\tkinterrr\\FirstSem Project\\Admin Dash\\Images\\Dashbtn.png")
# Create Quiz Button SELECTED
createbtnimg = PhotoImage(
    file="C:\\sandesh\\Python\\tkinterrr\\FirstSem Project\\Admin Dash\\Images\\createbtn.png")
# Recent Button SELECTED
recentbtnimg = PhotoImage(
    file="C:\\sandesh\\Python\\tkinterrr\\FirstSem Project\\Admin Dash\\Images\\recentbtn.png")
# Result Button SELECTED
resultbtnimg = PhotoImage(
    file="C:\\sandesh\\Python\\tkinterrr\\FirstSem Project\\Admin Dash\\Images\\resultbtn.png")
# Leaderboard Button SELECTED
leaderboardbtnimg = PhotoImage(
    file="C:\\sandesh\\Python\\tkinterrr\\FirstSem Project\\Admin Dash\\Images\\leaderboardbtn.png")
# Logo
logo = PhotoImage(
    file="C:\\sandesh\\Python\\tkinterrr\\FirstSem Project\\Admin Dash\\Images\\logo.png")
# Create Icon
createIcon = PhotoImage(
    file="C:\\sandesh\\Python\\tkinterrr\\FirstSem Project\\Admin Dash\\Images\\create_icon.png")
# Dash Icon
dashIcon = PhotoImage(
    file="C:\\sandesh\\Python\\tkinterrr\\FirstSem Project\\Admin Dash\\Images\\dashicon.png")
# recent Icon
recentIcon = PhotoImage(
    file="C:\\sandesh\\Python\\tkinterrr\\FirstSem Project\\Admin Dash\\Images\\recent_icon.png")
# result Icon
resultIcon = PhotoImage(
    file="C:\\sandesh\\Python\\tkinterrr\\FirstSem Project\\Admin Dash\\Images\\result_icon.png")
# laderboard Icon
leaderboardIcon = PhotoImage(
    file="C:\\sandesh\\Python\\tkinterrr\\FirstSem Project\\Admin Dash\\Images\\leaderboard_icon.png")
# logout Icon
logoutIcon = PhotoImage(
    file="C:\\sandesh\\Python\\tkinterrr\\FirstSem Project\\Admin Dash\\Images\\logout_icon.png")
# Quiz Card Imgae
QuizCardPic = PhotoImage(
    file="C:\\sandesh\\Python\\tkinterrr\\FirstSem Project\\Admin Dash\\Images\\quizswd.png")
# participant Card Imgae
participantCardPic = PhotoImage(
    file="C:\\sandesh\\Python\\tkinterrr\\FirstSem Project\\Admin Dash\\Images\\participantswd.png")
# result Card Imgae
resultCardPic = PhotoImage(
    file="C:\\sandesh\\Python\\tkinterrr\\FirstSem Project\\Admin Dash\\Images\\resultswd.png")
# View All GReen Imgae
viewAllGreen = PhotoImage(
    file="C:\\sandesh\\Python\\tkinterrr\\FirstSem Project\\Admin Dash\\Images\\viewallbtngreen.png")
# View All Yello Imgae
viewAllYellow = PhotoImage(
    file="C:\\sandesh\\Python\\tkinterrr\\FirstSem Project\\Admin Dash\\Images\\viewallbtnyellow.png")
# View All Red Imgae
viewAllRed = PhotoImage(
    file="C:\\sandesh\\Python\\tkinterrr\\FirstSem Project\\Admin Dash\\Images\\viewallbtnred.png")

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

# ----User Profile----


def profileFun():
    profileFrame = Frame(app, bg="white", width=1080, height=1010)
    profileFrame.place(x=300, y=70)
    header = Label(profileFrame, text="Admin Profile", font="Poppins 40",
                   fg="#2F3646", bg="white")
    header.place(x=13, y=10)


# DP
userdp = Image.open(
    "C:\\sandesh\\Python\\tkinterrr\\FirstSem Project\\Admin Dash\\Images\\userdp.png")
resizedp = userdp.resize((55, 55))
finaldp = ImageTk.PhotoImage(resizedp)
userprofile = Button(app, image=finaldp, text="Aladeen",
                     compound="left", font="Poppins 20", bg="#22A5BB", fg="white", padx=10, borderwidth=0, bd=0, activebackground="#22A5BB", activeforeground="white", command=profileFun)
userprofile.place(x=1170, y=4)

# -----------------------------------------------------

# ---------------PAGES FUNCTIONS-----------------------
# ----------------DASHBOARD DIV -----------------


def dashFun():
    dashbtn.config(image=dashbtnimg, borderwidth=0, bd=0, text='',
                   bg="#0E2023", activebackground="#0E2023", padx=0)
    createbtn.config(image=createIcon, text="Create Quiz", font=(
        "Poppins 20"), compound="left", padx=20, borderwidth=0, bd=0, bg="#0E2023", fg="white", activebackground="#0E2023", activeforeground="white")
    recentbtn.config(image=recentIcon, text="Recent", padx=20, font=(
        "Poppins 20"), compound="left", borderwidth=0, bd=0, bg="#0E2023", fg="white", activebackground="#0E2023", activeforeground="white")
    resultbtn.config(image=resultIcon, text="Results", padx=20, font=(
        "Poppins 20"), compound="left", borderwidth=0, bd=0, bg="#0E2023", fg="white", activebackground="#0E2023", activeforeground="white")
    leaderboardbtn.config(image=leaderboardIcon, text="Leaderboard", padx=20, font=(
        "Poppins 20"), compound="left", borderwidth=0, bd=0, bg="#0E2023", fg="white", activebackground="#0E2023", activeforeground="white")

    dashFrame = Frame(app, bg="white", width=1080, height=1010)
    dashFrame.place(x=300, y=70)
    header = Label(dashFrame, text="Dashboard", font="Poppins 40",
                   fg="#2F3646", bg="white")
    header.place(x=13, y=10)

    # ---1--Quiz Card-----
    quizCard = Frame(dashFrame, width=300, height=200, bg="#4A7A33", bd=0)
    quizCard.place(x=50, y=80)
    # Shadow Image
    quizCardImg = Label(dashFrame, image=QuizCardPic, bg="#4A7A33")
    quizCardImg.place(x=200, y=110)
    # Number
    quiznum = Label(dashFrame, text="5", font=(
        "Poppins 110"), bg="#4A7A33", fg="white")
    quiznum.place(x=60, y=110)
    # Text
    categ = Label(dashFrame, text="Quizes", font=(
        "Poppins 20"), bg="#4A7A33", fg="white")
    categ.place(x=60, y=240)

    # View All Button
    viewAllQ = Button(dashFrame, image=viewAllGreen, borderwidth=0,
                      bd=0, bg="#4A7A33", activebackground="#4A7A33")
    viewAllQ.place(x=50, y=280)

    # --2---Participants Card-----
    quizCard = Frame(dashFrame, width=300, height=200, bg="#C2A50C", bd=0)
    quizCard.place(x=370, y=80)
    # Shadow Image
    quizCardImg = Label(dashFrame, image=participantCardPic, bg="#C2A50C")
    quizCardImg.place(x=520, y=110)
    # Number
    quiznum = Label(dashFrame, text="17", font=(
        "Poppins 90"), bg="#C2A50C", fg="white")
    quiznum.place(x=380, y=110)
    # Text
    categ = Label(dashFrame, text="Participants", font=(
        "Poppins 20"), bg="#C2A50C", fg="white")
    categ.place(x=380, y=240)
    # View All Button
    viewAllQ = Button(dashFrame, image=viewAllYellow, borderwidth=0,
                      bd=0, bg="#C2A50C", activebackground="#C2A50C")
    viewAllQ.place(x=370, y=280)

    # --3---Results Card-----
    quizCard = Frame(dashFrame, width=300, height=200, bg="#D2403C", bd=0)
    quizCard.place(x=690, y=80)
    # Shadow Image
    quizCardImg = Label(dashFrame, image=resultCardPic, bg="#D2403C")
    quizCardImg.place(x=840, y=110)
    # Number
    quiznum = Label(dashFrame, text="3", font=(
        "Poppins 110"), bg="#D2403C", fg="white")
    quiznum.place(x=700, y=80)
    # Text
    categ = Label(dashFrame, text="Results", font=(
        "Poppins 20"), bg="#D2403C", fg="white")
    categ.place(x=700, y=240)
    # View All Button
    viewAllQ = Button(dashFrame, image=viewAllRed, borderwidth=0,
                      bd=0, bg="#D2403C", activebackground="#D2403C")
    viewAllQ.place(x=690, y=280)


# -----------CREATE QUIZ DIV--------------


def createQuizFun():
    createQuizFrame = Frame(app, bg="white", width=1080, height=1010)
    createQuizFrame.place(x=300, y=70)
    createbtn.config(image=createbtnimg, padx=0, text="", pady=10)
    dashbtn.config(image=dashIcon, text="Dashboard", padx=20, font=(
        "Poppins 20"), compound="left", borderwidth=0, bd=0, bg="#0E2023", fg="white", activebackground="#0E2023", activeforeground="white")
    recentbtn.config(image=recentIcon, text="Recent", padx=20, font=(
        "Poppins 20"), compound="left", borderwidth=0, bd=0, bg="#0E2023", fg="white", activebackground="#0E2023", activeforeground="white")
    resultbtn.config(image=resultIcon, text="Results", padx=20, font=(
        "Poppins 20"), compound="left", borderwidth=0, bd=0, bg="#0E2023", fg="white", activebackground="#0E2023", activeforeground="white")
    leaderboardbtn.config(image=leaderboardIcon, text="Leaderboard", padx=20, font=(
        "Poppins 20"), compound="left", borderwidth=0, bd=0, bg="#0E2023", fg="white", activebackground="#0E2023", activeforeground="white")

    header = Label(createQuizFrame, text="Create New Quiz", font="Poppins 40",
                   fg="#2F3646", bg="white")
    header.place(x=13, y=10)

# ------------RECENT QUIZ DIV---------------


def recentQuizFun():
    recentbtn.config(image=recentbtnimg, padx=0, text="", pady=10)
    dashbtn.config(image=dashIcon, text="Dashboard", padx=20, font=(
        "Poppins 20"), compound="left", borderwidth=0, bd=0, bg="#0E2023", fg="white", activebackground="#0E2023", activeforeground="white")
    createbtn.config(image=createIcon, text="Create Quiz", padx=20, font=(
        "Poppins 20"), compound="left", borderwidth=0, bd=0, bg="#0E2023", fg="white", activebackground="#0E2023", activeforeground="white")
    resultbtn.config(image=resultIcon, text="Results", padx=20, font=(
        "Poppins 20"), compound="left", borderwidth=0, bd=0, bg="#0E2023", fg="white", activebackground="#0E2023", activeforeground="white")
    leaderboardbtn.config(image=leaderboardIcon, text="Leaderboard", padx=20, font=(
        "Poppins 20"), compound="left", borderwidth=0, bd=0, bg="#0E2023", fg="white", activebackground="#0E2023", activeforeground="white")

    recentQuizFrame = Frame(app, bg="white", width=1080, height=1010)
    recentQuizFrame.place(x=300, y=70)
    header = Label(recentQuizFrame, text="Recent Quizes", font="Poppins 40",
                   fg="#2F3646", bg="white")
    header.place(x=13, y=10)

# ------------RESULTS DIV---------------


def resultsFun():
    resultbtn.config(image=resultbtnimg, padx=0, text="", pady=10)
    dashbtn.config(image=dashIcon, text="Dashboard", padx=20, font=(
        "Poppins 20"), compound="left", borderwidth=0, bd=0, bg="#0E2023", fg="white", activebackground="#0E2023", activeforeground="white")
    createbtn.config(image=createIcon, text="Create Quiz", padx=20, font=(
        "Poppins 20"), compound="left", borderwidth=0, bd=0, bg="#0E2023", fg="white", activebackground="#0E2023", activeforeground="white")
    recentbtn.config(image=recentIcon, text="Recent", padx=20, font=(
        "Poppins 20"), compound="left", borderwidth=0, bd=0, bg="#0E2023", fg="white", activebackground="#0E2023", activeforeground="white")
    leaderboardbtn.config(image=leaderboardIcon, text="Leaderboard", padx=20, font=(
        "Poppins 20"), compound="left", borderwidth=0, bd=0, bg="#0E2023", fg="white", activebackground="#0E2023", activeforeground="white")

    resultFrame = Frame(app, bg="white", width=1080, height=1010)
    resultFrame.place(x=300, y=70)
    header = Label(resultFrame, text="Results", font="Poppins 40",
                   fg="#2F3646", bg="white")
    header.place(x=13, y=10)

# ------------LEADERBOARD DIV---------------


def leaderboardFun():
    leaderboardbtn.config(image=leaderboardbtnimg, padx=0, text="", pady=10)
    dashbtn.config(image=dashIcon, text="Dashboard", padx=20, font=(
        "Poppins 20"), compound="left", borderwidth=0, bd=0, bg="#0E2023", fg="white", activebackground="#0E2023", activeforeground="white")
    createbtn.config(image=createIcon, text="Create Quiz", padx=20, font=(
        "Poppins 20"), compound="left", borderwidth=0, bd=0, bg="#0E2023", fg="white", activebackground="#0E2023", activeforeground="white")
    recentbtn.config(image=recentIcon, text="Recent", padx=20, font=(
        "Poppins 20"), compound="left", borderwidth=0, bd=0, bg="#0E2023", fg="white", activebackground="#0E2023", activeforeground="white")
    resultbtn.config(image=resultIcon, text="Results", padx=20, font=(
        "Poppins 20"), compound="left", borderwidth=0, bd=0, bg="#0E2023", fg="white", activebackground="#0E2023", activeforeground="white")

    leaderboardFrame = Frame(app, bg="white", width=1080, height=1010)
    leaderboardFrame.place(x=300, y=70)
    header = Label(leaderboardFrame, text="Leaderboard", font="Poppins 40",
                   fg="#2F3646", bg="white")
    header.place(x=13, y=10)


# ---------------- Side Bar----------------
# Creating a Frame
sideframe = Frame(app, width=300, height=1080, bg="#0E2023", bd=0)
sideframe.pack(side="left")
# # Inserting Gradient Image with Label
# sidebar = Label(sideframe, image=sidenav, bd=0)
# sidebar.pack()
# Admin Icon
adico = Label(app, image=adminicon, bd=0, bg="#0E2023")
adico.place(x=120, y=75)
# Hello Username
msg = Label(app, text="Hello, @username!", bg="#0E2023",
            font=("Poppins 16"), fg="white")
msg.place(x=100, y=200)

# ----Side Menu----

# DashBoard Button SELECTED
dashbtn = Button(app, image=dashbtnimg, borderwidth=0, bd=0,
                 bg="#0E2023", activebackground="#0E2023", command=dashFun)
dashbtn.place(x=0, y=250)

# Trial func


# Create Button
createbtn = Button(app, image=createIcon, text="Create Quiz", padx=20, font=(
    "Poppins 20"), compound="left", borderwidth=0, bd=0, bg="#0E2023", fg="white", activebackground="#0E2023", activeforeground="white", command=createQuizFun)
createbtn.place(x=0, y=310)
# recent Button
recentbtn = Button(app, image=recentIcon, text="Recent Quizes", padx=20, font=(
    "Poppins 20"), compound="left", borderwidth=0, bd=0, bg="#0E2023", fg="white", activebackground="#0E2023", activeforeground="white", command=recentQuizFun)
recentbtn.place(x=0, y=370)
# Result Button
resultbtn = Button(app, image=resultIcon, text="Results", padx=20, font=(
    "Poppins 20"), compound="left", borderwidth=0, bd=0, bg="#0E2023", fg="white", activebackground="#0E2023", activeforeground="white", command=resultsFun)
resultbtn.place(x=0, y=430)
# Leaderboard Button
leaderboardbtn = Button(app, image=leaderboardIcon, text="Leaderboard", padx=20, font=(
    "Poppins 20"), compound="left", borderwidth=0, bd=0, bg="#0E2023", fg="white", activebackground="#0E2023", activeforeground="white", command=leaderboardFun)
leaderboardbtn.place(x=0, y=490)

# Logout Button
logoutbtn = Button(app, image=logoutIcon, text="Logout", padx=10, font=(
    "Poppins 20"), compound="left", borderwidth=0, bd=0, bg="#0E2023", fg="white", activebackground="#0E2023", activeforeground="white")
logoutbtn.place(x=50, y=600)

# Calling the Dashboard Function by default
dashFun()
# ----Opening the Window-------
app.mainloop()
