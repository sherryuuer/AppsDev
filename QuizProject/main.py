from question_model import Question
from data import question_data

question_bank = []

for q in question_data:
    question = Question(q["text"], q["answer"])
    print(question.text, question.answer)
    question_bank.append(question)
