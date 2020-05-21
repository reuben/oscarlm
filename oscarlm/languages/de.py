import re
from . import LanguageBase


class Language(LanguageBase):
    def __init__(self):
        super(Language, self).__init__('de')
        self.alphabet += 'äöüß'
        self.substitutions = [
            (re.compile(r'\$'), 'dollar'),
            (re.compile(r'€'), 'euro'),
            (re.compile(r'£'), 'pfund')
        ]
        self.alpha = 0.931289039105002
        self.beta = 1.1834137581510284
