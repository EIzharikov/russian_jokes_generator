"""
Tag Translator implementation
"""


class TagTranslator:
    """
    Class for tag translation
    """
    def __init__(self):
        self.tags_dict = {
            "Еда": "eat",
            "Политика": "politics",
            "Коты": "cats",
            "Пошлые": "poshlye",
            "Про работу": "pro-rabotu",
            "Компьютеры": "pc",
            "Дети": "children",
            "Про Штирлица": "pro-shtirlica",
            "Про студентов": "pro-studentov",
            "Про соседей": "pro-sosedey"
        }

    def get_tag(self, tag):
        """
        Get tag value from tags_dict
        """
        return self.tags_dict.get(tag)

    def get_tag_dict_values(self):
        """
        Get all tags values
        """
        return self.tags_dict.values()
