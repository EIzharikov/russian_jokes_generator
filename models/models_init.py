import re
import gdown

from abc import ABC, abstractmethod

from pathlib import Path
from transformers import GPT2LMHeadModel, GPT2Tokenizer


class Model(ABC):
    @abstractmethod
    def _download_model(self):
        pass

    @abstractmethod
    def _is_downloaded_model(self):
        pass

    @abstractmethod
    def _load_tokenizer_and_model(self):
        pass

    @staticmethod
    @abstractmethod
    def _prepare_prompt(text, tag):
        pass


class CustomRuGPT3Model(Model):
    def __init__(self):
        self.model_path = ""

    def _download_model(self):
        gdown.download(
            id="19Glj9TXG44eG0HAHS3PPGVxn41O2gNYY",
            output="models_config/custom/pytorch_model.bin",
        )
        self.model_path = "models/models_config/custom"

    def _is_downloaded_model(self):
        if not Path("models/models_config/custom/pytorch_model.bin").is_file():
            return 0
        return 1

    def _load_tokenizer_and_model(self):
        if not self.model_path:
            self._download_model()
        return GPT2Tokenizer.from_pretrained(
            self.model_path
        ), GPT2LMHeadModel.from_pretrained(self.model_path)

    @staticmethod
    def _prepare_prompt(text, tag):
        prompt = f"<|startoftext{tag}|>{text}"
        return prompt

    def generate_joke(self, text: str, tag: str, max_len: int):
        if not isinstance(text, str) or not isinstance(max_len, int):
            return 0

        if max_len not in [30, 40, 50, 60, 70, 80, 90, 100]:
            return 0

        tokenizer, model = self._load_tokenizer_and_model()
        prompt = self._prepare_prompt(text, tag)
        input_ids = tokenizer.encode(prompt, return_tensors="pt")
        result = model.generate(
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
                list(map(tokenizer.decode, result))[0],
                count=1,
            ),
        )[0].split("\n")[0]

        return output


class PretrainedModel(Model):
    def __init__(self):
        self.model_path = ""

    def _download_model(self):
        gdown.download(
            id="1iJtv6WzShrn23M_ggvtFhXon3dopBA9x",
            output="models_config/pretrained/pytorch_model.bin",
        )
        self.model_path = "models/models_config/pretrained"

    def _is_downloaded_model(self):
        if not Path("models/models_config/pretrained/pytorch_model.bin").is_file():
            return 0
        return 1

    def _load_tokenizer_and_model(self):
        if not self.model_path:
            self._download_model()
        return GPT2Tokenizer.from_pretrained(
            self.model_path
        ), GPT2LMHeadModel.from_pretrained(self.model_path)

    @staticmethod
    def _prepare_prompt(text):
        prompt = f"<|startoftext|>{text}"
        return prompt

    def generate_joke(self, text: str, max_len: int):
        if not isinstance(text, str) or not isinstance(max_len, int):
            return 0

        if max_len not in [30, 40, 50, 60, 70, 80, 90, 100]:
            return 0

        tokenizer, model = self._load_tokenizer_and_model()
        prompt = self._prepare_prompt(text)
        input_ids = tokenizer.encode(prompt, return_tensors="pt")
        result = model.generate(
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
                list(map(tokenizer.decode, result))[0],
                count=1,
            ),
        )[0].split("\n")[0]
        return output


m = CustomRuGPT3Model()
print(m.generate_joke("Наливаю чай", "eat", 70))
