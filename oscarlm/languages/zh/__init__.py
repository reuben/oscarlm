import regex as re
import string
import unicodedata as ud

from .. import LanguageBase
from .cn_tn import NSWNormalizer, CHINESE_PUNC_LIST


class Language(LanguageBase):
    def __init__(self):
        super(Language, self).__init__('zh')
        self.alphabet = []
        self.substitutions = []
        self.simplify = False
        self.alpha = 0.931289039105002
        self.beta = 1.1834137581510284
        self.remove_punct_trans = str.maketrans(dict.fromkeys(CHINESE_PUNC_LIST + string.punctuation))
        self.removal_regex = re.compile(r'[^\p{Lo}]')

    def clean(self, line):
        line = line.translate(self.remove_punct_trans)
        line = NSWNormalizer(line).normalize()
        line = self.removal_regex.sub('', line)
        return [' '.join(line.replace(' ', ''))]
