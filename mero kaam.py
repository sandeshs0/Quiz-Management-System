from tkinter import *

# Creating the starting window:
window = Tk()
window.title("Quizzsport")
window.geometry("800x800")
window.configure(bg="white")

# Defining Photoimages
logo = PhotoImage(
    file="/Users/rabins_khanal/python/rtr.py/logo.png")
illus = PhotoImage(
    file="//Users//rabins_khanal//python//rtr.py//illus.png")
alogo = PhotoImage(
    file="//Users//rabins_khanal//python/rtr.py//alogo.png")
contillus = PhotoImage(
    file="//Users//rabins_khanal//python/rtr.py//contillus.png")
anadmin = PhotoImage(
    file="//Users//rabins_khanal//python/rtr.py//anadmin.png")
astudent = PhotoImage(
    file="//Users//rabins_khanal//python//rtr.py//astudent.png")
# GET Started button:
click_btn = PhotoImage(
    file="//Users//rabins_khanal//python//rtr.py//GET STARTED.png")
signup=PhotoImage(
    file="//Users//rabins_khanal//python//rtr.py//signup.png")



# Placing the Header Area
head = Label(window, text="EzyQzy", bg="white",
             fg="#22A9BB", font=("Helvetica 45 bold"), image=logo, compound=LEFT)
# Placing the illustration and slogan
illuslab = Label(window, text='"Lorem ipsum dolor sit amet, consectetur adipiscing elit"',
                 fg="#020439", bg="white", font=("Poppins italic", 20), image=illus, compound=TOP)
head.grid(column=0)
illuslab.grid(column=0,padx=150)


# Continue as wala Screen


def continueAs():
    global contd
    contWin = Toplevel()
    contWin.title('EzyQzy')
    contWin.configure(bg="white")
    contWin.geometry("800x800")

    head2 = Label(contWin, text="EzyQzy", bg="white",
                  fg="#22A9BB", font=("Helvetica 30 bold"), image=alogo, compound=LEFT)
    head2.grid(column=0,pady=0,padx=0)
    h1 = Label(contWin, text="Let's Get Trivial!",
               bg="white", fg="#15050B", font=("Roboto 35"), image=contillus, compound=BOTTOM)
    h1.grid(column=0,padx=245,pady=20)
    opttext = Label(contWin, text="C O N T I N U E   A S", bg="white",
                    fg="#020439", font=("Verdana 18"))
    opttext.grid(pady=20)

    
    # Parent Frame to contain both the buttons.
    pane = Frame(contWin)
    pane.grid()

    # button widgets which can also expand and fill
    # in the parent widget entirely
    # Button 1
    asAdmin = Button(pane, image=anadmin, command=contWin.destroy,
                      bg="white", activebackground="white")
    asAdmin.grid(pady=5)

    # Button 2
    asStudent = Button(pane, image=astudent, command=contWin.destroy
                , bg="white", activebackground="white")
    asStudent.grid(pady=5)

    
    
    # Button 3
getstartedbut =Button(window,fg="#020439", bg="white",image=click_btn,command=continueAs,compound=BOTTOM)
getstartedbut.grid(column=0,padx=100,pady=15)
    
signuptext =Label(window, text= "Are you new? Sign Up!",
    fg="#020439", bg="white", font=("Poppins italic", 20),compound=TOP)
signuptext.grid(column=0,padx=120,pady=20)


def admininfo():
  global contd
  import sqlite3
  from tkinter import messagebox

  admin_info = Toplevel()
  admin_info.title('Admin sign up')
  
  admin_info.configure(bg="white")
  admin_info.geometry("800x800")

  head3 = Label(admin_info, text="EzyQzy", bg="white",
                  fg="#22A9BB", font=("Helvetica 30 bold"), image=alogo, compound=LEFT)
  head3.grid()
  adminsignup=Label(admin_info,text="Fill the following informations:",bg="white",fg="#22A9BB",font=("Helvetica 30 bold"))
  adminsignup.grid(row=2,pady=5)

  
  
  

# Connecting Database
  dat=sqlite3.connect('client_info.db')

# Cursor
  cur=dat.cursor()

# creating table
  def submit():
    dat=sqlite3.connect('client_info.db')
    cur=dat.cursor()
    cur.execute("INSERT INTO info VALUES(:f_name,:l_name,:email,:age,:passsword)",{
        'f_name':fnameEnt.get(),
        'l_name':lnameEnt.get(),
        'email':emailEnt.get(),
        'age' :ageEnt.get(), 
        'passsword':pwdEnt.get()   
        })
    messagebox.showinfo("address","inserted successfully")
    dat.commit()
    dat.close()


    # cur.execute('''CREATE TABLE info(
    #     fname text,
    #     lname text,
    #     email text,
    #     age integer,
    #     password text
    #     )''')
    # print("Table done")
    # dat.commit()
    # dat.close()
    

  fnameLab=Label(admin_info,text="First Name     :")
  fnameLab.grid(row=4,padx=0,column=0,pady=20)
  lnameLab=Label(admin_info,text="Last name      :")
  lnameLab.grid(row=5,column=0,padx=0,pady=20)
  emailLab=Label(admin_info,text="Email        :")
  emailLab.grid(row=6,padx=0,pady=20)
  ageLab=Label(admin_info,text="Age     :")
  ageLab.grid(row=7,padx=0,pady=20)
  pwdLab=Label(admin_info,text="Password     :")
  pwdLab.grid(row=8,padx=0,pady=20)


  
  fnameEnt=Entry(admin_info,width=20)
  fnameEnt.grid(row=4,column=1,pady=10)
  lnameEnt=Entry(admin_info,width=20)
  lnameEnt.grid(row=5,column=1,pady=10)
  emailEnt=Entry(admin_info,width=20)
  emailEnt.grid(row=6,column=1,pady=10)
  ageEnt=Entry(admin_info,width=20)
  ageEnt.grid(row=7,column=1,pady=10)
  pwdEnt=Entry(admin_info,width=20)
  pwdEnt.grid(row=8,column=1,pady=10)

  submitbutton=Button(admin_info,text="Submit", command=submit)
  submitbutton.grid(row=12,column=0,padx=0,pady=10)

def studentinfo():
  global contd
  import sqlite3
  from tkinter import messagebox

  student_info = Toplevel()
  student_info.title('student sign up')
  
  student_info.configure(bg="white")
  student_info.geometry("800x800")

  head3 = Label(student_info, text="EzyQzy", bg="white",
                  fg="#22A9BB", font=("Helvetica 30 bold"), image=alogo, compound=LEFT)
  head3.grid()
  studentsignup=Label(student_info,text="Fill the following informations:",bg="white",fg="#22A9BB",font=("Helvetica 30 bold"))
  studentsignup.grid(row=2,pady=5)

  
  
  

# Connecting Database
  dat=sqlite3.connect('student_info.db')

# Cursor
  cur=dat.cursor()

# creating table
  def submit():
    dat=sqlite3.connect('student_info.db')
    cur=dat.cursor()
    cur.execute("INSERT INTO info2 VALUES(:f_name,:l_name,:email,:age,:passsword)",{
        'f_name':fnameEnt.get(),
        'l_name':lnameEnt.get(),
        'email':emailEnt.get(),
        'age' :ageEnt.get(), 
        'passsword':pwdEnt.get()   
        })
    messagebox.showinfo("address","inserted successfully")
    dat.commit()
    dat.close()


  # cur.execute('''CREATE TABLE info2(
  #       fname text,
  #       lname text,
  #       email text,
  #       age integer,
  #       password text
  #       )''')
  # print("Table done")
  # dat.commit()
  # dat.close()
    


# Input labels
  fnameLab=Label(student_info,text="First Name    :")
  fnameLab.grid(row=4,padx=0,column=0,pady=20)
  lnameLab=Label(student_info,text="Last name     :")
  lnameLab.grid(row=5,padx=0,column=0,pady=20)
  emailLab=Label(student_info,text="Email       :")
  emailLab.grid(row=6,padx=0,column=0,pady=20)
  ageLab=Label(student_info,text="Age          :")
  ageLab.grid(row=7,padx=0,column=0,pady=20)
  pwdLab=Label(student_info,text="Password      :")
  pwdLab.grid(row=8,padx=0,column=0,pady=20)


  
  fnameEnt=Entry(student_info,width=20)
  fnameEnt.grid(row=4,column=1,pady=10)
  lnameEnt=Entry(student_info,width=20)
  lnameEnt.grid(row=5,column=1,pady=10)
  emailEnt=Entry(student_info,width=20)
  emailEnt.grid(row=6,column=1,pady=10)
  ageEnt=Entry(student_info,width=20)
  ageEnt.grid(row=7,column=1,pady=10)
  pwdEnt=Entry(student_info,width=20)
  pwdEnt.grid(row=8,column=1,pady=10)


  submitbutton=Button(student_info,text="Submit", command=submit)
  submitbutton.grid(row=12,column=0,pady=10)


def sign_up():

  global contd
  adminorstudent = Toplevel()
  adminorstudent.title('SIGN UP Choice')
  adminorstudent.configure(bg="white")
  adminorstudent.geometry("800x800")

  head2 = Label(adminorstudent, text="EzyQzy", bg="white",
                  fg="#22A9BB", font=("Helvetica 30 bold"), image=alogo, compound=LEFT)
  head2.grid()

  signup=Label(adminorstudent,text="Are you ?",bg="white",fg="#22A9BB",font=("Helvetica 30 bold"))
  signup.grid(column=0,padx=0,pady=20)
  
  signupbuttonchoice=Button(adminorstudent,image=anadmin,command=admininfo,borderwidth=6,bg="white")
  signupbuttonchoice.grid(column=1,pady=40,padx=30)

  signupbuttonchoice1=Button(adminorstudent,image=astudent,command=studentinfo,borderwidth=6,bg="white")
  signupbuttonchoice1.grid(column=1,pady=40,padx=30)


  
  
# Button 4

signupbuttonchoice=Button(window,image=signup,command=sign_up,bg="yellow",compound=BOTTOM)
signupbuttonchoice.grid(padx=100)

  

  
window.mainloop()
