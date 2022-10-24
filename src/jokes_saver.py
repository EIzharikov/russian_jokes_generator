"""
Jokes saver implementation
"""
from src.constants import PATH_TO_SAVE


class JokesSaver:  # pylint: disable=too-few-public-methods
    """
    Jokes saver implementation
    """
    def __init__(self):
        self._path_to_save = PATH_TO_SAVE

    def save_joke(self, joke_beginning, final_joke):
        """
        Saves jokes
        :param joke_beginning: the beginning of joke
        :param final_joke: full joke
        :return: nothing
        """
        with open(self._path_to_save / 'jokes_history.txt', 'a', encoding='UTF-8') as file:
            file.write(f'Начало шутки:  {joke_beginning}\n'
                       f'Вся шутка: {final_joke}\n'
                       f'<------------------------------------------->\n')


if __name__ == '__main__':
    pass
