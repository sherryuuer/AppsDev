from question_model import Question
from quiz_brain import QuizBrain
from data import question_data

question_bank = []

for q in question_data:
    question = Question(q["text"], q["answer"])
    # print(question.text, question.answer)
    question_bank.append(question)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print("You've complete the quiz.")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")
