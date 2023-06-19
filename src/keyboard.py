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
        else:
            raise ValueError(f"AttributeError: property 'language' of 'KeyBoard' object has no setter")

    @property
    def language(self):
        return self.__language


class Keyboard(MixinLang, Item):
    def __init__(self, name: str, price: float, quantity: int):
        super().__init__(name, price, quantity)
