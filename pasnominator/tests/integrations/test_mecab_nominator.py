import unittest

from pasnominator.mecab import nominator
from .spec import SPECS, expected_output


class MeCabNominatorTestCase(unittest.TestCase):
    def test_analyze(self):
        for spec in SPECS:
            with self.subTest(document=spec.document):
                if spec.skip:
                    self.skipTest(spec.document)
                actual = list(nominator.analyze(spec.document))
                self.assertEqual(expected_output(spec.expected), actual)
