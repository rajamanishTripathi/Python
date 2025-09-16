
class QuizBrain:
    def __init__(self, q_list):
        self.question_number= 0
        self.score = 0
        self.question_list = q_list

    def stillHasQuestion(self):
        return self.question_number < len(self.question_list)

    def nextQuestion(self):
        currentquestion = self.question_list[self.question_number]
        self.question_number +=1
        useranswer = input(f"Q.{self.question_number}: {currentquestion.text} (True/False):  ")
        self.check_answer(useranswer,currentquestion.answer)

    def check_answer(self, useranswer, correctanswer):
        if useranswer.lower() == correctanswer.lower():
            print("Correct Answer")
            self.score +=1
        else:
            print("That's wrong")
        print(f"The Correct Answer is :  {correctanswer}")
        print(f"Your score is : {self.score}/{self.question_number}")
        print("\n")