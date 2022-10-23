"""
Message Request implementation
"""
from models.models_init import CustomRuGPT3Model, PretrainedModel


class MessageRequest:
    """
    Message Request implementation
    """

    def __init__(self):
        self._custom_model = CustomRuGPT3Model()
        self._pretrained_model = PretrainedModel()
        self._model_type = "Чужая модель"
        self._length = 30
        self._tag = None
        self._text = ""

    def __str__(self):
        return f'Model type is {self._model_type},\n' \
               f'Max length of text is {self._length}\n' \
               f'Tag is {self._tag}\n' \
               f'Text of the message is {self._text}'

    def get_settings(self):
        return self._text, self._tag, self._length, self._model_type

    def process_request(self):
        """
        Process the message request
        """
        if self._model_type == "Наша модель":
            return self._custom_model.generate_joke(self._text, self._tag, self._length)
        return self._pretrained_model.generate_joke(self._text, self._length)

    def set_model_type(self, model_type):
        """
        Set model type in message request
        """
        self._model_type = model_type

    def set_text(self, text):
        """
        Set text in message request
        """
        self._text = text

    def set_length(self, length):
        """
        Set max length in message request
        """
        self._length = int(length)

    def set_tag(self, tag):
        """
        Set tag of the text in message request
        """
        self._tag = tag


if __name__ == '__main__':
    pass
