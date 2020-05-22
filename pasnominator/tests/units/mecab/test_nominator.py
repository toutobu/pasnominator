import unittest

from pasnominator import Morpheme, PASUnit, UnitType
from pasnominator.mecab import nominator


class NominatorTestCase(unittest.TestCase):
    def test_analyze(self):
        result = list(nominator.analyze('太郎が花子にリンゴをあげた。'))

        self.assertIsInstance(result[0], PASUnit)
        self.assertEqual(result[0].text, '太郎')
        self.assertIsInstance(result[0].morphemes, list)
        self.assertIsInstance(result[0].morphemes[0], Morpheme)
        self.assertEqual(len(result[0].morphemes), 1)
        self.assertEqual(result[0].morphemes[0].surface, '太郎')
        self.assertEqual(result[0].morphemes[0].pos, '名詞')
        self.assertEqual(result[0].morphemes[0].subpos1, '固有名詞')
        self.assertEqual(result[0].morphemes[0].form, '太郎')

        self.assertEqual(result[1].text, 'が')
        self.assertEqual(len(result[1].morphemes), 1)
        self.assertEqual(result[1].morphemes[0].surface, 'が')

        self.assertEqual(result[2].text, '花子')
        self.assertEqual(len(result[2].morphemes), 1)
        self.assertEqual(result[2].morphemes[0].surface, '花子')

        self.assertEqual(result[3].text, 'に')
        self.assertEqual(len(result[3].morphemes), 1)
        self.assertEqual(result[3].morphemes[0].surface, 'に')

        self.assertEqual(result[4].text, 'リンゴ')
        self.assertEqual(len(result[4].morphemes), 1)
        self.assertEqual(result[4].morphemes[0].surface, 'リンゴ')

        self.assertEqual(result[5].text, 'を')
        self.assertEqual(len(result[5].morphemes), 1)
        self.assertEqual(result[5].morphemes[0].surface, 'を')

        self.assertEqual(result[6].text, 'あげ')
        self.assertEqual(len(result[6].morphemes), 1)
        self.assertEqual(result[6].morphemes[0].surface, 'あげ')
        self.assertEqual(result[6].unit, UnitType.PREDICATE)

        self.assertEqual(result[7].text, 'た')
        self.assertEqual(len(result[7].morphemes), 1)
        self.assertEqual(result[7].morphemes[0].surface, 'た')

        self.assertEqual(result[8].text, '。')
        self.assertEqual(len(result[8].morphemes), 1)
        self.assertEqual(result[8].morphemes[0].surface, '。')
