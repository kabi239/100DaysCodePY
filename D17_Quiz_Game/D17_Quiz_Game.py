from logo import logo
from question_model import Question
from data import data1,data2,data3
from quizi_brain import Brain
print(logo) 


question_bank=[]
for question in data3:
    question_text=question["text"]
    question_answer=question["answer"]
    new_question=Question(question_text,question_answer)
    question_bank.append(new_question)

quiz=Brain(question_bank)
while quiz.still_has_question():
    quiz.next_question()

print("You've compleates the quiz. ")
print(f"Your final score was{quiz.score}/{quiz.question_no}. ")