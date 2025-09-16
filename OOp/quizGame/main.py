from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for x in question_data:
    question_text = x["text"]
    question_answer = x["answer"]
    new_question = Question(question_text,question_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)

while quiz.stillHasQuestion():
    quiz.nextQuestion()

print("You have completed the Quiz Challenge !!!!!!")
print(f"Your final score is: {quiz.score}/{quiz.question_number}")