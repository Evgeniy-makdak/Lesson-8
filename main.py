import json
import random
from question import Question

with open('question.json', 'r', encoding='utf-8') as file:
    question_list = json.load(file)

questions = []
for question in question_list:
    d = Question(question['q'], question['d'], question['a'])
    questions.append(d)

random.shuffle(questions)
for question in questions:
    print("-" * 40)
    print(question.build_question())
    user_answer = input("Введите ответ:")
    question.set_user_answer(user_answer)

    if question.is_correct() is True:
        print(question.build_positive_feedback())

    else:
        print(question.build_negative_feedback())
        print("-" * 40)


def get_total(questions: list) -> None:
    sum_score = 0
    count = 0
    for question in questions:
        if question.is_correct():
            sum_score += question.get_points()
            count += 1
    print("-" * 40)
    print("Вот и все!")
    print(f"Отвечено {count} вопроса из {len(questions)}")
    print(f"Набранно {sum_score} баллов")
    print("-" * 40)


get_total(questions)
