from collections import namedtuple

from pasnominator import Morpheme, PASUnit, UnitType


OTHER, PREDICATE = UnitType.OTHER, UnitType.PREDICATE

Spec = namedtuple(
    'Spec',
    ['document', 'expected', 'skip', 'violate_naist_rule'],
    defaults=(False, None))

# TODO: NAIST のアノテーション仕様に揺らぎがある気がする…
# どうしても論理的に解決できないものについては、せめてコメントで言い訳をしておく

# TODO: unit フラグについては NAIST の仕様書と矛盾している箇所が多くあるので対応する(#9)


SPECS = [
    Spec(
        document='太郎が花子にリンゴをあげた。',
        expected=[
            ('太郎', [('太郎', '名詞', '固有名詞', '太郎')]),
            ('が', [('が', '助詞', '格助詞', 'が')]),
            ('花子', [('花子', '名詞', '固有名詞', '花子')]),
            ('に', [('に', '助詞', '格助詞', 'に')]),
            ('リンゴ', [('リンゴ', '名詞', '一般', 'リンゴ')]),
            ('を', [('を', '助詞', '格助詞', 'を')]),
            ('あげ', [('あげ', '動詞', '自立', 'あげる')], PREDICATE),
            ('た', [('た', '助動詞', '*', 'た')]),
            ('。', [('。', '記号', '句点', '。')]),
        ],
    ),
    Spec(
        document='広島は蛎がうまい。',
        expected=[
            ('広島', [('広島', '名詞', '固有名詞', '広島')]),
            ('は', [('は', '助詞', '係助詞', 'は')]),
            ('蛎', [('蛎', '名詞', '一般', '蛎')]),
            ('が', [('が', '助詞', '格助詞', 'が')]),
            ('うまい', [('うまい', '形容詞', '自立', 'うまい')], PREDICATE),
            ('。', [('。', '記号', '句点', '。')]),
        ],
    ),
    Spec(
        document='この論文は一貫性がない。',
        expected=[
            ('この', [('この', '連体詞', '*', 'この')]),
            ('論文', [('論文', '名詞', '一般', '論文')]),
            ('は', [('は', '助詞', '係助詞', 'は')]),
            ('一貫性', [
                ('一貫', '名詞', 'サ変接続', '一貫'),
                ('性', '名詞', '接尾', '性'),
            ]),
            ('が', [('が', '助詞', '格助詞', 'が')]),
            ('ない', [('ない', '形容詞', '自立', 'ない')], PREDICATE),
            ('。', [('。', '記号', '句点', '。')]),
        ],
    ),
    Spec(
        document='A社は新型交換機を導入する。',
        expected=[
            ('A社', [
                ('A', '名詞', '一般', '*'),
                ('社', '名詞', '接尾', '社'),
            ]),
            ('は', [('は', '助詞', '係助詞', 'は')]),
            ('新型交換機', [
                ('新型', '名詞', '一般', '新型'),
                ('交換', '名詞', 'サ変接続', '交換'),
                ('機', '名詞', '接尾', '機'),
            ]),
            ('を', [('を', '助詞', '格助詞', 'を')]),
            ('導入する', [
                ('導入', '名詞', 'サ変接続', '導入'),
                ('する', '動詞', '自立', 'する'),
            ], PREDICATE),
            ('。', [('。', '記号', '句点', '。')]),
        ]
    ),
    Spec(
        document='一貫性のない論文。',
        expected=[
            ('一貫性', [
                ('一貫', '名詞', 'サ変接続', '一貫'),
                ('性', '名詞', '接尾', '性')
            ]),
            ('の', [('の', '助詞', '格助詞', 'の')]),
            ('ない', [('ない', '形容詞', '自立', 'ない')], PREDICATE),
            ('論文', [('論文', '名詞', '一般', '論文')]),
            ('。', [('。', '記号', '句点', '。')]),
        ],
    ),
    Spec(
        document='太郎が花子が好きだ。',
        expected=[
            ('太郎', [('太郎', '名詞', '固有名詞', '太郎')]),
            ('が', [('が', '助詞', '格助詞', 'が')]),
            ('花子', [('花子', '名詞', '固有名詞', '花子')]),
            ('が', [('が', '助詞', '格助詞', 'が')]),
            ('好き', [('好き', '名詞', '形容動詞語幹', '好き')], PREDICATE),
            ('だ', [('だ', '助動詞', '*', 'だ')]),
            ('。', [('。', '記号', '句点', '。')]),
        ],
    ),
    Spec(
        document='彼が勉強ができる。',
        expected=[
            ('彼', [('彼', '名詞', '代名詞', '彼')]),
            ('が', [('が', '助詞', '格助詞', 'が')]),
            ('勉強', [('勉強', '名詞', 'サ変接続', '勉強')]),
            ('が', [('が', '助詞', '格助詞', 'が')]),
            ('できる', [('できる', '動詞', '自立', 'できる')], PREDICATE),
            ('。', [('。', '記号', '句点', '。')]),
        ],
    ),
    Spec(
        document='花子が好きだ。',
        expected=[
            ('花子', [('花子', '名詞', '固有名詞', '花子')]),
            ('が', [('が', '助詞', '格助詞', 'が')]),
            ('好き', [('好き', '名詞', '形容動詞語幹', '好き')], PREDICATE),
            ('だ', [('だ', '助動詞', '*', 'だ')]),
            ('。', [('。', '記号', '句点', '。')]),
        ],
    ),
    Spec(
        document='中学校は四割、高校も三割あった。',
        expected=[
            ('中学校', [('中学校', '名詞', '一般', '中学校')]),
            ('は', [('は', '助詞', '係助詞', 'は')]),
            ('四割', [
                ('四', '名詞', '数', '四'),
                ('割', '名詞', '接尾', '割'),
            ]),
            ('、', [('、', '記号', '読点', '、')]),
            ('高校', [('高校', '名詞', '一般', '高校')]),
            ('も', [('も', '助詞', '係助詞', 'も')]),
            ('三割', [
                ('三', '名詞', '数', '三'),
                ('割', '名詞', '接尾', '割'),]),
            ('あっ', [('あっ', '動詞', '自立', 'ある')], PREDICATE),
            ('た', [('た', '助動詞', '*', 'た')]),
            ('。', [('。', '記号', '句点', '。')]),
        ],
    ),
    Spec(
        document='太郎はリンゴを，次郎はオレンジを食べた。',
        expected=[
            ('太郎', [('太郎', '名詞', '固有名詞', '太郎')]),
            ('は', [('は', '助詞', '係助詞', 'は')]),
            ('リンゴ', [('リンゴ', '名詞', '一般', 'リンゴ')]),
            ('を', [('を', '助詞', '格助詞', 'を')]),
            ('，', [('，', '記号', '読点', '，')]),
            ('次郎', [('次郎', '名詞', '固有名詞', '次郎')]),
            ('は', [('は', '助詞', '係助詞', 'は')]),
            ('オレンジ', [('オレンジ', '名詞', '一般', 'オレンジ')]),
            ('を', [('を', '助詞', '格助詞', 'を')]),
            ('食べ', [('食べ', '動詞', '自立', '食べる')], PREDICATE),
            ('た', [('た', '助動詞', '*', 'た')]),
            ('。', [('。', '記号', '句点', '。')]),
        ],
    ),
    Spec(
        document='太郎と次郎が帰ってきて遊んでいた。',
        expected=[
            ('太郎', [('太郎', '名詞', '固有名詞', '太郎')]),
            ('と', [('と', '助詞', '並立助詞', 'と')]),
            ('次郎', [('次郎', '名詞', '固有名詞', '次郎')]),
            ('が', [('が', '助詞', '格助詞', 'が')]),
            ('帰っ', [('帰っ', '動詞', '自立', '帰る')], PREDICATE),
            ('て', [('て', '助詞', '接続助詞', 'て')]),
            ('き', [('き', '動詞', '非自立', 'くる')], PREDICATE),
            ('て', [('て', '助詞', '接続助詞', 'て')]),
            ('遊ん', [('遊ん', '動詞', '自立', '遊ぶ')], PREDICATE),
            ('で', [('で', '助詞', '接続助詞', 'で')]),
            ('い', [('い', '動詞', '非自立', 'いる')], PREDICATE),
            ('た', [('た', '助動詞', '*', 'た')]),
            ('。', [('。', '記号', '句点', '。')]),
        ],
    ),
    Spec(
        document='太郎が花子と結婚した。',
        expected=[
            ('太郎', [('太郎', '名詞', '固有名詞', '太郎')]),
            ('が', [('が', '助詞', '格助詞', 'が')]),
            ('花子', [('花子', '名詞', '固有名詞', '花子')]),
            ('と', [('と', '助詞', '格助詞', 'と')]),
            ('結婚し', [
                ('結婚', '名詞', 'サ変接続', '結婚'),
                ('し', '動詞', '自立', 'する'),
            ], PREDICATE),
            ('た', [('た', '助動詞', '*', 'た')]),
            ('。', [('。', '記号', '句点', '。')]),
        ],
    ),
    Spec(
        document='バナナのほとんどを食べる。',
        expected=[
            ('バナナ', [('バナナ', '名詞', '一般', 'バナナ')]),
            ('の', [('の', '助詞', '連体化', 'の')]),
            ('ほとんど', [('ほとんど', '副詞', '一般', 'ほとんど')]),
            ('を', [('を', '助詞', '格助詞', 'を')]),
            ('食べる', [('食べる', '動詞', '自立', '食べる')], PREDICATE),
            ('。', [('。', '記号', '句点', '。')]),
        ],
    ),
    Spec(
        document='バナナをほとんど食べる。',
        expected=[
            ('バナナ', [('バナナ', '名詞', '一般', 'バナナ')]),
            ('を', [('を', '助詞', '格助詞', 'を')]),
            ('ほとんど', [('ほとんど', '副詞', '一般', 'ほとんど')]),
            ('食べる', [('食べる', '動詞', '自立', '食べる')], PREDICATE),
            ('。', [('。', '記号', '句点', '。')]),
        ],
    ),
    Spec(
        document='土曜日が休みになる。',
        expected=[
            ('土曜日', [('土曜日', '名詞', '副詞可能', '土曜日')]),
            ('が', [('が', '助詞', '格助詞', 'が')]),
            ('休み', [('休み', '名詞', '一般', '休み')]),
            ('に', [('に', '助詞', '格助詞', 'に')]),
            ('なる', [('なる', '動詞', '自立', 'なる')], PREDICATE),
            ('。', [('。', '記号', '句点', '。')]),
        ],
    ),
    Spec(
        document='本が彼に読まれる。',
        expected=[
            ('本', [('本', '名詞', '一般', '本')]),
            ('が', [('が', '助詞', '格助詞', 'が')]),
            ('彼', [('彼', '名詞', '代名詞', '彼')]),
            ('に', [('に', '助詞', '格助詞', 'に')]),
            ('読ま', [('読ま', '動詞', '自立', '読む')], PREDICATE),
            ('れる', [('れる', '動詞', '接尾', 'れる')], PREDICATE),
            ('。', [('。', '記号', '句点', '。')]),
        ],
    ),
    Spec(
        document='私は父に死なれた。',
        expected=[
            ('私', [('私', '名詞', '代名詞', '私')]),
            ('は', [('は', '助詞', '係助詞', 'は')]),
            ('父', [('父', '名詞', '一般', '父')]),
            ('に', [('に', '助詞', '格助詞', 'に')]),
            ('死な', [('死な', '動詞', '自立', '死ぬ')], PREDICATE),
            ('れ', [('れ', '動詞', '接尾', 'れる')], PREDICATE),
            ('た', [('た', '助動詞', '*', 'た')]),
            ('。', [('。', '記号', '句点', '。')]),
        ],
    ),
    Spec(
        document='私は彼にリンゴを食べさせる。',
        expected=[
            ('私', [('私', '名詞', '代名詞', '私')]),
            ('は', [('は', '助詞', '係助詞', 'は')]),
            ('彼', [('彼', '名詞', '代名詞', '彼')]),
            ('に', [('に', '助詞', '格助詞', 'に')]),
            ('リンゴ', [('リンゴ', '名詞', '一般', 'リンゴ')]),
            ('を', [('を', '助詞', '格助詞', 'を')]),
            ('食べ', [('食べ', '動詞', '自立', '食べる')], PREDICATE),
            ('させる', [('させる', '動詞', '接尾', 'させる')], PREDICATE),
            ('。', [('。', '記号', '句点', '。')]),
        ],
    ),
    Spec(
        document='私は彼にリンゴを食べてほしい。',
        expected=[
            ('私', [('私', '名詞', '代名詞', '私')]),
            ('は', [('は', '助詞', '係助詞', 'は')]),
            ('彼', [('彼', '名詞', '代名詞', '彼')]),
            ('に', [('に', '助詞', '格助詞', 'に')]),
            ('リンゴ', [('リンゴ', '名詞', '一般', 'リンゴ')]),
            ('を', [('を', '助詞', '格助詞', 'を')]),
            ('食べ', [('食べ', '動詞', '自立', '食べる')], PREDICATE),
            ('て', [('て', '助詞', '接続助詞', 'て')]),
            ('ほしい', [('ほしい', '形容詞', '非自立', 'ほしい')], PREDICATE),
            ('。', [('。', '記号', '句点', '。')]),
        ],
    ),
    Spec(
        document='避難所で暮らす人たちに疲労の色が濃い。',
        expected=[
            ('避難所', [
                ('避難', '名詞', 'サ変接続', '避難'),
                ('所', '名詞', '接尾', '所'),
            ]),
            ('で', [('で', '助詞', '格助詞', 'で')]),
            ('暮らす', [('暮らす', '動詞', '自立', '暮らす')], PREDICATE),
            ('人たち', [
                ('人', '名詞', '一般', '人'),
                ('たち', '名詞', '接尾', 'たち'),
            ]),
            ('に', [('に', '助詞', '格助詞', 'に')]),
            ('疲労', [('疲労', '名詞', 'サ変接続', '疲労')]),
            ('の', [('の', '助詞', '連体化', 'の')]),
            ('色', [('色', '名詞', '一般', '色')]),
            ('が', [('が', '助詞', '格助詞', 'が')]),
            ('濃い', [('濃い', '形容詞', '自立', '濃い')], PREDICATE),
            ('。', [('。', '記号', '句点', '。')]),
        ],
    ),
    Spec(
        skip=True,
        document='状況に即応した、きめの細かい住まいの対策が重要だ。',
        expected=[
            ('状況', [('状況', '名詞', '一般', '状況')]),
            ('に', [('に', '助詞', '格助詞', 'に')]),
            ('即応し', [
                ('即応', '名詞', 'サ変接続', '即応'),
                ('し', '動詞', '自立', 'する'),
            ], PREDICATE),
            ('た', [('た', '助動詞', '*', 'た')]),
            ('、', [('、', '記号', '読点', '、')]),
            # FIXME: 「きめ」は動詞じゃなくて名詞だ。
            ('きめ', [('きめ', '動詞', '自立', 'きめる')]),
            ('の', [('の', '助詞', '連体化', 'の')]),
            ('細かい', [('細かい', '形容詞', '自立', '細かい')], PREDICATE),
            ('住まい', [('住まい', '名詞', '一般', '住まい')]),
            ('の', [('の', '助詞', '連体化', 'の')]),
            ('対策', [('対策', '名詞', 'サ変接続', '対策')]),
            ('が', [('が', '助詞', '格助詞', 'が')]),
            ('重要', [('重要', '名詞', '形容動詞語幹', '重要')], PREDICATE),
            ('だ', [('だ', '助動詞', '*', 'だ')]),
            ('。', [('。', '記号', '句点', '。')]),
        ],
    ),
    Spec(
        document='応急仮設住宅を一日も早く、大量に提供したい。',
        expected=[
            ('応急仮設住宅', [
                ('応急', '名詞', '一般', '応急'),
                ('仮設', '名詞', 'サ変接続', '仮設'),
                ('住宅', '名詞', '一般', '住宅'),
            ]),
            ('を', [('を', '助詞', '格助詞', 'を')]),
            ('一日', [
                ('一', '名詞', '数', '一'),
                ('日', '名詞', '接尾', '日'),
            ]),
            ('も', [('も', '助詞', '係助詞', 'も')]),
            ('早く', [('早く', '形容詞', '自立', '早い')], PREDICATE),
            ('、', [('、', '記号', '読点', '、')]),
            ('大量', [('大量', '名詞', '形容動詞語幹', '大量')]),
            ('に', [('に', '助詞', '副詞化', 'に')]),
            ('提供し', [
                ('提供', '名詞', 'サ変接続', '提供'),
                ('し', '動詞', '自立', 'する'),
            ], PREDICATE),
            ('たい', [('たい', '助動詞', '*', 'たい')]),
            ('。', [('。', '記号', '句点', '。')]),
        ],
    ),
    Spec(
        document='私は彼に本を読んでもらう。',
        expected=[
            ('私', [('私', '名詞', '代名詞', '私')]),
            ('は', [('は', '助詞', '係助詞', 'は')]),
            ('彼', [('彼', '名詞', '代名詞', '彼')]),
            ('に', [('に', '助詞', '格助詞', 'に')]),
            ('本', [('本', '名詞', '一般', '本')]),
            ('を', [('を', '助詞', '格助詞', 'を')]),
            ('読ん', [('読ん', '動詞', '自立', '読む')], PREDICATE),
            ('で', [('で', '助詞', '接続助詞', 'で')]),
            ('もらう', [('もらう', '動詞', '非自立', 'もらう')], PREDICATE),
            ('。', [('。', '記号', '句点', '。')]),
        ],
    ),
    Spec(
        document='彼は私に本を読んでくれる。',
        expected=[
            ('彼', [('彼', '名詞', '代名詞', '彼')]),
            ('は', [('は', '助詞', '係助詞', 'は')]),
            ('私', [('私', '名詞', '代名詞', '私')]),
            ('に', [('に', '助詞', '格助詞', 'に')]),
            ('本', [('本', '名詞', '一般', '本')]),
            ('を', [('を', '助詞', '格助詞', 'を')]),
            ('読ん', [('読ん', '動詞', '自立', '読む')], PREDICATE),
            ('で', [('で', '助詞', '接続助詞', 'で')]),
            ('くれる', [('くれる', '動詞', '非自立', 'くれる')], PREDICATE),
            ('。', [('。', '記号', '句点', '。')]),
        ],
    ),
    Spec(
        document='私は彼に本を読んでやった。',
        expected=[
            ('私', [('私', '名詞', '代名詞', '私')]),
            ('は', [('は', '助詞', '係助詞', 'は')]),
            ('彼', [('彼', '名詞', '代名詞', '彼')]),
            ('に', [('に', '助詞', '格助詞', 'に')]),
            ('本', [('本', '名詞', '一般', '本')]),
            ('を', [('を', '助詞', '格助詞', 'を')]),
            ('読ん', [('読ん', '動詞', '自立', '読む')], PREDICATE),
            ('で', [('で', '助詞', '接続助詞', 'で')]),
            ('やっ', [('やっ', '動詞', '非自立', 'やる')], PREDICATE),
            ('た', [('た', '助動詞', '*', 'た')]),
            ('。', [('。', '記号', '句点', '。')]),
        ],
    ),
    Spec(
        document='本が置いてある。',
        expected=[
            ('本', [('本', '名詞', '一般', '本')]),
            ('が', [('が', '助詞', '格助詞', 'が')]),
            ('置いてある', [
                ('置い', '動詞', '自立', '置く'),
                ('て', '助詞', '接続助詞', 'て'),
                ('ある', '動詞', '非自立', 'ある')
            ], PREDICATE),
            ('。', [('。', '記号', '句点', '。')]),
        ],
    ),
    Spec(
        skip=True,
        document='企業に於ける文化事業のむずかしさを考えさせられた。',
        expected=[
            ('企業', [('企業', '名詞', '一般', '企業')]),
            ('に於ける', [('に於ける', 'その他', '機能語', 'に於ける')]),
            ('文化事業', [
                ('文化', '名詞', '一般', '文化'),
                ('事業', [('事業', '名詞', '一般', '事業')]),
            ]),
            ('の', [('の', '助詞', '連体化', 'の')]),
            # TODO: ここは名詞にしたい…
            ('むずかしさ', [
                ('むずかし', '形容詞', '自立', 'むずかしい'),
                ('さ', '名詞', '接尾', 'さ'),
            ]),
            ('を', [('を', '助詞', '格助詞', 'を')]),
            ('考え', [('考え', '動詞', '自立', '考える')], PREDICATE),
            ('させ', [('させ', '動詞', '接尾', 'させる')], PREDICATE),
            ('られ', [('られ', '動詞', '接尾', 'られる')], PREDICATE),
            ('た', [('た', '助動詞', '*', 'た')]),
            ('。', [('。', '記号', '句点', '。')]),
        ],
    ),
    Spec(
        document='彼にはこの計画を実現させてほしい。',
        expected=[
            ('彼', [('彼', '名詞', '代名詞', '彼')]),
            ('に', [('に', '助詞', '格助詞', 'に')]),
            ('は', [('は', '助詞', '係助詞', 'は')]),
            ('この', [('この', '連体詞', '*', 'この')]),
            ('計画', [('計画', '名詞', 'サ変接続', '計画')]),
            ('を', [('を', '助詞', '格助詞', 'を')]),
            ('実現さ', [
                ('実現', '名詞', 'サ変接続', '実現'),
                ('さ', '動詞', '自立', 'する'),
            ], PREDICATE),
            ('せ', [('せ', '動詞', '接尾', 'せる')], PREDICATE),
            ('て', [('て', '助詞', '接続助詞', 'て')]),
            ('ほしい', [('ほしい', '形容詞', '非自立', 'ほしい')], PREDICATE),
            ('。', [('。', '記号', '句点', '。')]),
        ],
    ),
    Spec(
        skip=True,
        document='自己診断機能を搭載、200システムを設置する。',
        expected=[
            ('自己診断機能', [
                ('自己', '名詞', '一般', '自己'),
                ('診断', '名詞', 'サ変接続', '診断'),
                ('機能', '名詞', 'サ変接続', '機能'),
            ]),
            ('を', [('を', '助詞', '格助詞', 'を')]),
            # TODO: ここを述語にしたい、サ変名詞 + 読点で特別扱いする？？
            ('搭載', [('搭載', '名詞', 'サ変接続', '搭載')], PREDICATE),
            ('、', [('、', '記号', '読点', '、')]),
            ('200システム', [
                ('200', '名詞', '数', '*'),
                ('システム', '名詞', '一般', 'システム'),
            ]),
            ('を', [('を', '助詞', '格助詞', 'を')]),
            ('設置する', [
                ('設置', '名詞', 'サ変接続', '設置'),
                ('する', '動詞', '自立', 'する'),
            ], PREDICATE),
            ('。', [('。', '記号', '句点', '。')]),
        ],
    ),
    Spec(
        document='蛎を食べるため、太郎は広島へ行った。',
        expected=[
            ('蛎', [('蛎', '名詞', '一般', '蛎')]),
            ('を', [('を', '助詞', '格助詞', 'を')]),
            ('食べる', [('食べる', '動詞', '自立', '食べる')], PREDICATE),
            ('ため', [('ため', '名詞', '非自立', 'ため')]),
            ('、', [('、', '記号', '読点', '、')]),
            ('太郎', [('太郎', '名詞', '固有名詞', '太郎')]),
            ('は', [('は', '助詞', '係助詞', 'は')]),
            ('広島', [('広島', '名詞', '固有名詞', '広島')]),
            ('へ', [('へ', '助詞', '格助詞', 'へ')]),
            ('行っ', [('行っ', '動詞', '自立', '行く')], PREDICATE),
            ('た', [('た', '助動詞', '*', 'た')]),
            ('。', [('。', '記号', '句点', '。')]),
        ],
    ),
    Spec(
        document='独身男性が部屋で死亡していた。',
        expected=[
            ('独身男性', [
                ('独身', '名詞', '一般', '独身'),
                ('男性', '名詞', '一般', '男性'),
            ]),
            ('が', [('が', '助詞', '格助詞', 'が')]),
            ('部屋', [('部屋', '名詞', '一般', '部屋')]),
            ('で', [('で', '助詞', '格助詞', 'で')]),
            ('死亡し', [
                ('死亡', '名詞', 'サ変接続', '死亡'),
                ('し', '動詞', '自立', 'する'),
            ], PREDICATE),
            ('て', [('て', '助詞', '接続助詞', 'て')]),
            ('い', [('い', '動詞', '非自立', 'いる')], PREDICATE),
            ('た', [('た', '助動詞', '*', 'た')]),
            ('。', [('。', '記号', '句点', '。')]),
        ],
    ),
    Spec(
        document='彼の友人が発見して通報した。',
        expected=[
            ('彼', [('彼', '名詞', '代名詞', '彼')]),
            ('の', [('の', '助詞', '連体化', 'の')]),
            ('友人', [('友人', '名詞', '一般', '友人')]),
            ('が', [('が', '助詞', '格助詞', 'が')]),
            ('発見し', [
                ('発見', '名詞', 'サ変接続', '発見'),
                ('し', '動詞', '自立', 'する'),
            ], PREDICATE),
            ('て', [('て', '助詞', '接続助詞', 'て')]),
            ('通報し', [
                ('通報', '名詞', 'サ変接続', '通報'),
                ('し', '動詞', '自立', 'する'),
            ], PREDICATE),
            ('た', [('た', '助動詞', '*', 'た')]),
            ('。', [('。', '記号', '句点', '。')]),
        ],
    ),
    Spec(
        document='太郎が学校から帰ってきた。',
        expected=[
            ('太郎', [('太郎', '名詞', '固有名詞', '太郎')]),
            ('が', [('が', '助詞', '格助詞', 'が')]),
            ('学校', [('学校', '名詞', '一般', '学校')]),
            ('から', [('から', '助詞', '格助詞', 'から')]),
            ('帰っ', [('帰っ', '動詞', '自立', '帰る')], PREDICATE),
            ('て', [('て', '助詞', '接続助詞', 'て')]),
            ('き', [('き', '動詞', '非自立', 'くる')], PREDICATE),
            ('た', [('た', '助動詞', '*', 'た')]),
            ('。', [('。', '記号', '句点', '。')]),
        ],
    ),
    Spec(
        document='しかし、彼はすぐに公園に出かけてしまった。',
        expected=[
            ('しかし', [('しかし', '接続詞', '*', 'しかし')]),
            ('、', [('、', '記号', '読点', '、')]),
            ('彼', [('彼', '名詞', '代名詞', '彼')]),
            ('は', [('は', '助詞', '係助詞', 'は')]),
            ('すぐ', [('すぐ', '副詞', '助詞類接続', 'すぐ')]),
            ('に', [('に', '助詞', '副詞化', 'に')]),
            ('公園', [('公園', '名詞', '一般', '公園')]),
            ('に', [('に', '助詞', '格助詞', 'に')]),
            ('出かけ', [('出かけ', '動詞', '自立', '出かける')], PREDICATE),
            ('て', [('て', '助詞', '接続助詞', 'て')]),
            ('しまっ', [('しまっ', '動詞', '非自立', 'しまう')], PREDICATE),
            ('た', [('た', '助動詞', '*', 'た')]),
            ('。', [('。', '記号', '句点', '。')]),
        ],
    ),
    Spec(
        violate_naist_rule=(
            '仕様書によると「いない」で述語になっているが、ここは「い」で述語とする'
            '理由は、なんで仕様書が「いない」で述語にしているか分からないため…'
        ),
        document='彼には友達なんていないはずなのに。',
        expected=[
            ('彼', [('彼', '名詞', '代名詞', '彼')]),
            ('に', [('に', '助詞', '格助詞', 'に')]),
            ('は', [('は', '助詞', '係助詞', 'は')]),
            ('友達', [('友達', '名詞', '一般', '友達')]),
            ('なんて', [('なんて', '助詞', '副助詞', 'なんて')]),
            ('い', [('い', '動詞', '自立', 'いる')], PREDICATE),
            ('ない', [('ない', '助動詞', '*', 'ない')]),
            ('はず', [('はず', '名詞', '非自立', 'はず')]),
            ('な', [('な', '助動詞', '*', 'だ')]),
            ('のに', [('のに', '助詞', '接続助詞', 'のに')]),
            ('。', [('。', '記号', '句点', '。')]),
        ],
    ),
    Spec(
        # TODO: 事態を表す名詞(「釈放」)に対応する
        skip=True,
        document='Ａ政府は捕虜釈放を呼びかけた。',
        expected=[
            ('Ａ政府', [
                ('Ａ', '記号', 'アルファベット', 'Ａ'),
                ('政府', '名詞', '一般', '政府'),
            ]),
            ('は', [('は', '助詞', '係助詞', 'は')]),
            ('捕虜', [('捕虜', '名詞', '一般', '捕虜')]),
            ('釈放', [('釈放', '名詞', 'サ変接続', '釈放')]),
            ('を', [('を', '助詞', '格助詞', 'を')]),
            ('呼びかけ', [('呼びかけ', '動詞', '自立', '呼びかける')]),
            ('た', [('た', '助動詞', '*', 'た')]),
            ('。', [('。', '記号', '句点', '。')]),
        ],
    ),
    Spec(
        document='それに対して、Ｂ政府は捕虜の解放を保証した。',
        expected=[
            ('それ', [('それ', '名詞', '代名詞', 'それ')]),
            ('に対して', [('に対して', '助詞', '格助詞', 'に対して')]),
            ('、', [('、', '記号', '読点', '、')]),
            ('Ｂ政府', [
                ('Ｂ', '記号', 'アルファベット', 'Ｂ'),
                ('政府', '名詞', '一般', '政府'),
            ]),
            ('は', [('は', '助詞', '係助詞', 'は')]),
            ('捕虜', [('捕虜', '名詞', '一般', '捕虜')]),
            ('の', [('の', '助詞', '連体化', 'の')]),
            ('解放', [('解放', '名詞', 'サ変接続', '解放')]),
            ('を', [('を', '助詞', '格助詞', 'を')]),
            ('保証し', [
                ('保証', '名詞', 'サ変接続', '保証'),
                ('し', '動詞', '自立', 'する'),
            ], PREDICATE),
            ('た', [('た', '助動詞', '*', 'た')]),
            ('。', [('。', '記号', '句点', '。')]),
        ],
    ),
    Spec(
        document='図書館では本を借りることができる。',
        expected=[
            ('図書館', [('図書館', '名詞', '一般', '図書館')]),
            ('で', [('で', '助詞', '格助詞', 'で')]),
            ('は', [('は', '助詞', '係助詞', 'は')]),
            ('本', [('本', '名詞', '一般', '本')]),
            ('を', [('を', '助詞', '格助詞', 'を')]),
            ('借りる', [('借りる', '動詞', '自立', '借りる')], PREDICATE),
            ('こと', [('こと', '名詞', '非自立', 'こと')]),
            ('が', [('が', '助詞', '格助詞', 'が')]),
            ('できる', [('できる', '動詞', '自立', 'できる')], PREDICATE),
            ('。', [('。', '記号', '句点', '。')]),
        ],
    ),
    Spec(
        document='しかし、図書館に置いてある本は汚れている。',
        expected=[
            ('しかし', [('しかし', '接続詞', '*', 'しかし')]),
            ('、', [('、', '記号', '読点', '、')]),
            ('図書館', [('図書館', '名詞', '一般', '図書館')]),
            ('に', [('に', '助詞', '格助詞', 'に')]),
            ('置いてある', [
                ('置い', '動詞', '自立', '置く'),
                ('て', '助詞', '接続助詞', 'て'),
                ('ある', '動詞', '非自立', 'ある'),
            ], PREDICATE),
            ('本', [('本', '名詞', '一般', '本')]),
            ('は', [('は', '助詞', '係助詞', 'は')]),
            ('汚れ', [('汚れ', '動詞', '自立', '汚れる')], PREDICATE),
            ('て', [('て', '助詞', '接続助詞', 'て')]),
            ('いる', [('いる', '動詞', '非自立', 'いる')], PREDICATE),
            ('。', [('。', '記号', '句点', '。')]),
        ],
    ),
    Spec(
        document='太郎が花子に会った。',
        expected=[
            ('太郎', [('太郎', '名詞', '固有名詞', '太郎')]),
            ('が', [('が', '助詞', '格助詞', 'が')]),
            ('花子', [('花子', '名詞', '固有名詞', '花子')]),
            ('に', [('に', '助詞', '格助詞', 'に')]),
            ('会っ', [('会っ', '動詞', '自立', '会う')], PREDICATE),
            ('た', [('た', '助動詞', '*', 'た')]),
            ('。', [('。', '記号', '句点', '。')]),
        ],
    ),
    Spec(
        # TODO: 「帰ってき」の複合動詞とするか検討する
        # 仕様書に従うならば複合動詞となる、そうすると「帰っていらっしゃる」や「歩いていらっしゃる」は？
        # これらを別個に扱う方が色々と煩雑になってしまう…
        # また、前例の「太郎が学校から帰ってきた。」と仕様書内で矛盾している
        skip=True,
        document='太郎と次郎が学校から帰ってきた。',
        expected=[
            ('太郎', [('太郎', '名詞', '固有名詞', '太郎')]),
            ('と', [('と', '助詞', '並立助詞', 'と')]),
            ('次郎', [('次郎', '名詞', '固有名詞', '次郎')]),
            ('が', [('が', '助詞', '格助詞', 'が')]),
            ('学校', [('学校', '名詞', '一般', '学校')]),
            ('から', [('から', '助詞', '格助詞', 'から')]),
            ('帰ってき', [
                ('帰っ', '動詞', '自立', '帰る'),
                ('て', '助詞', '接続助詞', 'て'),
                ('き', '動詞', '非自立', 'くる'),], PREDICATE),
            ('た', [('た', '助動詞', '*', 'た')]),
            ('。', [('。', '記号', '句点', '。')]),
        ],
    ),
    Spec(
        document='二人はすぐに出かけた。',
        expected=[
            ('二人', [
                ('二', '名詞', '数', '二'),
                ('人', '名詞', '接尾', '人'),
            ]),
            ('は', [('は', '助詞', '係助詞', 'は')]),
            ('すぐ', [('すぐ', '副詞', '助詞類接続', 'すぐ')]),
            ('に', [('に', '助詞', '副詞化', 'に')]),
            ('出かけ', [('出かけ', '動詞', '自立', '出かける')], PREDICATE),
            ('た', [('た', '助動詞', '*', 'た')]),
            ('。', [('。', '記号', '句点', '。')]),
        ],
    ),
    Spec(
        document='太郎は蛎を買った。',
        expected=[
            ('太郎', [('太郎', '名詞', '固有名詞', '太郎')]),
            ('は', [('は', '助詞', '係助詞', 'は')]),
            ('蛎', [('蛎', '名詞', '一般', '蛎')]),
            ('を', [('を', '助詞', '格助詞', 'を')]),
            ('買っ', [('買っ', '動詞', '自立', '買う')], PREDICATE),
            ('た', [('た', '助動詞', '*', 'た')]),
            ('。', [('。', '記号', '句点', '。')]),
        ],
    ),
    Spec(
        violate_naist_rule=(
            '仕様書だと「国産だっ」が述語となっているけれどここは「国産」にタグを付与する',
            '理由は「名詞句+助動詞("だ")」の「名詞句」というルールに従いたいため'
        ),
        document='ほとんどが国産だった。',
        expected=[
            ('ほとんど', [('ほとんど', '副詞', '一般', 'ほとんど')]),
            ('が', [('が', '助詞', '格助詞', 'が')]),
            ('国産', [('国産', '名詞', '一般', '国産')], PREDICATE),
            ('だっ', [('だっ', '助動詞', '*', 'だ')]),
            ('た', [('た', '助動詞', '*', 'た')]),
            ('。', [('。', '記号', '句点', '。')]),
        ],
    ),
    Spec(
        document='サンマを焼く男。',
        expected=[
            ('サンマ', [('サンマ', '名詞', '一般', 'サンマ')]),
            ('を', [('を', '助詞', '格助詞', 'を')]),
            ('焼く', [('焼く', '動詞', '自立', '焼く')], PREDICATE),
            ('男', [('男', '名詞', '一般', '男')]),
            ('。', [('。', '記号', '句点', '。')]),
        ],
    ),
    Spec(
        document='お母さんが怪我した子ども。',
        expected=[
            ('お母さん', [('お母さん', '名詞', '一般', 'お母さん')]),
            ('が', [('が', '助詞', '格助詞', 'が')]),
            ('怪我し', [
                ('怪我', '名詞', 'サ変接続', '怪我'),
                ('し', '動詞', '自立', 'する'),
            ], PREDICATE),
            ('た', [('た', '助動詞', '*', 'た')]),
            ('子ども', [('子ども', '名詞', '一般', '子ども')]),
            ('。', [('。', '記号', '句点', '。')]),
        ],
    ),
    Spec(
        document='サンマを焼くにおい。',
        expected=[
            ('サンマ', [('サンマ', '名詞', '一般', 'サンマ')]),
            ('を', [('を', '助詞', '格助詞', 'を')]),
            ('焼く', [('焼く', '動詞', '自立', '焼く')], PREDICATE),
            ('におい', [('におい', '名詞', '一般', 'におい')]),
            ('。', [('。', '記号', '句点', '。')]),
        ],
    ),
    Spec(
        document='おなかが減ったので帰ろうと思う。',
        expected=[
            ('おなか', [('おなか', '名詞', '一般', 'おなか')]),
            ('が', [('が', '助詞', '格助詞', 'が')]),
            ('減っ', [('減っ', '動詞', '自立', '減る')], PREDICATE),
            ('た', [('た', '助動詞', '*', 'た')]),
            ('ので', [('ので', '助詞', '接続助詞', 'ので')]),
            ('帰ろ', [('帰ろ', '動詞', '自立', '帰る')], PREDICATE),
            ('う', [('う', '助動詞', '*', 'う')]),
            ('と', [('と', '助詞', '格助詞', 'と')]),
            ('思う', [('思う', '動詞', '自立', '思う')], PREDICATE),
            ('。', [('。', '記号', '句点', '。')]),
        ],
    ),
    Spec(
        skip=True,
        document='さしずめ政党は政治を限りなくつまらなくするための談合組織といえる。',
        expected=[
            ('さしずめ', [('さしずめ', '副詞', '一般', 'さしずめ')]),
            ('政党', [('政党', '名詞', '一般', '政党')]),
            ('は', [('は', '助詞', '係助詞', 'は')]),
            ('政治', [('政治', '名詞', '一般', '政治')]),
            ('を', [('を', '助詞', '格助詞', 'を')]),
            ('限り', [('限り', '名詞', 'ナイ形容詞語幹', '限り')]),
            ('なく', [('なく', '助動詞', '*', 'ない')]),
            # TODO: 対応を考える
            # 格交替の使役と考えると、「すまらなく」と「する」それぞれにタグが必要になるのでは？
            # だけど「述語+てある」と似ていて、「つまらなくする」に「政党が」と「政治を」
            # の格関係をタグ付けしたいかもしれない…
            ('つまらなくする', [
                ('つまらなく', '形容詞', '自立', 'つまらない'),
                ('する', '動詞', '自立', 'する'),
            ], PREDICATE),
            ('ため', [('ため', '名詞', '非自立', 'ため')]),
            ('の', [('の', '助詞', '連体化', 'の')]),
            ('談合組織', [
                ('談合', '名詞', 'サ変接続', '談合'),
                ('組織', '名詞', 'サ変接続', '組織'),
            ]),
            ('と', [('と', '助詞', '格助詞', 'と')]),
            ('いえる', [('いえる', '動詞', '自立', 'いえる')], PREDICATE),
            ('。', [('。', '記号', '句点', '。')]),
        ],
    ),
    Spec(
        violate_naist_rule=(
            '仕様書だと「寝た」が述語となっているけれどここは MeCab の「寝」',
            'が正しい気がする？'
        ),
        document='もう帰って寝たらどうですか。',
        expected=[
            ('もう', [('もう', '副詞', '一般', 'もう')]),
            ('帰っ', [('帰っ', '動詞', '自立', '帰る')], PREDICATE),
            ('て', [('て', '助詞', '接続助詞', 'て')]),
            ('寝', [('寝', '動詞', '自立', '寝る')], PREDICATE),
            ('たら', [('たら', '助動詞', '*', 'た')]),
            ('どう', [('どう', '副詞', '助詞類接続', 'どう')]),
            ('です', [('です', '助動詞', '*', 'です')]),
            ('か', [('か', '助詞', '副助詞／並立助詞／終助詞', 'か')]),
            ('。', [('。', '記号', '句点', '。')]),
        ],
    ),
    Spec(
        document='もう二十日近くになる。',
        expected=[
            ('もう', [('もう', '副詞', '一般', 'もう')]),
            ('二十日近く', [
                ('二', '名詞', '数', '二'),
                ('十', '名詞', '数', '十'),
                ('日', '名詞', '接尾', '日'),
                ('近く', '名詞', '副詞可能', '近く'),
            ]),
            ('に', [('に', '助詞', '格助詞', 'に')]),
            ('なる', [('なる', '動詞', '自立', 'なる')], PREDICATE),
            ('。', [('。', '記号', '句点', '。')]),
        ],
    ),
    Spec(
        document='もうそろそろ円安に転じるといわれて、ずいぶん時がたった。',
        expected=[
            ('もう', [('もう', '副詞', '一般', 'もう')]),
            ('そろそろ', [('そろそろ', '副詞', '助詞類接続', 'そろそろ')]),
            ('円安', [
                ('円', '名詞', '一般', '円'),
                ('安', '名詞', '接尾', '安'),
            ]),
            ('に', [('に', '助詞', '格助詞', 'に')]),
            ('転じる', [('転じる', '動詞', '自立', '転じる')], PREDICATE),
            ('と', [('と', '助詞', '格助詞', 'と')]),
            ('いわ', [('いわ', '動詞', '自立', 'いう')], PREDICATE),
            ('れ', [('れ', '動詞', '接尾', 'れる')], PREDICATE),
            ('て', [('て', '助詞', '接続助詞', 'て')]),
            ('、', [('、', '記号', '読点', '、')]),
            ('ずいぶん', [('ずいぶん', '副詞', '助詞類接続', 'ずいぶん')]),
            ('時', [('時', '名詞', '接尾', '時')]),
            ('が', [('が', '助詞', '格助詞', 'が')]),
            ('たっ', [('たっ', '動詞', '自立', 'たつ')], PREDICATE),
            ('た', [('た', '助動詞', '*', 'た')]),
            ('。', [('。', '記号', '句点', '。')]),
        ],
    ),
]


def expected_output(expected_spec):
    return [
        PASUnit(
            text=text, unit=unit[0],
            morphemes=[Morpheme._make(m) for m in morphemes])
        if len(unit) > 0 else
        PASUnit(
            text=text,
            morphemes=[Morpheme._make(m) for m in morphemes])
        for text, morphemes, *unit in expected_spec]
