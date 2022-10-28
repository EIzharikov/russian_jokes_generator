class TagTranslator:
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
        return self.tags_dict.get(tag)

    def get_tag_dict_values(self):
        return self.tags_dict.values()
