from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain) -> None:
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        self.score_label = Label(text="score: 0", bg=THEME_COLOR)
        self.score_label.grid(row=0, column=0)

        self.canvas = Canvas(width=300, height=250)
        self.question_text = self.canvas.create_text(
            158,
            125,
            width=200,  #  separete lines
            text="?",
            font=("Arial", 20, "bold"),
            fill=THEME_COLOR,
        )
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        true_image = PhotoImage(file="images/true.png")
        self.true_button = Button(
            image=true_image, highlightthickness=0, command=self.correct
        )
        self.true_button.grid(row=2, column=0)

        false_image = PhotoImage(file="images/false.png")
        self.false_button = Button(
            image=false_image, highlightthickness=0, command=self.incorrect
        )
        self.false_button.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        if self.quiz.still_has_questions():
            self.canvas.config(bg="white")
            self.score_label.config(text=f"score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(
                self.question_text, text="mmm nop"
            )  #  when over 10 questions
            self.true_button.config(state="disabled")  #  disable 2 buttons
            self.false_button.config(state="disabled")

    def correct(self):
        self.give_feedback(self.quiz.check_answer("True"))
        print("yes")

    def incorrect(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)
