class Question:
    def __init__(self, question_text, question_different, true_answer):
        self.question_text = question_text
        self.question_different = question_different
        self.true_answer = true_answer
        self.if_question = False
        self.user_answer = None
        self.score = question_different

    def get_points(self):
        return int(self.score) * 10

    """Возвращает int, количество баллов.
    Баллы зависят от сложности: за 1 дается 10 баллов, за 5 дается 50 баллов.
    """

    def is_correct(self):
        return self.true_answer == self.user_answer

    """Возвращает True, если ответ пользователя совпадает
    с верным ответов иначе False.
    """

    def build_question(self):
        return f'Вопрос: {self.question_text}\nСложность: {self.question_different}/5'

    """Возвращает вопрос в понятном пользователю виде, например:
    Вопрос: What do people often call American flag?
    Сложность 4/5
    """

    def build_positive_feedback(self):
        return f'Ответ верный, получено {self.get_points()} баллов'

    """Возвращает :
    Ответ верный, получено __ баллов
    """

    def build_negative_feedback(self):
        return f'Ответ неверный, верный ответ {self.true_answer}'

    """Возвращает :
    Ответ неверный, верный ответ __
    """
    def set_user_answer(self, answer: str):
        self.user_answer = answer

