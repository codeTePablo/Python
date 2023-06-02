class QuizBrain:
    def __init__(self, q_list):
        self.question_list = q_list
        self.question_number = 0
        self.score = 0

    def next_question(self):
        # question list pos in question number
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        # text from data dict
        user_answer = input(f"Q. {self.question_number}: {current_question.text}")
        self.check_answer(user_answer, current_question.answer)

    def still_has_quest(self):
        return len(self.question_number) < len(self.question_list)

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print("correct")
            self.score += 1
        else:
            print("incorrect")
            print(f"you score is {self.score}")