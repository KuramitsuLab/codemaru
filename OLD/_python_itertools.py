import operator
# itertools

import itertools
'''
itertoolsモジュールをインポートしたい
'''

# 設定
__要素__ = 10  # [文字列]
_整数_ = 2
__イテレータ__ = [1, 2]
'''
@poly(__要素__;_整数_;_文字列_)
@poly(__イテレータ__;_イテレータ_;_リスト_;_配列_)
'''

itertools.repeat(_整数_)
'''
@alt(数列|[|整数]リスト)

_整数_の無限[|な|の]数列が欲しい
_整数_が無限に続く数列が欲しい
'''

itertools.repeat(__要素__)
'''
@alt(イテラブル|列|イテレータ)
@alt(無限に|いつまでも)
{__要素__が|無限に}[繰り返す|続く]イテラブルが欲しい
__要素__の無限[|な|の]イテラブルが欲しい
'''

itertools.repeat(__要素__, _整数_)
'''
{__要素__[が|を]|_整数_回}[繰り返す|続く]イテラブルが欲しい
'''

itertools.count()
'''
@alt(カウントアップしたい|数え上げたい)
無限にカウントアップしたい
[０から始まる|]無限[|な|の]数列が欲しい
'''

itertools.count(start=_整数_, step=1)
'''
_整数_から始まる無限[|な|の]数列が欲しい
'''

itertools.count(start=_整数_, step=-1)
'''
{_整数_から|無限に}カウントダウンしたい
'''

itertools.cycle(__イテレータ__)
'''
@alt(周期的に|循環的に|サイクリックに|ぐるぐると|何度も|無限に)

{__イテレータ__を|周期的に}結合したい
'''

for x in itertools.cycle(__イテレータ__):
    print(x)
'''
{__イテレータ__[の要素|]を|周期的に}繰り返したい
'''

itertools.accumulate(__イテレータ__)
'''
__イテレータ__を累加したい
__イテレータ__を累加したイテレータが欲しい
'''

itertools.accumulate(__イテレータ__, operator.mul)
'''
__イテレータ__を累積したい
__イテレータ__を__関数__で累積したイテレータが欲しい
'''

itertools.chain(__イテレータ__, __イテレータ__)
'''
__イテレータ__と__イテレータ__を[連結したい|つなぎたい|チェインしたい]
__イテレータ__に__イテレータ__を続けたい
__イテレータ__に__イテレータ__を続けた__イテレータ__が欲しい
'''

itertools.compress(__イテレータ__, selectors=__イテレータ__)
'''
__イテレータ__[の要素|]をマスクしたい
__イテレータ__でマスクされた__イテレータ__が欲しい
'''


def _関数_(x): return True


itertools.takewhile(_関数_, __イテレータ__)
'''
__イテレータ__[の要素|]を_関数_で[残したい|選びたい]
'''

itertools.dropwhile(_関数_, __イテレータ__)
'''
__イテレータ__[の要素|]を_関数_で[消したい|除去したい]
'''

itertools.zip_longest(__イテレータ__, __イテレータ__)
'''
@alt(ペアリングしたい|ペア化したい|[zip|ジップ]したい)
__イテレータ__と__イテレータ__をペアリングしたい
[不揃いな長さの|長さが一致しない[とき|バージョン]]のzip
'''

itertools.product(__イテレータ__, __イテレータ__)
'''
@alt(直積|デカルト積|全要素の[組み合わせ|ペア])
__イテレータ__と__イテレータ__の直積が欲しい
'''

list(itertools.product(__イテレータ__, __イテレータ__))
'''
__イテレータ__と__イテレータ__の直積がリストとして欲しい
'''

itertools.product(__イテレータ__, repeat=2)
'''
同じ__イテレータ__[|自身]の直積が欲しい
'''

for x, y in itertools(range(0, _整数_), range(0, _整数_)):
    print(x, y)
'''
二重ループを[シングル|単一]ループで書きたい
'''

list(itertools.product(range(_整数_), range(_整数_)))
'''
{_整数_と_整数_の全[組み合わせ|ペア]が|リストとして}欲しい
'''


itertools.permutations(__イテレータ__)
'''
__イテレータ__の全順列が欲しい
'''

itertools.permutations(__イテレータ__, _整数_)
'''
__イテレータ__[|自身]の長さ_整数_の順列が欲しい
'''

list(itertools.permutations(__イテレータ__))
'''
__イテレータ__の全順列をリストにしたい
'''

list(itertools.permutations(__イテレータ__, _整数_))
'''
__イテレータ__[|自身]の長さ_整数_の順列をリストにしたい
'''

# コンビネーション

itertools.combinations(__イテレータ__, 2)
'''
@alt(コンビネーション|組み合わせ)
__イテレータ__のコンビネーションが欲しい
'''

itertools.combinations_with_replacement(__イテレータ__, 2)
'''
__イテレータ__の重複コンビネーションが欲しい
'''

list(itertools.combinations(__イテレータ__, 2))
'''
@alt(コンビネーション|組み合わせ)
__イテレータ__のコンビネーション[をリストにしたい|リスト[で|として]欲しい]
'''

list(itertools.combinations_with_replacement(__イテレータ__, 2))
'''
__イテレータ__の重複コンビネーション[をリストにしたい|リスト[で|として]欲しい]
'''


itertools.combinations(__イテレータ__, _整数_)
'''
__イテレータ__の長さ_整数_のコンビネーションが欲しい
'''

itertools.combinations_with_replacement(__イテレータ__, _整数_)
'''
__イテレータ__の長さ_整数_の重複コンビネーションが欲しい
'''

for x, y in itertools.combinations(__イテレータ__, 2):
    print(x, y)
'''
__イテレータ__のコンビネーションを繰り返したい
'''

for x, y in itertools.combinations_with_replacement(__イテレータ__, 2):
    print(x, y)
'''
__イテレータ__の重複コンビネーションを繰り返したい
'''

for pairs in itertools.combinations(__イテレータ__, _整数_):
    print(pairs)
'''
__イテレータ__の長さ_整数_のコンビネーションを繰り返したい
'''

for pairs in itertools.combinations_with_replacement(__イテレータ__, _整数_):
    print(pairs)
'''
__イテレータ__の長さ_整数_の重複コンビネーションを繰り返したい
'''
