from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

# Lesson learned: Always put variables above everything
'''' _______________________[ ↓ Variables down here ↓ ]_______________________'''

question_bank = []
data = question_data['category']
category_choice = input('Choose a category [CS, Games, Mathematics]: ').capitalize()  #alway put input up top

category = question_data['category'][category_choice]
Q = category[0]['question']
A = category[0]['correct_answer']
quiz = QuizBrain(question_bank)


'''' _____________________[ ↓ Code & Calling function ↓ ]_____________________'''

for question in category:
    each_question = question['question']
    new_question = Question(Q, A)
    question_bank.append(each_question)

while quiz.still_has_question():
    print('Question Bank: ', question_bank)
    p_answer = quiz.nextQuestion()  # contain input

    quiz.track_score(p_answer, A)
    quiz.still_has_question()  # print more questions
    print()
