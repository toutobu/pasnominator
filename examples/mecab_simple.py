from pasnominator import nominator


if __name__ == '__main__':
    # NOTE: ここまで前処理でできると楽なんだけどなぁ
    # 最悪、形態素単位(a)、できれば述語単位(b)、できれば格関係(c)まで付与
    # b までできれば、paselector としては十分(c は要らない？)
    # c までできると、アノテーションが楽なはず

    # TODO: 最新の仕様に更新する
    print(nominator.analyze('太郎が花子にリンゴをあげた。'))
    # [
    #   PASUnit(
    #     unit=UnitType.HAArgument,
    #     text='太郎',
    #     morphemes=[Morpheme(surface='太郎'...)]),
    #   PASUnit(
    #     unit=UnitType.Other,
    #     text='は',
    #     morphemes=[Morpheme(surface='は'...)]),
    #   ...
    # ]

    print(nominator.analyze('A社は新型交換機を導入する。'))
    # [
    #   PASUnit(
    #     unit=UnitType.HAArgument,
    #     text='A社',
    #     morphemes=[Morpheme(surface='A'...), Morpheme(surface='社'...)]),
    #   PASUnit(
    #     unit=UnitType.Other,
    #     text='は',
    #     morphemes=[Morpheme(surface='は'...)]),
    #   PASUnit(
    #     unit=UnitType.WOArgument,
    #     text='新型交換機',
    #     morphemes=[Morpheme(surface='新型'...), ...]),
    #   ...
    #   PASUnit(
    #     unit=UnitType.Predicate,
    #     text='導入する',
    #     morphemes=[Morpheme(surface='導入'...), ...]),
    #   PASUnit(
    #     text='。',
    #     morphemes=[Morpheme(surface='は'...)]),
    # ]
