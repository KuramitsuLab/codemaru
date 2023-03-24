import pandas as pd

_データフレーム_ = pd.DataFrame(
    data=[[1, 2, 3], [4, 5, 6]], columns=['列A', '列B', '列C'])

_列名_ = 'A'


def func(x): return '列A'


関数 = func

# グループ化


_データフレーム_.groupby(グループ化したいカテゴリのある列名)
'''
@alt(グループ化したい|集[約|計]したい|分類したい])

_データフレーム_をグループ化したい
'''

_データフレーム_.groupby(by=_列名_)
'''
@alt(ごと|毎|)
@alt(それぞれの|各|)

_列名_のカテゴリごとにグループ化したい
{_データフレーム_を|_列名_[の値|のカテゴリ|][によって|で]}グループ化したい
'''

_データフレーム_.groupby(by=[_列名_, _列名_])
'''
{[_データフレーム_を|_列名_と_列名_][によって|で]}グループ化したい
{_データフレーム_を|[二つの|複数の]_列名_[によって|で]}グループ化したい
'''

_データフレーム_.groupby(_列名_, dropna=False)
'''
{[_データフレーム_|_列名_]を|欠損値を[含めて|省略せずに]}グループ化したい
'''

_データフレーム_.groupby(by=関数)
'''
{_データフレーム_を|関数適用[によって|で]}グループ化したい
'''

_データフレーム_.groupby(_列名_).describe()
'''
@alt(要約統計量|記述統計量|[|基本]統計量)

_列名_のカテゴリごとの要約統計量が欲しい
{_データフレーム_を|_列名_[の値|][によって|で]}グループ化し、要約統計量を求めたい
'''

dropna = True
'''
option: 欠損値[は無視したい|を含めない]
'''

dropna = False
'''
option: 欠損値[も無視しない|[も|を]含める]
'''

[(name, group__データフレーム_) for name, group__データフレーム_ in _データフレーム_.groupby(_列名_)]
'''
{_データフレーム_を|_列名_[の値|][によって|ごとに|で]}グループ化して、列挙したい
'''

[name for name, _ in _データフレーム_.groupby(_列名_)]
'''
[_データフレーム_|_列名_]をグループ化して、そのグループ名[の一覧が欲しい|を列挙したい]
'''

グループ名 = 'A'

_データフレーム_.groupby(_列名_).get_group(グループ名)
'''
@alt(のカテゴリ|の値|)

[_データフレーム_|_列名_]をグループ化して、グループ名で取り出す
'''

_データフレーム_.groupby(_列名_).size()
'''
_データフレーム_をあるカラムのカテゴリで_グループ化して、それぞれのグループごとの件数を知る
'''

_データフレーム_.groupby(_列名_).size()[s]
'''
_データフレーム_を各column毎にグループ化して、sというグループの[個数|大きさ]を求めたい
'''


_データフレーム_.groupby(_列名_).__集約__
'''
@poly(__集約__;合計 sum();平均値 mean();個数 count();最大値 max();最小値 min();分散 var();標準偏差 std())

[_データフレーム_|_列名_]をグループ化して、[それぞれの|]__集約__を求めたい
_列名_のカテゴリごとの__集約__[|を求めたい]
'''

_データフレーム_.groupby(['列A', '列B'], as_index=False).__集約__
'''
[ふたつ|２つ|複数]のカラム[から|を組み合わせて|で_]グループ化し、_列名_を求めたい
'''

_データフレーム_.groupby('列A')['列B'].__集約__
'''
_データフレーム_をグループ化し、あるカラムに対し_列名_を求めたい
'''

_データフレーム_.groupby('列A').describe()['列B']
'''
_データフレーム_をグループ化し、あるカラムの要約統計量を求めたい
'''