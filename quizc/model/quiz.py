class Quiz(object):
    def __init__(self, title):
        self.__title = title
        self.__questions = []

    @property
    def questions(self):
        return self.__questions

    @questions.setter
    def questions(self, new_value):
        self.__questions = new_value

    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, new_value):
        self.__title = new_value

    def add_question(self, question):
        self.questions.append(question)

