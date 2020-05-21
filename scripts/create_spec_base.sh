# pasnominator.tests.integrations.spec の Spec の雛形を作るための横着スクリプト
# このスクリプトの出力を調整して Spec としてコピー & ペーストする。
#
# 例
#   以下の例では、「一貫性のない論文。」については出力結果を手で補正して、「一貫」+「性」を
#   「一貫性」とする必要がある。
#   https://sites.google.com/site/naisttextcorpus/ntc-annotation-scheme
#
#     $ cat work_tajima/naist_sample.txt
#     一貫性のない論文。
#     太郎が花子が好きだ。
#     彼が勉強ができる。
#
#     $ for doc in $(cat work_tajima/naist_sample.txt); do
#     > ./scripts/create_spec_base.sh $doc
#     > done
#         Spec(
#             document='一貫性のない論文。',
#             expected=[
#                 ('一貫', [('一貫', '名詞', 'サ変接続', '一貫')]),
#                 ('性', [('性', '名詞', '接尾', '性')]),
#                 ('の', [('の', '助詞', '格助詞', 'の')]),
#                 ('ない', [('ない', '形容詞', '自立', 'ない')]),
#                 ('論文', [('論文', '名詞', '一般', '論文')]),
#                 ('。', [('。', '記号', '句点', '。')]),
#             ],
#         ),
#         Spec(
#             document='太郎が花子が好きだ。',
#             expected=[
#                 ('太郎', [('太郎', '名詞', '固有名詞', '太郎')]),
#                 ('が', [('が', '助詞', '格助詞', 'が')]),
#                 ('花子', [('花子', '名詞', '固有名詞', '花子')]),
#                 ('が', [('が', '助詞', '格助詞', 'が')]),
#                 ('好き', [('好き', '名詞', '形容動詞語幹', '好き')]),
#                 ('だ', [('だ', '助動詞', '*', 'だ')]),
#                 ('。', [('。', '記号', '句点', '。')]),
#             ],
#         ),
#         Spec(
#             document='彼が勉強ができる。',
#             expected=[
#                 ('彼', [('彼', '名詞', '代名詞', '彼')]),
#                 ('が', [('が', '助詞', '格助詞', 'が')]),
#                 ('勉強', [('勉強', '名詞', 'サ変接続', '勉強')]),
#                 ('が', [('が', '助詞', '格助詞', 'が')]),
#                 ('できる', [('できる', '動詞', '自立', 'できる')]),
#                 ('。', [('。', '記号', '句点', '。')]),
#             ],
#         ),

TEXT=$(echo $1 | sed -e 's/ //g')

cat <<EOS
    Spec(
        document='$TEXT',
        expected=[
EOS

PREV_IFS=$IFS
IFS="
"
for line in $(echo $TEXT | mecab | grep -v 'BOS' | grep -v 'EOS'); do
    IFS=$PREV_IFS

    SURFACE=$(echo $line | cut -f1 -d ' ')
    FEATURES=$(echo $line | cut -f2 -d ' '\
        | awk -F ',' '{print "'\''" $1 "'\'', '\''" $2 "'\'', '\''" $7 "'\''"}')

    cat <<EOS
            ('${SURFACE}', [('${SURFACE}', ${FEATURES})]),
EOS
done

cat <<EOS
        ],
    ),
EOS
