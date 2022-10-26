"""
Models implementation
"""
import re
from pathlib import Path
from abc import ABC, abstractmethod

import gdown
from transformers import GPT2LMHeadModel, GPT2Tokenizer

from src.constants import CUSTOM_MODEL_FOLDER, PRETRAINED_MODEL_FOLDER, TAGS_DICT, CUSTOM_MODEL_ID, PRETRAINED_MODEL_ID


class Model(ABC):  # pylint: disable=too-few-public-methods
    """
    Abstract class for Models
    """

    @abstractmethod
    def _download_model(self):
        pass

    @abstractmethod
    def _is_downloaded_model(self):
        pass

    @abstractmethod
    def _load_tokenizer_and_model(self):
        pass


class CustomRuGPT3Model(Model):  # pylint: disable=too-few-public-methods
    """
    Custom Model implementation
    """

    def __init__(self):
        self.model_path = CUSTOM_MODEL_FOLDER
        self.tokenizer, self.model = self._load_tokenizer_and_model()

    def _download_model(self):
        gdown.download(
            id=CUSTOM_MODEL_ID,
            output=str(CUSTOM_MODEL_FOLDER / 'pytorch_model.bin'),
        )

    def _is_downloaded_model(self):
        if Path(CUSTOM_MODEL_FOLDER / 'pytorch_model.bin').exists():
            return True
        return False

    def _load_tokenizer_and_model(self):
        if not self._is_downloaded_model():
            self._download_model()
        return GPT2Tokenizer.from_pretrained(
            self.model_path
        ), GPT2LMHeadModel.from_pretrained(self.model_path)

    @staticmethod
    def _prepare_prompt(text, tag):
        prompt = f"<|startoftext{tag}|>{text}"
        return prompt

    def generate_joke(self, text: str, tag: str, max_len: int):
        """
        Generates the joke
        :param text: string with text
        :param tag: tag for type of joke
        :param max_len: max length of final joke
        :return: the final joke
        """
        if not isinstance(text, str) \
                or not isinstance(max_len, int) \
                or not isinstance(tag, str):
            return 0

        if max_len not in list(range(30, 110, 10)):
            return 0

        if tag not in list(TAGS_DICT.values()):
            return 0

        prompt = self._prepare_prompt(text, tag)
        input_ids = self.tokenizer.encode(prompt, return_tensors="pt")
        result = self.model.generate(
            input_ids,
            num_return_sequences=1,
            max_length=max_len,
            repetition_penalty=8.0,
            do_sample=True,
            top_k=10,
            top_p=1,
            temperature=1,
            num_beams=15,
            no_repeat_ngram_size=3,
            pad_token_id=50256,
        )
        output = re.split(
            "<",
            re.sub(
                r"<\|startoftext[\w-]*\|>|©.*",
                "",
                list(map(self.tokenizer.decode, result))[0],
                count=1,
            ),
        )[0].split("\n")[0]

        return output


class PretrainedModel(Model):  # pylint: disable=too-few-public-methods
    """
    Pretrained Model implementation
    """

    def __init__(self):
        self.model_path = PRETRAINED_MODEL_FOLDER
        self.tokenizer, self.model = self._load_tokenizer_and_model()

    def _download_model(self):
        gdown.download(
            id=PRETRAINED_MODEL_ID,
            output=str(PRETRAINED_MODEL_FOLDER / 'pytorch_model.bin'),
        )

    def _is_downloaded_model(self):
        if Path(PRETRAINED_MODEL_FOLDER / 'pytorch_model.bin').exists():
            return True
        return False

    def _load_tokenizer_and_model(self):
        if not self._is_downloaded_model():
            self._download_model()
        return GPT2Tokenizer.from_pretrained(
            self.model_path
        ), GPT2LMHeadModel.from_pretrained(self.model_path)

    @staticmethod
    def _prepare_prompt(text):
        prompt = f"<|startoftext|>{text}"
        return prompt

    def generate_joke(self, text: str, max_len: int):
        """
        Generates the joke
        :param text: string with text
        :param max_len: max length of final joke
        :return: the final joke
        """
        if not isinstance(text, str) \
                or not isinstance(max_len, int):
            return 0

        if max_len not in [30, 40, 50, 60, 70, 80, 90, 100]:
            return 0

        prompt = self._prepare_prompt(text)
        input_ids = self.tokenizer.encode(prompt, return_tensors="pt")
        result = self.model.generate(
            input_ids,
            num_return_sequences=1,
            max_length=max_len,
            repetition_penalty=8.0,
            do_sample=True,
            top_k=10,
            top_p=1,
            temperature=1,
            num_beams=15,
            no_repeat_ngram_size=3,
            pad_token_id=50256,
        )
        output = re.split(
            "<",
            re.sub(
                r"<\|startoftext[\w-]*\|>|©.*",
                "",
                list(map(self.tokenizer.decode, result))[0],
                count=1,
            ),
        )[0].split("\n")[0]
        return output


if __name__ == '__main__':
    pass
