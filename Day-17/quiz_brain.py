
class QuizBrain():
    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        answer = input(
            f"Q.{self.question_number}: {current_question.text}  (True/False) : ").capitalize()

    def still_have_questions(self):
        if self.question_number-1 == len(self.question_list):
            return False
        else:
            return True

            # if answer == current_question["answer"]:
            #       print('You got it Right!')
            #       print(f"Your current score is: 1/{self.question_number}")
            #   else:
            #       print('That was wrong!')
