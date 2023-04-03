import uuid


class QuizAnswer(object):
    def __init__(self, quiz):
        self.__quiz = quiz
        self.__id = uuid.uuid4()
        self.__answers = []

    @property
    def answers(self):
        return self.__answers

    @answers.setter
    def answers(self, new_value):
        self.__answers = new_value

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, new_value):
        self.__id = new_value

    @property
    def quiz(self):
        return self.__quiz

    @quiz.setter
    def quiz(self, new_value):
        self.__quiz = new_value

    def add_answer(self, answer):
        self.answers.append(answer)


class Answer(object):
    def __init__(self, answers, question):
        self.question = question
        self.answers = answers

