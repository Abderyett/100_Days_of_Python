from data import question_data
from question_model import Questions
from quiz_brain import QuizBrain


class User:
    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        self.followers = 0  # Default Value
        self.following = 0  # Default Value

    def follow(self, user):
        user.followers += 1
        self.following += 1


# user_1 = User("001", "Jesse")
# user_2 = User("002", "James")

# user_1.follow(user_2)

# print("user_1 following", user_1.following)
# print("user_1 followers", user_1.followers)

# print("user_2 following", user_2.following)
# print("user_2 followers", user_2.followers)

question_bank = []


for question in question_data:
    new_q = Questions(question["text"], question["answer"])
    question_bank.append(new_q)


quiz = QuizBrain(question_bank)
while quiz.still_have_questions():

    quiz.next_question()
