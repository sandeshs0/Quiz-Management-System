# import tkinter as tk

# def add_question():
#     question = question_text.get("1.0", tk.END).strip()
#     option1 = option1_entry.get().strip()
#     option2 = option2_entry.get().strip()
#     option3 = option3_entry.get().strip()
#     option4 = option4_entry.get().strip()
#     answer = answer_entry.get().strip()
    
#     # if not question or not option1 or not option2 or not option3 or not option4 or not answer:
#     #     message_label.config(text="Please enter all fields")
#     #     return
    
#     # # Call the function that handles adding the question to the database here
#     # message_label.config(text="Question added successfully")
    
# root = tk.Tk()
# root.title("Add Question")

# question_label = tk.Label(root, text="Question:")
# question_label.grid(row=0, column=0, padx=10, pady=10)

# question_text = tk.Text(root, height=5, width=30)
# question_text.grid(row=0, column=1, padx=10, pady=10)

# option1_label = tk.Label(root, text="Option 1:")
# option1_label.grid(row=1, column=0, padx=10, pady=10)

# option1_entry = tk.Entry(root)
# option1_entry.grid(row=1, column=1, padx=10, pady=10)

# option2_label = tk.Label(root, text="Option 2:")
# option2_label.grid(row=2, column=0, padx=10, pady=10)

# option2_entry = tk.Entry(root)
# option2_entry.grid(row=2, column=1, padx=10, pady=10)

# option3_label = tk.Label(root, text="Option 3:")
# option3_label.grid(row=3, column=0, padx=10, pady=10)

# option3_entry = tk.Entry(root)
# option3_entry.grid(row=3, column=1, padx=10, pady=10)

# option4_label = tk.Label(root, text="Option 4:")
# option4_label.grid(row=4, column=0, padx=10, pady=10)

# option4_entry = tk.Entry(root)
# option4_entry.grid(row=4, column=1, padx=10, pady=10)

# answer_label = tk.Label(root, text="Answer:")
# answer_label.grid(row=5, column=0, padx=10, pady=10)

# answer_entry = tk.Entry(root)
# answer_entry.grid(row=5, column=1, padx=10, pady=10)

# add_button = tk.Button(root, text="Add Question", command=add_question)
# add_button.grid(row=6, column=1, padx=10, pady=10)


# root.mainloop()


import sqlite3
import tkinter as tk

# Connect to the database
conn = sqlite3.connect("quiz.db")
cursor = conn.cursor()

# Create the questions table
cursor.execute("""CREATE TABLE IF NOT EXISTS questions (
                    id INTEGER PRIMARY KEY,
                    question TEXT,
                    option1 TEXT,
                    option2 TEXT,
                    option3 TEXT,
                    option4 TEXT,
                    answer INTEGER
                )""")
conn.commit()

# Function to add a question to the database
def add_question(question, option1, option2, option3, option4, answer):
    cursor.execute("""INSERT INTO questions (question, option1, option2, option3, option4, answer)
                      VALUES (?,?,?,?,?,?)""", (question, option1, option2, option3, option4, answer))
    conn.commit()

# Function to retrieve a question from the database
def get_question(id):
    cursor.execute("SELECT * FROM questions WHERE id=?", (id,))
    return cursor.fetchone()

# Function to retrieve all questions from the database
def get_questions():
    cursor.execute("SELECT * FROM questions")
    return cursor.fetchall()

# Tkinter GUI for adding questions
class AddQuestionGUI:
    def __init__(self, root):
        self.root = root
        self.question_entry = tk.Entry(root)
        self.option1_entry = tk.Entry(root)
        self.option2_entry = tk.Entry(root)
        self.option3_entry = tk.Entry(root)
        self.option4_entry = tk.Entry(root)
        self.answer_entry = tk.Entry(root)
        self.add_button = tk.Button(root, text="Add", command=self.add_question)

        self.question_entry.pack()
        self.option1_entry.pack()
        self.option2_entry.pack()
        self.option3_entry.pack()
        self.option4_entry.pack()
        self.answer_entry.pack()
        self.add_button.pack()

    def add_question(self):
        question = self.question_entry.get()
        option1 = self.option1_entry.get()
        option2 = self.option2_entry.get()
        option3 = self.option3_entry.get()
        option4 = self.option4_entry.get()
        answer = self.answer_entry.get()
        add_question(question, option1, option2, option3, option4, answer)
        self.root.destroy()

# Tkinter GUI for taking the quiz
class QuizGUI:
    def __init__(self, root):
        self.root = root
        self.question_label = tk.Label(root)
        self.option1_button = tk.Button(root, text="Option 1", command=lambda: self.choose_answer(1))

 
