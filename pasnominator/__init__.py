from collections import namedtuple


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
