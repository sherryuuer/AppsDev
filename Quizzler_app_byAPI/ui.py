from tkinter import *
from quiz_brain import QuizBrain


THEME_COLOR = "#375362"
CANVAS_COLOR = "#FBFFE3"

class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        # canvas画布
        self.canvas = Canvas(width=300, height=250, bg=CANVAS_COLOR, highlightthickness=0)
        self.question_text = self.canvas.create_text(150, 120, width=280, text="some question", font=("Arial", 20, "italic"), fill=THEME_COLOR)
        self.canvas.grid(row=1, column=0, columnspan=2)

        # Score Label
        self.score_label = Label(text="score: 0", justify="right", fg="white", font=("Arial", 12, "bold"), bg=THEME_COLOR)
        self.score_label.grid(column=1, row=0)
        self.score_label.config(padx=20, pady=10)

        # Buttons
        self.true_image = PhotoImage(file="Quizzler_app_byAPI/images/true.png")
        self.true_button = Button(image=self.true_image, highlightthickness=0, command=self.press_true_button)
        self.true_button.grid(row=2, column=0, pady=20)
        self.false_image = PhotoImage(file="Quizzler_app_byAPI/images/false.png")
        self.false_button = Button(image=self.false_image, highlightthickness=0, command=self.press_false_button)
        self.false_button.grid(row=2, column=1, pady=20)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You are at the end of the question list.")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def press_true_button(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)

    def press_false_button(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)



