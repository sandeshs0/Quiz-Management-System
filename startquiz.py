from tkinter import *
from tkinter import messagebox
import sqlite3
import sys
import subprocess

# Importing variables
all = sys.argv
stdusername = all[-1]
# print(stdusername)
# stdusername = "test"
quizTitle = "Function"

root = Tk()
root.geometry("800x500")
root.resizable(False, False)
root.title("Quiz")
root.config(bg="white")


def completed():
    conn = sqlite3.connect('scores.db')
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS scorechart(ID INTEGER PRIMARY KEY AUTOINCREMENT, Quiz_title TEXT, Candidate TEXT, Score INTEGER)")
    cur.execute("INSERT INTO scorechart(Quiz_title, Candidate, Score) VALUES(?,?,?)",
                (quizTitle, stdusername, score))
    conn.commit()
    conn.close()

    root.destroy()


# img
nextbut = PhotoImage(file=(
    r"C:\sandesh\Python\tkinterrr\FirstSem Project - Copy\Khichadi\nextbtn.png"))
quitbut = PhotoImage(file=(
    r"C:\sandesh\Python\tkinterrr\FirstSem Project - Copy\Khichadi\quitbtn.png"))
framebg = PhotoImage(file=(
    r"C:\sandesh\Python\tkinterrr\FirstSem Project - Copy\Khichadi\quizframe.png"))

conn = sqlite3.connect('quizes.db')
cur = conn.cursor()
# For Questions:
cur.execute(f"SELECT Questions FROM {quizTitle}")
q = cur.fetchall()

# For Options:
cur.execute(f"SELECT Option1, Option2, Option3, Option4 FROM {quizTitle}")
options = cur.fetchall()

# For Answer:
cur.execute(f"SELECT Answer FROM {quizTitle}")
a = cur.fetchall()

# Commiting and Closing the DB
conn.commit()
conn.close()

# Frame
container = Frame(root, bg="black", height=200, width=200)
container.place(x=70, y=90)

# --Placing the background rectangle
bglabel = Label(container, image=framebg, bg="white")
bglabel.pack()


class Quiz:
    def __init__(self):
        self.qn = 0
        self.opt_sel = IntVar()
        self.options = self.radiobtns()
        self.ques = self.question(self.qn)
        self.display_options(self.qn)
        self.buttons()
        self.correct = 0

    def question(self, qn):
        t = Label(root, text=f"{quizTitle}", width=50, bg="#22A5BB",
                  fg="white", font=("Poppins", 20, "bold"))
        t.place(x=0, y=2)
        qn = Label(container, text=q[qn], width=40, font=(
            "Poppins", 18, "bold"), bg="#F9ECEC", anchor="w")
        qn.place(x=10, y=10)
        return qn

    def radiobtns(self):
        val = 0
        b = []
        yp = 100
        while val < 4:
            btn = Radiobutton(container, text=" ", variable=self.opt_sel,
                              value=val+1, width=80, anchor=W, bg="#9BB1E2", fg="#310606", font=("Poppins", 16))
            b.append(btn)
            btn.place(x=50, y=yp)
            val += 1
            yp += 40
        return b

    def display_options(self, qn):
        val = 0
        self.opt_sel.set(0)
        self.ques['text'] = q[qn]
        for op in options[qn]:
            self.options[val]['text'] = op
            val += 1

    def buttons(self):
        nbutton = Button(container, image=nextbut, borderwidth=0, bd=0, bg="white",
                         command=self.next_btn)
        nbutton.place(x=300, y=280)
        quitbutton = Button(container, image=quitbut, borderwidth=0, bd=0,
                            bg="white", command=root.destroy)
        quitbutton.place(x=420, y=280)

    def checkans(self, qn):
        # print(self.opt_sel.get())

        x = str(a[qn])
        y = int(x[1:2])
        # print(y)
        # print(self.opt_sel.get() == y)
        if self.opt_sel.get() == y:
            return True

    def next_btn(self):
        if self.checkans(self.qn):
            self.correct += 1
        self.qn += 1
        if self.qn == len(q):
            self.display_result()
        else:
            self.display_options(self.qn)

    def display_result(self):
        global score
        score = int(self.correct/len(q)*100)
        result = "Score: "+str(score)+" %"
        wc = len(q)-self.correct
        correct = "Correct: " + str(self.correct)
        wrong = "Wrong: " + str(wc)
        alert = messagebox.showinfo("Result", "\n".join(
            ["Quiz Completed! Here is your result:", result, correct, wrong]))
        if alert:
            completed()


quiz = Quiz()
root.mainloop()
