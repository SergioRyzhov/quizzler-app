from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(pady=20, padx=20, bg=THEME_COLOR)

        self.label = Label(
            text="Score: 0",
            bg=THEME_COLOR,
            font=("Arial", 14,),
            fg="white",
        )
        self.label.grid(row=0, column=1, pady=20, padx=20)

        self.canvas = Canvas(width=300, height=250, highlightthickness=0, bg="white")
        self.canvas_text_id = self.canvas.create_text(
            150,
            125,
            text="Text",
            fill=THEME_COLOR,
            font=("Arial", 20, "italic"),
            width=280,
        )
        self.canvas.grid(row=1, column=0, columnspan=2)

        self.button_true_img = PhotoImage(file="images/true.png")
        self.button_false_img = PhotoImage(file="images/false.png")

        self.button_true = Button(
            image=self.button_true_img,
            highlightthickness=0,
            bg=THEME_COLOR,
            borderwidth=0,
            command=self.right_answer,
        )
        self.button_true.grid(row=2, column=0, padx=20, pady=20)
        self.button_false = Button(
            image=self.button_false_img,
            highlightthickness=0,
            bg=THEME_COLOR,
            borderwidth=0,
            command=self.wrong_answer
        )
        self.button_false.grid(row=2, column=1, padx=20, pady=20)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.label.config(text=f"Score: {self.quiz.score}")
            self.canvas.itemconfig(self.canvas_text_id, text=q_text)
        else:
            self.canvas.itemconfig(self.canvas_text_id, text="You've reached the end of the quiz")
            self.button_true.config(state="disabled")
            self.button_false.config(state="disabled")

    def right_answer(self):
        self.feedback_to_user(self.quiz.check_answer("true"))

    def wrong_answer(self):
        self.feedback_to_user(self.quiz.check_answer("false"))

    def feedback_to_user(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)
