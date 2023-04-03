import datetime
from enum import Enum
from quizc.model.validations import ValidatorType
import re


class QuestionConfiguration(object):
    def __init__(self, has_additional_data, supported_validations):
        self.__has_additional_data = has_additional_data
        self.__supported_validations = supported_validations

    @property
    def supported_validations(self):
        return self.__supported_validations

    @supported_validations.setter
    def supported_validations(self, new_value):
        self.__supported_validations = new_value

    @property
    def has_additional_data(self):
        return self.__has_additional_data

    @has_additional_data.setter
    def has_additional_data(self, new_value):
        self.__has_additional_data = new_value

    def convert_value(self, value):
        return value


class TextConfiguration(QuestionConfiguration):
    def __init__(self):
        QuestionConfiguration.__init__(self, False, [ValidatorType.REQUIRED, ValidatorType.MIN_LENGTH])


class DateConfiguration(QuestionConfiguration):
    DATE_FORMAT = '%d/%m/%Y'

    def __init__(self):
        QuestionConfiguration.__init__(self, False, [ValidatorType.REQUIRED, ValidatorType.DATE])

    def convert_value(self, value):
        try:
            return datetime.datetime.strptime(value, DateConfiguration.DATE_FORMAT)
        except ValueError:
            return None


class NumericConfiguration(QuestionConfiguration):
    REGEX = '^[0-9]*$'

    def __init__(self):
        QuestionConfiguration.__init__(self, False, [ValidatorType.REQUIRED, ValidatorType.NUMERIC])

    def convert_value(self, value):
        if re.search(self.REGEX, str(value)):
            return int(value)
        else:
            return None


class PickOneQuestionConfiguration(QuestionConfiguration):
    def __init__(self):
        QuestionConfiguration.__init__(self, True, [ValidatorType.REQUIRED])


class QuestionType(Enum):
    TEXT = (1, TextConfiguration())
    DATE = (2, DateConfiguration())
    PICK_ONE = (3, PickOneQuestionConfiguration())
    NUMERIC = (4, NumericConfiguration())

    def __init__(self, code, configuration):
        self.__code = code
        self.__configuration = configuration

    @property
    def configuration(self):
        return self.__configuration

    @configuration.setter
    def configuration(self, new_value):
        self.__configuration = new_value

    @property
    def code(self):
        return self.__code

    @code.setter
    def code(self, new_value):
        self.__code = new_value

    def get_validations(self):
        return self.configuration.supported_validations

    def get_code(self):
        return self.code

    def has_additional_data(self):
        return self.configuration.has_additional_data

    @staticmethod
    def get_by_code(code) :
        for question_type in QuestionType:
            if question_type.code == code or question_type.code == int(code):
                return question_type
        return None
