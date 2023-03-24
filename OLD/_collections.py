# collections
import itertools
import typing

import collections
'''
@alt(両端キュー=[両端キュー|双方向キュー|[キュー|スタック|デック]])

[コレクション|データ構造|両端キュー|カウンタ|名前付きタプル]を使いたい
'''

__イテラブル__ = [1, 2]
element = 1

_整数_ = 1
_両端キュー_ = collections.deque([1, 2])
names = ['A', 'B']

__要素__, __要素2__ = 1, 1
__イテラブル__= [1, 2]
'''
@poly(__要素__;_文字列_;_整数_;[要素|値|オブジェクト] 要素)
@poly(__イテラブル__;_リスト_;_タプル_;_配列_;_イテラブル_)
'''

collections.deque()
'''
[空の|]両端キュー[|を作りたい]
両端キュー[|が欲しい]
'''

最大長 = 10
'''
@poly(__最大長__;_整数_;最大長)
'''

collections.deque(maxlen=最大長)
'''
@alt(最大長|上限[|長||制限された長さ])

[両端キューが欲しい。|両端キューの]長さを制限したい
[最大長[を指定して、|長さの制限がある]]両端キューが欲しい
最大長nの両端キューを作りたい
'''

collections.deque(maxlen=_整数_)
'''
最大長_整数_の両端キューを作りたい
'''

_両端キュー_.appendleft(__要素__)
'''
@alt(先頭|最初|左[|側])
@alt(追加したい|[付け|つけ]加えたい|入れたい)

{_両端キュー_の先頭に|__要素__を}追加したい
'''

_両端キュー_.append(__要素__)
'''
@alt(末尾|最後|右[|側])
@alt(プッシュしたい|積む|スタックしたい)
@alt(エンキューしたい|enqueueしたい)

{_両端キュー_の末尾に|__要素__を}追加したい
{_両端キュー_に|__要素__を}エンキューしたい
{_両端キュー_に|__要素__を}プッシュしたい
'''

_両端キュー_.insert(_整数_, __要素__)
'''
@alt(挿入したい|差し込む|[途中|]追加したい)

{_両端キュー_の_整数_番目に|__要素__を}挿入したい
'''

_両端キュー_.popleft()
'''
@alt(デキューしたい|dequeue|要素を出したい)

{_両端キュー_の先頭から|要素を}取り出したい
_両端キュー_[を|から]デキューしたい
'''

_両端キュー_.pop()
'''
{_両端キュー_の末尾から|要素を}取り出したい
_両端キュー_[を|から]ポップしたい
'''

_両端キュー_.remove(__要素__)
'''
@alt(取り除きたい|削除したい)

{_両端キュー_から|[最初の|]__要素__を}取り除きたい
'''

_両端キュー_.clear()
'''
@alt(空にしたい|クリアしたい|全て取り除きたい)

_両端キュー_を空にしたい
'''

deq = collections.deque([1, 2, 3, 0], maxlen=5)

_両端キュー_.rotate(1)
'''
@alt(ローテーションしたい|回転させたい|輪番で回したい)
@alt(順序|順[|番])

{_両端キュー_の[要素|順序]を|[右に|]}ローテーションしたい
'''

_両端キュー_.rotate(-1)
'''
{_両端キュー_の[要素|順序]を|左に}ローテーションしたい
'''

_両端キュー_.maxlen
'''
_両端キュー_の最大長[|をえたい]
'''

len(_両端キュー_)
'''
_両端キュー_の[大きさ|要素数|サイズ|長さ][|を求めたい]
'''

len(_両端キュー_) == 0
'''
_両端キュー_[が|は]空[|である]かどうか
'''

len(_両端キュー_) != 0
'''
_両端キュー_[が|は]空でないかどうか
'''

__要素__ in _両端キュー_
'''
@alt(含まれてる|存在したい|ある)

{_両端キュー_の中に|__要素__[が|は]}含まれてるかどうか
'''

_両端キュー_[0]
'''
_両端キュー_の先頭[|の要素]が欲しい
'''

_両端キュー_[-1]
'''
_両端キュー_の末尾[|の要素]が欲しい
'''

_両端キュー_[_整数_]
'''
deqの_整数_番目[|の要素]が欲しい
'''

deq = collections.deque([1, 2, 1, 2, 1, 2])
start = 1
end = 3

FIXME collections.deque(itertools.islice(deq, start, end))
'''
deqから[部分|指定された範囲]を取り出したい
deqのstart〜endの[部分|]要素[|を得たい]
deqのstart番目からend[番目[|まで]]の[部分|]要素[|を得たい]
'''

_両端キュー_.index(__要素__)
'''
@alt(インデックス|位置)

_両端キュー_中の__要素__のインデックスを知りたい
'''

_両端キュー_.count(__要素__)
'''
@alt(数えたい|カウントしたい)

両端キュー中の__要素__[の[数|出現数]]を数えたい
'''

_両端キュー_.reverse()
'''
@alt(反転したい|逆順にしたい|逆に並べ直す)

{両端キューの要素を|[インプレースに|]}反転したい
'''

reversed(_両端キュー_)
'''
逆順の_両端キュー_[|を得たい]
_両端キュー_[|の順序]を逆[順|]にしたい

'''

list(_両端キュー_)
'''
_両端キュー_をリストに変換したい
'''

tuple(_両端キュー_)
'''
_両端キュー_をタプルに変換したい
'''

set(_両端キュー_)
'''
_両端キュー_を[セット|集合]に変換したい
'''

# カウンタ

collections.Counter()
'''
@alt(多重集合=[カウンタ|多重集合|計数器])

[空の|]多重集合[|を作りたい]
'''

FIXME collections.Counter(__イテラブル__)
'''
{__イテラブル__から|[|新しい]多重集合を}作りたい
__イテラブル__を多重集合に変換したい
'''

_辞書_ = {'A': 0, 'B': 1}

collections.Counter(_辞書_)
'''
{_辞書_から|多重集合を}作りたい
_辞書_を多重集合に変換したい
'''

_カウンタ_ = collections.Counter(A=2, B=1)
_カウンタ_ = _カウンタ_

_カウンタ_.elements()
'''
@alt(それぞれの|各|)
@alt(カウント=[カウント|[出現|]回数])
@alt(の回数|[回|]数|分の回数)
@alt(列挙したい|リストとして得たい)
@alt(項目|[要素|キー]|[文字列|値])

_カウンタ_のそれぞれの項目を[、その|]カウントだけ列挙したい
'''

_カウンタ_.most_common()
'''
@alt(順に|順番に|方から)

{_カウンタ_を|[高頻出|高頻度][|な]方から}列挙したい
{_カウンタ_を|多い順に}列挙したい
'''

_カウンタ_.most_common()[::-1]
'''
{_カウンタ_を|少ない順に}列挙したい
{_カウンタ_を|[低頻出|低頻度][|な]方から}列挙したい
'''

_整数_ = 10

_カウンタ_.most_common(_整数_)
'''
_カウンタ_の[上位|_整数_top|_整数_トップ]を列挙したい
'''

_カウンタ_.most_common()[:-_整数_-1:-1]
'''
_カウンタ_の[下位|ボトム]を列挙したい
'''

_カウンタ_ = collections.Counter([1, 1, 1, 1, 2, 2, 2, 3, 3])

_カウンタ_.most_common()[0]
'''
@alt(最頻出|最も頻出)

_カウンタ_の最頻出[な|の]項目[|を求めたい]
'''

_カウンタ_.most_common()[1]
'''
_カウンタ_から最頻出[な|の]項目の件数[|を求めたい]
'''

_カウンタ_.update(__イテラブル__)
'''
@alt(追加したい|増やしたい)

{_カウンタ_を|__イテラブル__で_}更新したい
{__イテラブル__をカウントして、|_カウンタ_を}更新したい
'''

_カウンタ_.update(_辞書_)
'''
{_カウンタ_を|_辞書_で_}更新したい
'''

_カウンタ_.subtract(__イテラブル__)
'''
@alt(引きたい|減らしたい)

{_カウンタ_から|__イテラブル__をカウントして}引きたい
'''

_カウンタ_.subtract(_辞書_)
'''
_カウンタ_から_辞書_を引きたい
'''

_カウンタ_[element] += 1
'''
_カウンタ_の項目を[|一つ]増やしたい
'''

_カウンタ_[element]
'''
_カウンタ_の項目のカウント[|を得たい]
'''

_カウンタ_.total()
'''
@alt(トータル|全)
_カウンタ_の[全数|全カウント][|を得たい]
'''

_カウンタ_.keys()
'''
_カウンタ_の項目一覧[|を得たい]
_カウンタ_の項目を列挙したい
'''

len(_カウンタ_)
'''
_カウンタ_の項目数[|を得たい]
'''

_カウンタ_.clear()
'''
_カウンタ_を[リセット|クリア|ゼロに]したい
'''

list(_カウンタ_)
'''
_カウンタ_のユニークな項目を列挙したい
_カウンタ_をリストに変換したい
'''

set(_カウンタ_)
'''
_カウンタ_を[集合|セット]に変換したい
'''

dict(_カウンタ_)
'''
_カウンタ_を辞書に変換したい
'''

_カウンタ_.items()
'''
_カウンタ_のキーとカウントを列挙したい
'''

pairs = [('A', 1)]

collections.Counter(dict(pairs))
'''
ペアリストpairsからカウンタを[作りたい|構築したい]
'''

+_カウンタ_
'''
_カウンタ_から[ゼロ|マイナス]カウントを取り除きたい
_カウンタ_の正の[数|カウント][のみ|だけ][残|に]したい
'''
_カウンタ_ & _カウンタ_
'''
@alt(インターセクション=[積集合|共通部分|[交わり|交差]|インターセクション|∩])
@alt(同士で|間で|の)

[_カウンタ_同士|_カウンタ_と_カウンタ_][で|の]インターセクション[|を求めたい|を取りたい]
２つの_カウンタ_の共通したい要素[|を求めたい]
_カウンタ_同士でインターセクション演算したい
'''

_カウンタ_ | _カウンタ_
'''
@alt(ユニオン|和集合|∪)

_カウンタ_同士でユニオン[|を求めたい|を取りたい]
２つの_カウンタ_のいずれかに含まれる要素[|を求めたい]
_カウンタ_同士でユニオン演算したい
'''

name = 'A'
name2 = 'B'

クラス名 = 'C'
プロパティ名のリスト = ['A', 'B']

C = collections.namedtuple('クラス名', プロパティ名のリスト)
'''
@alt(名前付きタプル|ネームドタプル)

名前付きタプルを定義したい
'''

issubclass(_型名_, tuple)
'''
_型名_[が|は]名前付きタプルかどうか
'''

パラメータ = (1, 2, 3)

名前付きタプルのクラス名._make(パラメータ)
'''
@alt(パラメータ|引数|データ)

{名前付きタプル[のクラス名|]を|パラメータから}インスタンス化したい
'''

_結果_ = C(1, 2, 3)

hasattr(_結果_, '_asdict') and hasattr(_結果_, '_fields')
'''
_結果_が名前付きタプル[|型|のインスタンス]かどうか
'''

aNamedTupleObject = C(1, 2, 3)

aNamedTupleObject._asdict()
'''
名前付きタプルを辞書に変換したい
'''

###

collections.ChainMap()
'''
@alt(チェーンマップ|階層化[マップ|辞書])

[空|ルート]のチェーンマップ[|を作りたい]
'''

collections.ChainMap(_辞書_)
'''
@alt(階層化したい|ネスト化したい)

_辞書_をチェーンマップに変換したい
_辞書_を階層化したい
'''

collections.ChainMap(_辞書_, _辞書_)
'''
@alt(チェーンしたい|階層的につなぎたい|ネストしたい)

２つの_辞書_をチェーンしたい
[２つの_辞書_|_辞書_と_辞書_]を階層化したい
'''