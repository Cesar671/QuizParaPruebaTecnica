class QuestionInputHandler(object):
    MENU_PROMPT = "> "

    def ask_question_value(self, question):
        print("Question:" + question.title)
        return self.get_answer(question)

    def get_answer(self, question):
        if question.type.configuration.has_additional_data:
            answers = self.collect_answer_options(question)
        else:
            print(question.type.name + ' value:')
            answers = [self.get_validated_answer(question.validations)]
        return answers

    def get_validated_answer(self, validations=[]):
        while True:
            entry = input(self.MENU_PROMPT)
            errors = []
            for valid in validations:
                valid.validate(entry, condition_value=None, errors=errors)

            if len(errors) == 0:
                break
            for st in errors:
                print(st)

    def collect_answer_options(self, question):
        options = []
        while True:
            self.show_options(question)
            option = input(self.MENU_PROMPT)
            if option == "0":
                break
        return options

    def show_options(self, question):
        index = 1
        print("Select an option:")
        for option in question.additional_data:
            print("{index}. {option}".format(index=index, option=option))
            index += 1
        print("0. To Finish")
