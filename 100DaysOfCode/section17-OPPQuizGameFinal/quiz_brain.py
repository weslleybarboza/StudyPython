class QuizBrain:

    def __init__(self, question_list):
        self.question_number = 0
        self.score = 0
        self.question_list = question_list

    def still_has_question(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        question_text = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q. {self.question_number}: {question_text.text} (True/False): ")
        self.check_answer(user_answer, question_text.answer)

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print("You got ir right!")
        else:
            print("That's wrong.")
        print(f"The correct answer was: {correct_answer}.")
        print(f"Your current score is: {self.score}/{self.question_number}")
        print("\n")
