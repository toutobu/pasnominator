import logging
import MeCab

from ..unit import Morpheme, PASUnit, POS


logger = logging.getLogger(__name__)

tagger = MeCab.Tagger()
tagger.parse('')


def analyze(document):
    def start_idx_of_compound_term(end_idx):
        start_idx = end_idx
        while (start_idx >= 0
               and is_noun_or_alphabet_symbol(morphemes[start_idx])):
            start_idx -= 1
        return start_idx + 1

    morphemes = [
        make_morpheme(chunk) for chunk
        in tagger.parse(document).splitlines()[:-1]]

    idx = 0

    while idx < len(morphemes):
        current = morphemes[idx]

        if (idx > 0 and is_s_irregular_noun(morphemes[idx - 1])
                and current.pos == POS.VERB.value
                and current.form == 'する'):
            # 「サ変名詞+"する"」の場合はこれを述語とする [乾 2013]
            logger.debug(f'Rule: 「サ変名詞+"する"」')
            compound = morphemes[start_idx_of_compound_term(idx - 1):idx]
            yield make_pas_unit(compound + [current])
        elif (current.pos == POS.VERB.value
              and idx + 2 < len(morphemes)
              and morphemes[idx + 1].pos == POS.PARTICLE.value
              and morphemes[idx + 1].form == 'て'
              and morphemes[idx + 2].pos == POS.VERB.value
              and morphemes[idx + 2].form == 'ある'):
            # テアル形の場合は，「述語+てある」を原型 と考えてタグを付与する．[乾 2013]
            compound = morphemes[start_idx_of_compound_term(idx - 1):idx]
            yield make_pas_unit(
                compound + [current] + morphemes[idx + 1:idx + 3])
            # 「て」「ある」分 idx を進める
            idx += 2
        elif not is_noun_or_alphabet_symbol(current):
            compound = morphemes[start_idx_of_compound_term(idx - 1):idx]

            if len(compound) > 0:
                yield make_pas_unit(compound)

            yield make_pas_unit([current])

        idx += 1


def is_noun_or_alphabet_symbol(m):
    return (m.pos == POS.NOUN.value or
            (m.pos == POS.SYMBOL.value and m.subpos1 == 'アルファベット'))


def is_s_irregular_noun(morpheme):
    return morpheme.pos == POS.NOUN.value and morpheme.subpos1 == 'サ変接続'


def make_pas_unit(morphemes):
    return PASUnit(
        text=''.join(m.surface for m in morphemes),
        morphemes=morphemes)


def make_morpheme(chunk):
    surface, feature = chunk.split('\t')
    features = feature.split(',')
    return Morpheme(surface, features[0], features[1], features[-3])
