
class QuizBrain():
    def __init__(self, q_list):
        self.question_number = 0
        self.score = 0
        self.question_list = q_list

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        answer = input(
            f"Q.{self.question_number}: {current_question.text}  (True/False) : ").capitalize()
        self.check_answer(answer, current_question.answer)

    def still_have_questions(self):
        return self.question_number < len(self.question_list)

    def check_answer(self, answer, correct_answer):

        if answer == correct_answer:
            self.score += 1
            print('You got it Right!')

        else:
            print('That was wrong!')
        print(
            f"Your current score is: {self.score}/{self.question_number}")
        print("\n")
