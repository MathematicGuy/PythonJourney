from data import question_data
import random

class Question:

    def __init__(self, QText, QAnswers):
        self.text = QText
        self.answers = QAnswers


point = 0
totalQuiz = 0

random.shuffle(question_data)

for quiz in question_data['results']:
    random_Q = quiz['text']
    random_A = quiz['answer']
    category_Q = question_data['result'][quiz]['category']


    totalQuiz += 1

    answer = input(f"{random_Q} True or False: ").capitalize()
    newQuestion = Question(random_Q, random_A)

    if answer == "True" or answer == "False":
        if answer == random_A:
            print("Correct, point + 1")
            point += 1
        elif answer != random_A:
            print("Incorrect")
        print(f'The answer is: {newQuestion.answers}')
    else:
        print("Pls only enter True or False")

    print(f'Your current score: {point}/{totalQuiz}')
    print('.oOo.oOo.oOo.'*8)

print("That for today game show, Come back again")
print(point)
