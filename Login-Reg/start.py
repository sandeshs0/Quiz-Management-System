from tkinter import *

# Creating the starting window
window = Tk()
window.title("Quizsport")
window.geometry("800x800")
window.configure(bg="white")

# Defining Photoimages
logo = PhotoImage(
    file="C:\\sandesh\\Python\\tkinterrr\\FirstSem Project\\Login-Reg\\logo.png")
illus = PhotoImage(
    file="C:\\sandesh\\Python\\tkinterrr\\FirstSem Project\\Login-Reg\\illus.png")
alogo = PhotoImage(
    file="C:\\sandesh\\Python\\tkinterrr\\FirstSem Project\\Login-Reg\\alogo.png")
contillus = PhotoImage(
    file="C:\\sandesh\\Python\\tkinterrr\\FirstSem Project\\Login-Reg\\contillus.png")
anadmin = PhotoImage(
    file="C:\\sandesh\\Python\\tkinterrr\\FirstSem Project\\Login-Reg\\anadmin.png")
astudent = PhotoImage(
    file="C:\\sandesh\\Python\\tkinterrr\\FirstSem Project\\Login-Reg\\astudent.png")

# Placing the Header Area
head = Label(window, text="EzyQzy", bg="white",
             fg="#22A9BB", font=("Helvetica 45 bold"), image=logo, compound=LEFT)
# Placing the illustration and slogan
illuslab = Label(window, text='"Lorem ipsum dolor sit amet, consectetur adipiscing elit"',
                 fg="#020439", bg="white", font=("Poppins italic", 20), image=illus, compound=TOP)
head.pack()
illuslab.pack(padx=10)

# Continue as wala Screen


def continueAs():
    global contd
    contWin = Toplevel()
    contWin.title('EzyQzy')
    contWin.configure(bg="white")
    contWin.geometry("800x800")

    head2 = Label(contWin, text="EzyQzy", bg="white",
                  fg="#22A9BB", font=("Helvetica 30 bold"), image=alogo, compound=LEFT)
    head2.pack(side='top', anchor=NW)
    h1 = Label(contWin, text="Let's Get Trivial!",
               bg="white", fg="#15050B", font=("Roboto 35"), image=contillus, compound=BOTTOM)
    h1.pack(pady=20)
    opttext = Label(contWin, text="C O N T I N U E   A S", bg="white",
                    fg="#020439", font=("Verdana 18"))
    opttext.pack()

    # Parent Frame to contain both the buttons.
    pane = Frame(contWin)
    pane.pack(fill=BOTH, expand=True)

    # button widgets which can also expand and fill
    # in the parent widget entirely
    # Button 1
    asAdmin = Button(pane, image=anadmin, command=contWin.destroy,
                     borderwidth=0, bg="white", activebackground="white")
    asAdmin.pack(side=LEFT, expand=True, fill=BOTH)

    # Button 2
    asStudent = Button(pane, image=astudent, command=contWin.destroy,
                       borderwidth=0, bg="white", activebackground="white")
    asStudent.pack(side=LEFT, expand=True, fill=BOTH)


# GET Started button:
click_btn = PhotoImage(
    file="C:\\sandesh\\Python\\tkinterrr\\FirstSem Project\\Login-Reg\\GET STARTED.png")

# creating a dummy button and passing the image
button = Button(window, image=click_btn, command=continueAs,
                borderwidth=0, bg="white", activebackground="white")
button.pack(pady=50)

window.mainloop()
