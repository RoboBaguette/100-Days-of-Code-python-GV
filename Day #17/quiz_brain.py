class QuizB:
    def __init__(self, q_lis):
        self.q_num = 0
        self.score = 0
        self.q_list = q_lis

    def sill_qus(self):
        if self.q_num < len(self.q_list):
            return True
        else:
            return False

    def next_q(self):
        curr_q = self.q_list[self.q_num]
        self.q_num += 1
        user_ans = input(f"Q.{self.q_num}: {curr_q.text} (True/False): ")
        self.check_ans(user_ans, curr_q.ans)

    def check_ans(self, user_answer, corr_ans):
        if user_answer.lower() == corr_ans.lower():
            print("You got it right")
            self.score += 1
        else:
            print("That's wrong")
        print(f"The correct answer is {corr_ans}.")
        print(f"Your current score is: {self.score}/{self.q_num}")
        print("\n")
