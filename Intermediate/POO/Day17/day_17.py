# Attribute 

from data import question_data
from question import Question
from quiz_brain import QuizBrain
# class User:
#     def __init__(self, name):
#         self.id = name
#         # declare attribute with value, no declaring like a attribute in init
#         self.followers = 0
#         self.following = 0

#     def follow(self, user):
#         user.followers += 1
#         self.following += 1

# # declare object 
# person = User("nk-2")
# person_1 = User("nk-2")
# # print id 
# person.follow(person_1)
# print(person.followers)
# print(person.following)

question_bank = []

for i in question_data:
    question_text = i["text"]
    question_answer = i["answer"]
    new_question = Question(question_text,question_answer)
    question_bank.append(new_question)

# print(question_bank[0])

quiz = QuizBrain(question_bank)
while quiz.still_has_quest:
    quiz.next_question()
