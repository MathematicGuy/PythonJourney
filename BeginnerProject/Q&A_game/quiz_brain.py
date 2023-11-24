def score(current_score, total_score):
    print(f'Your current score: {current_score}/{total_score}')


class QuizBrain:

    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.current_score = 0
        print('Question length: ', len(self.question_list))

    def still_has_question(self):  # activate while list when True
        return self.question_number < len(self.question_list)

    def track_score(self, p_answer, q_answer):
        if p_answer == q_answer:
            self.current_score += 1
            print("That Correct, score + 1")
        elif p_answer != q_answer:
            print("Incorrect")

        print('Current score: {}/{}'.format(self.current_score, self.question_number))

    def nextQuestion(self):
        next_question = self.question_list[self.question_number]
        q_rank = self.question_number
        self.question_number += 1
        answer = input('Q.{}: {}, True or False: '.format(q_rank, next_question)).capitalize()
        return answer
