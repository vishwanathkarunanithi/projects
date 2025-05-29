import tkinter as tk
from tkinter import messagebox

questions = [
    {
        "question": "What is the capital of France?",
        "options": ["Berlin", "London", "Paris", "Madrid"],
        "answer": 2
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["Earth", "Mars", "Jupiter", "Saturn"],
        "answer": 1
    },
    {
        "question": "Who wrote 'Hamlet'?",
        "options": ["Charles Dickens", "William Shakespeare", "Mark Twain", "Jane Austen"],
        "answer": 1
    }
]

class QuizApp:
    def __init__(self, root, questions):
        self.root = root
        self.questions = questions
        self.qn = 0
        self.score = 0
        self.var = tk.IntVar()
        self.create_widgets()
        self.show_question()

    def create_widgets(self):
        self.label = tk.Label(self.root, text="", font=("Arial", 16), wraplength=400)
        self.label.pack(pady=20)
        self.opts = []
        for i in range(4):
            rb = tk.Radiobutton(self.root, text="", variable=self.var, value=i, font=("Arial", 14))
            rb.pack(anchor="w")
            self.opts.append(rb)
        self.btn = tk.Button(self.root, text="Next", command=self.next_q)
        self.btn.pack(pady=20)

    def show_question(self):
        q = self.questions[self.qn]
        self.label.config(text=q["question"])
        self.var.set(-1)
        for i, option in enumerate(q["options"]):
            self.opts[i].config(text=option)

    def next_q(self):
        if self.var.get() == -1:
            messagebox.showwarning("Select an option", "Please select an answer.")
            return
        if self.var.get() == self.questions[self.qn]["answer"]:
            self.score += 1
        self.qn += 1
        if self.qn < len(self.questions):
            self.show_question()
        else:
            messagebox.showinfo("Quiz Finished", f"Your score: {self.score}/{len(self.questions)}")
            self.root.destroy()

root = tk.Tk()
root.title("Quiz App")
app = QuizApp(root, questions)
root.mainloop()
