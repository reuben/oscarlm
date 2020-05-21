import re
from . import LanguageBase


class Language(LanguageBase):
    def __init__(self):
        super(Language, self).__init__('en')
        self.substitutions = [
            (re.compile(r'\$'), 'dollar'),
            (re.compile(r'€'), 'euro'),
            (re.compile(r'£'), 'pound')
        ]
        self.alpha = 0.931289039105002
        self.beta = 1.1834137581510284
