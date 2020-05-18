import MeCab

from .. import Morpheme, PASUnit


tagger = MeCab.Tagger()
tagger.parse('')


def analyze(text):
    node = tagger.parseToNode(text)

    while node:
        surface = node.surface
        features = node.feature.split(',')

        if features[0] != 'BOS/EOS':
            yield PASUnit(
                text=surface,
                morphemes=[
                    Morpheme(
                        surface=surface,
                        pos=features[0],
                        subpos1=features[1],
                        form=features[-3])])

        node = node.next
