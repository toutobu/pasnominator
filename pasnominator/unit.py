from collections import namedtuple
from enum import Enum


class PASUnit(namedtuple('PASUnit', [
    'text',
    'morphemes'
])):
    pass


class Morpheme(namedtuple('Morpheme', [
    'surface',
    'pos',
    'subpos1',
    'form'
])):
    pass


class POS(Enum):
    NOUN = '名詞'
    VERB = '動詞'
    ADJECTIVE = '形容詞'
    PARTICLE = '助詞'
    AUXILIARY_VERB = '助動詞'
    ADVERB = '副詞'

    SYMBOL = '記号'
    BOS_EOS = 'BOS/EOS'

    def __repr__(self):
        return '<%s.%s>' % (self.__class__.__name__, self.name)
