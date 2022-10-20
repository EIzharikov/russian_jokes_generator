from models.models_init import CustomRuGPT3Model, PretrainedModel


class MessageRequest:
    def __init__(self):
        self.custom_model = CustomRuGPT3Model()
        self.pretrained_model = PretrainedModel()
        self.model_type = "Чужая модель"
        self.length = 30
        self.tag = None
        self.text = ""

    def process_request(self):
        if self.model_type == "Наша модель":
            return self.custom_model.generate_joke(self.text, self.tag, self.length)
        else:
            return self.pretrained_model.generate_joke(self.text, self.length)
        # return self.model_type, self.length, self.tag, self.text

    def _stats(self):
        print(self.model_type, type(self.length), self.tag, self.text)


if __name__ == '__main__':
    mes = MessageRequest()
