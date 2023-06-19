from src.item import Item


class MixinLang:
    langs = ("EN", "RU")

    def __init__(self, name: str, price: float, quantity: int):
        super().__init__(name, price, quantity)
        self.__language = self.langs[0]

    def change_lang(self):
        MixinLang.langs = self.langs[::-1]
        self.__language = self.langs[0]
        if self.__language in self.langs:
            return self


    @property
    def language(self):
        return self.__language

    @language.setter
    def language(self, language):
        if language not in self.langs:
            raise ValueError("Данный язык не найден")


class Keyboard(MixinLang, Item):

    def __init__(self, name: str, price: float, quantity: int):
        super().__init__(name, price, quantity)
