from question_model import Question
from data import question_data
from quiz_brain import QuizB
q_bank = []

for q in question_data:
    q_text = q["text"]
    q_ans = q["answer"]
    new_qus = Question(q_text, q_ans)
    q_bank.append(new_qus)

quiz_b = QuizB(q_bank)

while quiz_b.sill_qus():
    quiz_b.next_q()

print(f"You have completed the quiz\nYour final score was: {quiz_b.score}/{quiz_b.q_num} ")