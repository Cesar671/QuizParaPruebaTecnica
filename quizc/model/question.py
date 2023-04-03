class Question(object):
    def __init__(self, title, question_type, validations):
        self.__title = title
        self.__type = question_type
        self.__validations = validations
        self.__additional_data = []

    @property
    def additional_data(self):
        return self.__additional_data

    @additional_data.setter
    def additional_data(self, new_value):
        self.__additional_data = new_value

    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, new_value):
        self.__title = new_value

    @property
    def type(self):
        return self.__type

    @type.setter
    def type(self, new_value):
        self.__type = new_value

    @property
    def validations(self):
        return self.__validations

    @validations.setter
    def validations(self, new_value):
        self.__validations = new_value


class QuestionBuilder(object):
    def __init__(self, title, question_type):
        self.__question_type = question_type
        self.__title = title
        self.__validations = []
        self.__additional_data = []

    @property
    def additional_data(self):
        return self.__additional_data

    @additional_data.setter
    def additional_data(self, new_value):
        self.__additional_data = new_value

    @property
    def validations(self):
        return self.__validations

    @validations.setter
    def validations(self, new_value):
        self.__validations = new_value

    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, new_value):
        self.__title = new_value

    @property
    def question_type(self):
        return self.__question_type

    @question_type.setter
    def question_type(self, new_value):
        self.__question_type = new_value

    def add_validation(self, validation):
        if validation in self.validations:
            return False
        self.validations.append(validation)
        return True

    def build(self):
        question = Question(self.title, self.question_type, self.validations)
        if len(self.additional_data) > 0:
            question.additional_data = self.additional_data
        return question
