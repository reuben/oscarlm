import re
from . import LanguageBase


class Language(LanguageBase):
    def __init__(self):
        super(Language, self).__init__(__file__)
        self.alphabet += 'áâãàçéêíóôõú'
        self.substitutions = []
        self.alpha = 0.931289039105002
        self.beta = 1.1834137581510284
