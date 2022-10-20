"""
Configurations for JokesSpider
"""

HEADERS = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
                  " AppleWebKit/537.36 (KHTML, like Gecko) "
    "Chrome/98.0.4758.102 Safari/537.36"
}
START_URLS = [
    "https://humornet.ru/anekdot/eat/",  # food
    "https://humornet.ru/anekdot/politics/",  # politics
    "https://humornet.ru/anekdot/cats/",  # pets
    "https://humornet.ru/anekdot/poshlye/",  # 18+
    "https://humornet.ru/anekdot/pro-rabotu/",  # work
    "https://humornet.ru/anekdot/pc/",  # computers
    "https://humornet.ru/anekdot/children/",  # children
    "https://humornet.ru/anekdot/pro-shtirlica/",  # Shtirlitz
    "https://humornet.ru/anekdot/pro-studentov/",  # students
    "https://humornet.ru/anekdot/pro-sosedey/",  # neighbours
]
