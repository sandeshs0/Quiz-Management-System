from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk
import runpy
from tkinter import messagebox
import sqlite3


con= sqlite3.connect(database=r'crud.db')
cur= con.cursor()
def connection():
    cur.execute("CREATE TABLE IF NOT EXIST CreateQuiz(subject_id INTEGER PRIMARY KEY  AUTOINCREMENT, Subject Name VARCHAR(100), Questions Text TEXT, Option1 TEXT, Option2 TEXT, Option3 TEXT, Option4  TEXT, Answer TEXT")
    con.commit()
    

def gotoAddQns():
    connection
    app.destroy()
    runpy.run_path(r"C:\Users\pooja\Desktop\QuizProject\Codes\questions.py")
    # cur.execute("""INSERT INTO CreateQuiz (subjectname,questiontext, option1, option2, option3, option4, answer)
    #                   VALUES (?,?,?,?,?,?,?)""", (subjectname,questiontext, option1, option2, option3, option4, answer))
    # con.commit()
    # app.destroy()
    # runpy.run_path(r"C:\Users\pooja\Desktop\QuizProject\Codes\questions.py")

 

def get_questions():
    cur.execute("SELECT * FROM CreateQuiz")
    return cur.fetchall()

def show():
    connection
    try:
        cur.execute("select * from CreateQuiz")
        rows=cur.fetchall()
        quiz_tree.delete(quiz_tree.get_children())
        for row in rows:
            quiz_tree.insert('',END,values=row)
    except Exception as ex:
        messagebox.showerror("Error", f"Error due to :{str(ex)}", parent =app)

###Create window
app = Tk()
app.geometry("1480x1080")
app.title("Admin Dashboard ~ EzyQzy")
app.config(bg="white")
app.resizable(False,False)
create_quiz_frame=ImageTk.PhotoImage(file=r"C:\Users\pooja\Desktop\QuizProject\Codes\Images\Untitled.png")
create_quiz=Label(app, image=create_quiz_frame,)
create_quiz.pack(fill='both', expand='yes')

quiz_text=Label(app,text="Create Quiz",font=("poppins 20",15, "bold"),bg="white",fg="black")
quiz_text.place(x=420, y=70, width=640)

one_frame= Frame(app,bg="white")
one_frame.place(x=100, y=115, height=572, width=315)




##next  frame

tree_frame= Frame(app,bg="white")
tree_frame.place(x=480, y=115, height=572, width=880)

####label frame 
two_frame= LabelFrame(one_frame, text="Online quiz", font=("poppins 20",12, "bold"),bg="white",height=465 ,  width=303, borderwidth=2.4)
two_frame.config(highlightbackground="red")
two_frame.place(x=5, y=45)

##Add questions button 
add_que= ImageTk.PhotoImage(file=r"C:\Users\pooja\Desktop\QuizProject\Codes\Images\addimg.png")
add_que_btn= Button(two_frame, image=add_que,borderwidth=0,activebackground="white", bg="white",command=gotoAddQns)
add_que_btn.place(x=8, y=40)

##3update questions
upd_que= ImageTk.PhotoImage(file=r"C:\Users\pooja\Desktop\QuizProject\Codes\Images\button_upd.png")
upd_que_btn= Button(two_frame, image=upd_que,borderwidth=0,activebackground="white", bg="white")
upd_que_btn.place(x=8, y=90)

###del questions button
# del_que= ImageTk.PhotoImage(file=r"C:\Users\pooja\Desktop\QuizProject\Codes\Images\buttondel.png")
# del_que_btn= Button(two_frame, image=del_que,borderwidth=0,activebackground="white", bg="white")
# upd_que_btn.place(x=8, y=120)

#3 dashboard button
dash_que= ImageTk.PhotoImage(file=r"C:\Users\pooja\Desktop\QuizProject\Codes\Images\dashboard.png")
dash_que_btn= Button(two_frame, image=dash_que,borderwidth=0,activebackground="white", bg="white")
 
dash_que_btn.place(x=8, y=160)

####tree view

style = ttk.Style()
style.configure("Treeview.Heading", font=("poppins 20",10, "bold"), foreground="black")

scroll_x = Scrollbar(tree_frame, orient=HORIZONTAL)
scroll_y = Scrollbar(tree_frame ,orient=VERTICAL)
quiz_tree = ttk.Treeview(tree_frame, columns=("Subject ID", "Subject NAME", "Questions Text", "Created at", "Status","Option1","Option2","Option3","Option4", "Answer"),
         xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

scroll_x.pack(side=BOTTOM, fill=X)
scroll_y.pack(side=RIGHT, fill=Y)
scroll_x.config(command=quiz_tree.xview)
scroll_y.config(command=quiz_tree.yview)

quiz_tree.heading("Subject ID", text="ID")
quiz_tree.heading("Subject NAME",text="Subject NAME")
quiz_tree.heading("Questions Text", text="Questions Text")
quiz_tree.heading("Created at", text="Created at")
quiz_tree.heading("Status", text="Status")
quiz_tree.heading("Option1", text="Option1")
quiz_tree.heading("Option2", text="Option2")
quiz_tree.heading("Option3", text="Option3")
quiz_tree.heading("Option4", text="Option4")
quiz_tree.heading("Answer", text="Answer")





quiz_tree["show"] = "headings"

quiz_tree.column("Subject ID",width=50)
quiz_tree.column("Subject NAME",width=150)
quiz_tree.column("Questions Text",width=100)
quiz_tree.column("Created at", width=100)
quiz_tree.column("Status",width=100)
quiz_tree.column("Option1",width=100)
quiz_tree.column("Option2",width=100)
quiz_tree.column("Option3",width=100)
quiz_tree.column("Option4",width=100)
quiz_tree.column("Answer",width=100)
quiz_tree.pack(fill=BOTH, expand=1)
show()




 



###images 
app.mainloop()

