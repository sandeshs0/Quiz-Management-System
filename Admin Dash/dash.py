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
# Logo
logo = PhotoImage(
    file="C:\\sandesh\\Python\\tkinterrr\\FirstSem Project\\Admin Dash\\Images\\logo.png")
# Create Icon
createIcon = PhotoImage(
    file="C:\\sandesh\\Python\\tkinterrr\\FirstSem Project\\Admin Dash\\Images\\create_icon.png")
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
# DP
userdp = Image.open(
    "C:\\sandesh\\Python\\tkinterrr\\FirstSem Project\\Admin Dash\\Images\\userdp.png")
resizedp = userdp.resize((55, 55))
finaldp = ImageTk.PhotoImage(resizedp)
userprofile = Label(app, image=finaldp, text="Aladeen",
                    compound="left", font="Poppins 20", bg="#22A5BB", fg="white", padx=10)
userprofile.place(x=1170, y=4)

# -----------------------------------------------------

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
                 bg="#0E2023", activebackground="#0E2023")
dashbtn.place(x=0, y=250)

# Create Button
createbtn = Button(app, image=createIcon, text="Create Quiz", padx=20, font=(
    "Poppins 20"), compound="left", borderwidth=0, bd=0, bg="#0E2023", fg="white", activebackground="#0E2023", activeforeground="white")
createbtn.place(x=0, y=310)
# recent Button
recentbtn = Button(app, image=recentIcon, text="Recent Quizes", padx=20, font=(
    "Poppins 20"), compound="left", borderwidth=0, bd=0, bg="#0E2023", fg="white", activebackground="#0E2023", activeforeground="white")
recentbtn.place(x=0, y=360)
# Result Button
resultbtn = Button(app, image=resultIcon, text="Results", padx=20, font=(
    "Poppins 20"), compound="left", borderwidth=0, bd=0, bg="#0E2023", fg="white", activebackground="#0E2023", activeforeground="white")
resultbtn.place(x=0, y=410)
# Leaderboard Button
leaderboardbtn = Button(app, image=leaderboardIcon, text="Leaderboard", padx=20, font=(
    "Poppins 20"), compound="left", borderwidth=0, bd=0, bg="#0E2023", fg="white", activebackground="#0E2023", activeforeground="white")
leaderboardbtn.place(x=0, y=460)

# Logout Button
logoutbtn = Button(app, image=logoutIcon, text="Logout", padx=10, font=(
    "Poppins 20"), compound="left", borderwidth=0, bd=0, bg="#0E2023", fg="white", activebackground="#0E2023", activeforeground="white")
logoutbtn.place(x=50, y=600)

# ----------------C A R D S -----------------
header = Label(app, text="Dashboard", font="Poppins 40",
               fg="#2F3646", bg="white")
header.place(x=313, y=80)


# ---1--Quiz Card-----
quizCard = Frame(app, width=300, height=200, bg="#4A7A33", bd=0)
quizCard.place(x=350, y=150)
# Shadow Image
quizCardImg = Label(app, image=QuizCardPic, bg="#4A7A33")
quizCardImg.place(x=500, y=180)
# Number
quiznum = Label(app, text="5", font=("Poppins 110"), bg="#4A7A33", fg="white")
quiznum.place(x=360, y=150)
# Text
categ = Label(app, text="Quizes", font=(
    "Poppins 20"), bg="#4A7A33", fg="white")
categ.place(x=360, y=310)
# View All Button
viewAllQ = Button(app, image=viewAllGreen, borderwidth=0,
                  bd=0, bg="#4A7A33", activebackground="#4A7A33")
viewAllQ.place(x=350, y=350)

# --2---Participants Card-----
quizCard = Frame(app, width=300, height=200, bg="#C2A50C", bd=0)
quizCard.place(x=670, y=150)
# Shadow Image
quizCardImg = Label(app, image=participantCardPic, bg="#C2A50C")
quizCardImg.place(x=820, y=180)
# Number
quiznum = Label(app, text="17", font=("Poppins 90"), bg="#C2A50C", fg="white")
quiznum.place(x=680, y=180)
# Text
categ = Label(app, text="Participants", font=(
    "Poppins 20"), bg="#C2A50C", fg="white")
categ.place(x=680, y=310)
# View All Button
viewAllQ = Button(app, image=viewAllYellow, borderwidth=0,
                  bd=0, bg="#C2A50C", activebackground="#C2A50C")
viewAllQ.place(x=670, y=350)

# --3---Results Card-----
quizCard = Frame(app, width=300, height=200, bg="#D2403C", bd=0)
quizCard.place(x=990, y=150)
# Shadow Image
quizCardImg = Label(app, image=resultCardPic, bg="#D2403C")
quizCardImg.place(x=1140, y=180)
# Number
quiznum = Label(app, text="3", font=("Poppins 110"), bg="#D2403C", fg="white")
quiznum.place(x=1000, y=150)
# Text
categ = Label(app, text="Results", font=(
    "Poppins 20"), bg="#D2403C", fg="white")
categ.place(x=1000, y=310)
# View All Button
viewAllQ = Button(app, image=viewAllRed, borderwidth=0,
                  bd=0, bg="#D2403C", activebackground="#D2403C")
viewAllQ.place(x=990, y=350)


# ----Opening the Window-------
app.mainloop()
