from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk
import runpy
import sqlite3
 
con= sqlite3.connect(database=r'crud.db')
cur= con.cursor()
def connection():
    cur.execute("CREATE TABLE IF NOT EXIST CreateQuiz(subject_id INTEGER PRIMARY KEY  AUTOINCREMENT, subjectname VARCHAR(100), questionstext TEXT, option1 TEXT, option2 TEXT, option3 TEXT, option4  TEXT, answer INTEGER")
   
    con.commit()
     
 
 
#### to submit data
def submit_data():
    connection
    try:
        if sub_nam_entry.get()=="" or que_name_entry.get()=="" or option1_entry.get()=="" :
         messagebox.showwarning("Warning", "All Fields are Required\n Please fill all required fields")
        else:
            cur.execute("select * from CreateQuiz where subjectname=?",(sub_nam_entry.get(),))
            row=cur.fetchone()
            if row!=None:
                messagebox.showerror("Error", "subject name already exists", "try different", parent= app )
            else:
                cur.execute("Insert into CreateQuiz(subjectname,questionstext,option1, option2,option3,option4,answer) values (?,?,?,?,?,?,?)",
                (sub_nam_entry.get(),que_name_entry.get(),option1_entry.get(),option2_entry.get(),option3_entry.get(),option4_entry.get(),answer_entry.get()))
                con.commit()
                messagebox.showinfo("Sucess","Questions added  successfully", parent=app)
    except Exception as ex:
        messagebox.showerror("Error", f"Error due to :{str(ex)}", parent =app)

# def get_questions():
#     cur.execute("SELECT * FROM CreateQuiz WHERE subjectname=?", (sub_nam_entry.get(),))
#     return cur.fetchone()

def get_questions():
    cur.execute("SELECT * FROM CreateQuiz")
    return cur.fetchall()

# def get_questions():
#     cur.execute("SELECT * FROM questions WHERE id=?", (id,))
#     return cur.fetchone()
# def get_questions():
#     cur.execute("SELECT * FROM questions")
#     return cur.fetchall()
def show():
    connection
     
                
     


     
#333 to clear text 

def clear_text():
  sub_nam_entry.delete("0", END) 
  que_name_entry.delete("0", END)
  option1_entry.delete("0", END)
  option2_entry.delete("0", END)
  option3_entry.delete("0", END)
  option4_entry.delete("0", END)
  answer_entry.delete("0", END)
  show()
  


  

     

#### exit from window
def click_exit():
    app.destroy()
##### back to dashboard
def backto_createquiz():
    app.destroy()
    runpy.run_path(r"C:\Users\pooja\Desktop\QuizProject\Codes\createquiz.py")
### class crud class 
 
app = Tk()
app.geometry("1480x1080")
app.title("Admin Dashboard ~ EzyQzy")
app.config(bg="white")
app.resizable(False,False)
create_quiz_frame=ImageTk.PhotoImage(file=r"C:\Users\pooja\Desktop\QuizProject\Codes\Images\Untitled.png")
create_quiz=Label(app, image=create_quiz_frame,)
create_quiz.pack(fill='both', expand='yes')

quiz_text=Label(app,text="Add Questions",font=("poppins 20",15, "bold"),bg="white",fg="Blue")
quiz_text.place(x=420, y=150, width=640)


quiz_frame= LabelFrame(create_quiz, text="Questions",bg="white", font=("Poppins 20",15,"bold"), fg="#4f4e4d", height=380, width=800, borderwidth=2.4,)
quiz_frame.place(x=550, y=250, height=600)

#333   subject name 
subject_name= StringVar()

sub_nam= Label(quiz_frame, text= "Subject Name",bg="white", fg="#4f4e4d",font=("Poppins 20", 13,"bold"))
sub_nam.place(x=100, y=65)

sub_nam_entry = Entry(quiz_frame,highlightthickness=0, relief=FLAT, bg="grey", fg="black",font=("Poppins 20", 13,"bold"), textvariable=subject_name)
sub_nam_entry.place(x=250, y=65, width=400)

##3questions text 
que_name= Label(quiz_frame,text= "Questions Text",bg="white", fg="#4f4e4d",font=("Poppins 20", 13,"bold"))
que_name.place(x=100, y=120)


que_name_entry= Entry(quiz_frame,highlightthickness=0, relief=FLAT, bg="grey", fg="black",font=("Poppins 20", 13,"bold"))
que_name_entry.place(x=250, y=120, width=400, height=50)
## option1 
Option1= Label(quiz_frame,text= "Option1",bg="white", fg="#4f4e4d",font=("Poppins 20", 13,"bold"))
Option1.place(x=100, y=170)

option1_entry=  Entry(quiz_frame,highlightthickness=0, relief=FLAT, bg="grey", fg="black",font=("Poppins 20", 13,"bold"))
option1_entry.place(x=250, y=172, width=400)

Option2= Label(quiz_frame,text= "Option2",bg="white", fg="#4f4e4d",font=("Poppins 20", 13,"bold"))
Option2.place(x=100, y=220)

option2_entry=  Entry(quiz_frame,highlightthickness=0, relief=FLAT, bg="grey", fg="black",font=("Poppins 20", 13,"bold"))
option2_entry.place(x=250, y=220, width=400)

Option3= Label(quiz_frame,text= "Option3",bg="white", fg="#4f4e4d",font=("Poppins 20", 13,"bold"))
Option3.place(x=100, y=270)

option3_entry=  Entry(quiz_frame,highlightthickness=0, relief=FLAT, bg="grey", fg="black",font=("Poppins 20", 13,"bold"))
option3_entry.place(x=250, y=270, width=400)

Option4= Label(quiz_frame,text= "Option4",bg="white", fg="#4f4e4d",font=("Poppins 20", 13,"bold"))
Option4.place(x=100, y=320)

option4_entry=  Entry(quiz_frame,highlightthickness=0, relief=FLAT, bg="grey", fg="black",font=("Poppins 20", 13,"bold"))
option4_entry.place(x=250, y=320, width=400)

Answer= Label(quiz_frame,text= "Answer",bg="white", fg="#4f4e4d",font=("Poppins 20", 13,"bold"))
Answer.place(x=100, y=370)

answer_entry=  Entry(quiz_frame,highlightthickness=0, relief=FLAT, bg="grey", fg="black",font=("Poppins 20", 13,"bold"))
answer_entry.place(x=250, y=370, width=400)

app.option_add("*TCombobox*Listbox*Foreground", 'blue')
###Create at label
created_at=  Label(quiz_frame,text= "Created at",bg="white", fg="#4f4e4d",font=("Poppins 20", 13,"bold"))
created_at.place(x=100, y=420)

created_at_combo= ttk.Combobox(quiz_frame, state='readonly',width=35,font=("Poppins 20", 13,"bold"))
created_at_combo['values']= ("Sunday", "Monday", "Tuesday","wednesday", "Thursday", "Friday", "Saturday")

created_at_combo.current(0)
created_at_combo.place(x=250, y=420,width=400)

## status
app.option_add("*TCombobox*Listbox*Foreground", 'blue')
status_lab= Label(quiz_frame,text= "Status",bg="white", fg="#4f4e4d",font=("Poppins 20", 13,"bold"))
status_lab.place(x=100, y=470)

status_combo= ttk.Combobox(quiz_frame, state='readonly',width=35,font=("Poppins 20", 13,"bold"))
status_combo['values']= ("Published", "Unpublished")
status_combo.current(0)
status_combo.place(x=250, y=470,width=400)

###frame 
# two_frame= LabelFrame(app,  font=("poppins 20",12, "bold"),bg="white",height=465 ,  width=303, borderwidth=2.4)
# two_frame.config(highlightbackground="red")
# two_frame.place(x=180, y=280, width=350)

two_frame_ima= ImageTk.PhotoImage(file=r"C:\Users\pooja\Desktop\QuizProject\Codes\Images\—Pngtree—quiz sign icon questions_6234109.png")

two_frame_lab= Label(app,image=two_frame_ima)
two_frame_lab.place(x=160, y=400)

sub_ima= ImageTk.PhotoImage(file=r"C:\Users\pooja\Desktop\QuizProject\Codes\Images\submitpng.png")
sub_btn= Button(app, image=sub_ima, borderwidth=0,activebackground="white", bg="white", command=submit_data)
sub_btn.place(x=550, y=900)

clear_ima= ImageTk.PhotoImage(file=r"C:\Users\pooja\Desktop\QuizProject\Codes\Images\clear.png")
clear_btn=  Button(app, image=clear_ima, borderwidth=0,activebackground="white", bg="white",command=clear_text)
clear_btn.place(x=700, y=900)

exit_ima= ImageTk.PhotoImage(file=r"C:\Users\pooja\Desktop\QuizProject\Codes\Images\exit.png")
exit_btn= Button(app, image=exit_ima, borderwidth=0,activebackground="white", bg="white",command=click_exit)
exit_btn.place(x=850, y=900)

back_ima=  ImageTk.PhotoImage(file=r"C:\Users\pooja\Desktop\QuizProject\Codes\Images\back.png")
back_btn=   Button(app, image=back_ima, borderwidth=0,activebackground="white", bg="white", command=backto_createquiz)
back_btn.place(x=1000, y=900)
 

 



 
           
           


app.mainloop()




