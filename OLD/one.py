# https://knooto.info/python-snippets/#json

import collections
import typing
import itertools
import operator
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['font.size'] = 18
plt.tight_layout()
'''
[matplotlibで|]グラフの[文字|フォント]サイズを大きくする
グラフの[文字|フォント]サイズを[整数]_int_ptにする
'''

x = np.linspace(-3, 3, 20)  # -3～3まで20刻みでxの値を生成
y = x**2 - 1            # 2次関数
plt.plot(x, y, label='$y=x^2+1$')      # 曲線を引く
plt.show()              # グラフ表示
'''
[2次関数|放物線]を[グラフ表示する|描きたい]
'''

x = np.arange(-np.pi, -np.pi, 0.25)
y = np.sin(x)
plt.plot(x, y, label='$y=\sin{x}$')      # 曲線を引く
plt.show()              # グラフ表示
'''
[サイン|sin][曲線|]をグラフ[描画|表示|化]する
'''

x = np.arange(-np.pi, -np.pi, 0.25)
y = np.cos(x)
plt.plot(x, y, label='$y=\cos{x}$')      # 曲線を引く
plt.show()              # グラフ表示
'''
[コサイン|cos][|曲線]をグラフ[描画|表示|化]する
'''

plt.plot(_ColumnName_, _列名2_)
plt.title('(タイトル)')
plt.show()
'''
[カラム名]_ColumnName_と[カラム名]_ColumnName_を[折れ線|]グラフにする
'''

# 設定


def predicate(a): return a > 0


_int_ = 1

# プリント

print()
'''
[空行を|改行[だけ|のみ]]プリントする
改行する
'''

print(_int_)
'''
[整数|結果]_int_をプリントする
'''

print(_int_, _int_)
'''
２つの[整数|結果]_int_を[順に|]プリントする
'''

print(_int_, _int_, _int_)
'''
[３つ|複数]の[整数|結果]_int_を[順に|]プリントする
'''

end = _str_
'''
ただし、{改行[|する]の代わりに|_str_を}用いる
ただし、{[プリント|出力]の終端に|_str_を}用いる
'''

end = ''
'''
ただし、改行しない[|ように設定する]
ただし、改行なし
'''

print(_int_, end='')
'''
{改行なしに|[結果|整数]_int_を}プリントする
{[結果|整数]_int_の出力を|改行なしに}行う
'''

print(_int_, _int_, end='')
'''
{改行なしに|[２つの|複数の][結果|整数]_int_を}プリントする
'''

print(*_list_)
'''
[リスト|タプル]_list_[[の要素|]を展開してプリントする
'''

_ = [("','", "カンマ")]

sep = ','
'''
ただし、セパレータをカンマにする
ただし、カンマをセパレータで使用する
'''

sep = ''
'''
ただし、セパレータを使用しない
'''

print(_int_, _int_, sep=',')
'''
{[結果|整数]_int_と[結果|整数]_int_を|カンマ区切りで}プリントする
'''

print('Hello World')
'''
[ハローワールド|こんにちは世界][と|を]プリントする
{試しに|何か}動か[す|してみたい]
[最初の|初めての]プログラムを書きたい
'''

print(f'\033[1m{_str_}\033[0m')
'''
{[文字列|結果]_str_を|[太字で|強調して]}プリントする
'''

print(f'\033[2m{_str_}\033[0m')
'''
{[文字列|結果]_str_を|[下線付きで|アンダーラインを付けて]}プリントする
'''

_ = [('31m', '赤色'), ('32m', '緑色'), ('33m', '黄色'), ('30m', '黒色'),
     ('34m', '青色'), ('35m', '紫色'), ('36m', '水色'), ('37m', '白色')]

print(f'\033[31m{_str_}\033[0m')
'''
{[文字列|結果]_str_を|赤色で}プリントする
'''

f'\033[31m{_str_}\033[0m'
'''
[文字列|結果]_str_を赤色にする
'''

_ = [('.3f', '3桁'), ('.2f', '2桁'), ('.1f', '1桁'), ('.4f', '4桁')]

_float_ = 0.11

print(f'{_float_:.3f}')
'''
[[結果|実数|数値]_float_の]小数点以下3桁まで[を|]プリントする
'''

'{:.3f}'.format(_float_)
'''
[結果|実数|数値]_float_を小数点以下3桁にした[文字列]
'''

# 入力

input()
'''
標準入力から1行[読み取りたい|受け取りたい]
[ユーザ|標準入力]から入力される
'''

int(input())
'''
[ユーザの]入力を整数として受け取りたい
ユーザが整数を入力する
ユーザから入力される
'''


##

x = 0
'''
変数を定義する
'''

x, y = y, x
'''
変数[|の値]をスワップする
'''

_list_[x], _list_[y] = _list_[y], _list_[x]
'''
[リスト]_list_の要素をスワップする
[リスト]_list_のx番目とy番目をスワップする
'''

# 組み込み関数（計算）

abs(_float_)
'''
[数値|実数]_float_の絶対値
'''

bool(_int_)
'''
[結果|整数]_int_の論理値
[結果|整数]_int_を論理値に変換する
[結果|整数]_int_が真かどうか
'''

complex(_float_, _float_)
'''
[数値|実数]_float_の複素数
[数値|実数]_float_を複素数にする
'''

divmod(_float_, _float_)
'''
二数の[商と余り]
'''

float(_str_)
'''
[[文字列]_str_を|]浮動小数点数に変換する
[[文字列]_str_を|]から変換した[浮動小数点数]
'''

int(_str_)
'''
[[文字列]_str_を|]整数に変換する
[文字列]_str_から変換した[整数]
'''

# 組み込み関数（文字列）

ascii(_object_)
'''
[[オブジェクト]_object_を|]印字できる文字列にする
[[オブジェクト]_object_の|]印字可能な文字列
'''

hash(_str_)
'''
[文字列|オブジェクト]_str_のハッシュ値
'''

max(_int_, _int_)
'''
２[変数|数|つ]の[最大値]
[整数|実数]_int_と[整数|実数]_int_の大きい方
'''

min(_int_, _int_)
'''
２[変数|数|つ]の[最小値]
[整数|実数]_int_と[整数|実数]_int_の小さい方
'''

max(_int_, _int_, _int_)
'''
３[変数|数|つ]の[最大値]
'''

min(_int_, _int_, _int_)
'''
３[変数|数|つ]の[最小値]
'''

max(_list_)
'''
[数列|リスト]の最大値
'''

min(_list_)
'''
[数列|リスト]の最小値
'''

max(_list_)/len(_list_)
'''
[数列|リスト]の平均値
'''

min(_list_)/len(_list_)
'''
[数列|リスト]の平均値
'''

str(_int_)
'''
[整数|実数]_int_を文字列に変換する
[整数|実数]_int_を文字列化する
'''

# collections

_list_ = [1, 2]
element = 1

_deque_ = collections.deque([1, 2])
names = ['A', 'B']
_list_ = [1, 2]

_deque_ = collections.deque()
'''
[空の|新しい]両端キューを用意する
'''

_deque_ = collections.deque(maxlen=n)  # 最大長
'''
[長さの制限がある|最大長のある]両端キューを[新たに|]用意する
最大長nの両端キューを用意する
'''

_deque_ = collections.deque(_list_)  # 最大長
'''
[リスト|タプル]_list_を両端キューに変換する
[リスト|タプル]_list_から作成した両端キュー
'''

_ = [('_str_', '[要素|文字列]_str_'), ('_int_', '[要素|数値]_int_')]

_deque_.appendleft(_str_)
'''
{[両端キュー]_deque_の先頭に|[要素|文字列]_str_を}追加する
'''

_deque_.append(_str_)
'''
{[両端キュー]_deque_の末尾に|[要素|文字列]_str_を}追加する
'''


_deque_.insert(n, _str_)
'''
{[両端キュー]_deque_のn番目に|[要素|文字列]_str_を}挿入する
'''

_deque_.popleft()
'''
{[両端キュー]_deque_の先頭から|要素を}デキューする
'''

_deque_.pop()
'''
{[両端キュー]_deque_の末尾から|要素を}ポップする
'''

_deque_.remove(_str_)
'''
{[両端キュー]_deque_から|[最初の|][要素|文字列]_str_を}削除する
'''

_deque_.clear()
'''
[両端キュー]_deque_を空にする
'''

deq = collections.deque([1, 2, 3, 0], maxlen=5)

_deque_.rotate(1)
'''
{[両端キュー]_deque_の[要素|順序]を|[右に|]}ローテーションする
'''

_deque_.rotate(-1)
'''
{[両端キュー]_deque_の[要素|順序]を|左に}ローテーションする
'''

list(collections.deque(_list_).rotate(-n))
'''
{[リスト]_list_[の要素|]を|左にn個}ローテーションする
'''

list(collections.deque(_list_).rotate(n))
'''
{[リスト]_list_[の要素|]を|右にn個}ローテーションする
'''

_deque_.maxlen
'''
[両端キュー]_deque_の最大長
'''

len(_deque_)
'''
[両端キュー]_deque_の[大きさ|要素数|サイズ|長さ]
'''

len(_deque_) == 0
'''
[両端キュー]_deque_[が|は]空[|である]かどうか
'''

len(_deque_) != 0
'''
[両端キュー]_deque_[が|は]空でないかどうか
'''

_str_ in _deque_
'''
{[両端キュー]_deque_の中に|[要素|文字列]_str_[が|は]}存在するかどうか
'''

_str_ not in _deque_
'''
{[両端キュー]_deque_の中に|[要素|文字列]_str_[が|は]}存在しないかどうか
'''

_deque_[0]
'''
[両端キュー]_deque_の先頭[|の要素]
'''

_deque_[-1]
'''
[両端キュー]_deque_の末尾[|の要素]
'''

_deque_[n]
'''
[両端キュー]_deque_のn番目[|の要素]
'''

collections.deque(itertools.islice(_deque_, _int_, _int_))  # start, end
'''
[両端キュー]_deque_の部分キュー
'''

_deque_.index(_str_)
'''
[両端キュー]_deque_中の[要素|文字列]_str_のインデックス
'''

_deque_.count(_str_)
'''
[両端キュー]_deque_中の[要素|文字列]_str_の出現数
[両端キュー]_deque_中の[要素|文字列]_str_をカウントする
'''

_deque_.reverse()
'''
{[両端キュー]_deque_の要素を|[インプレースに|]}反転する
'''

reversed(_deque_)
'''
[両端キュー]_deque_を逆順にする
'''

list(_deque_)
'''
[両端キュー]_deque_をリストに変換する
[両端キュー]_deque_[から変換した|の]リスト
'''

tuple(_deque_)
'''
[両端キュー]_deque_をタプルに変換する
[両端キュー]_deque_[から変換した|の]タプル
'''

set(_deque_)
'''
[両端キュー]_deque_をセットに変換する
[両端キュー]_deque_[から変換した|の]セット
'''

# カウンタ
#

collections.Counter()
'''
[空の|新しい]カウンタを用意する
'''

collections.Counter(_list_)
'''
{[リスト]_list_から|カウンタを}[新たに|]作成する
_list_をカウンタに変換する
'''

_dict_ = {'A': 0, 'B': 1}

collections.Counter(_dict_)
'''
{[辞書]_list_から|カウンタを}作成する
_dict_をカウンタに変換する
'''

_Counter_ = collections.Counter(A=2, B=1)
_Counter_ = _Counter_

_Counter_.elements()
'''
@alt(それぞれの|各|)
@alt(カウント=[カウント|[出現|]回数])
@alt(の回数|[回|]数|分の回数)
@alt(列挙する|リストとして得たい)
@alt(項目|[要素|キー]|[文字列|値])

_Counter_のそれぞれの項目を[、その|]カウントだけ列挙する
'''

_Counter_.most_common()
'''
@alt(順に|順番に|方から)

{_Counter_を|[高頻出|高頻度][|な]方から}列挙する
{_Counter_を|多い順に}列挙する
'''

_Counter_.most_common()[::-1]
'''
{_Counter_を|少ない順に}列挙する
{_Counter_を|[低頻出|低頻度][|な]方から}列挙する
'''

_Counter_.most_common(_int_)
'''
_Counter_の[上位|_int_top|_int_トップ]を列挙する
'''

_Counter_.most_common()[:-_int_-1:-1]
'''
_Counter_の[下位|ボトム]を列挙する
'''

_Counter_ = collections.Counter([1, 1, 1, 1, 2, 2, 2, 3, 3])

_Counter_.most_common()[0]
'''
@alt(最頻出|最も頻出)

_Counter_の最頻出[な|の]項目[|]
'''

_Counter_.most_common()[1]
'''
_Counter_から最頻出[な|の]項目の件数[|]
'''

_Counter_.update(_list_)
'''
@alt(追加する|増やする)

{_Counter_を|_list_で_}更新する
{[リスト]_list_をカウントして、|_Counter_を}更新する
'''

_Counter_.update(_dict_)
'''
{_Counter_を|_dict_で_}更新する
'''

_Counter_.subtract(_list_)
'''
@alt(引きたい|減らする)

{_Counter_から|_list_をカウントして}引きたい
'''

_Counter_.subtract(_dict_)
'''
_Counter_から_dict_を引きたい
'''

_Counter_[element] += 1
'''
_Counter_の項目を[|一つ]増やする
'''

_Counter_[element]
'''
_Counter_の項目のカウント[|を得たい]
'''

_Counter_.total()
'''
@alt(トータル|全)
_Counter_の[全数|全カウント][|を得たい]
'''

_Counter_.keys()
'''
_Counter_の項目一覧[|を得たい]
_Counter_の項目を列挙する
'''

len(_Counter_)
'''
_Counter_の項目数[|を得たい]
'''

_Counter_.clear()
'''
_Counter_を[リセット|クリア|ゼロに]する
'''

list(_Counter_)
'''
_Counter_のユニークな項目を列挙する
_Counter_をリストに変換する
'''

set(_Counter_)
'''
_Counter_を[集合|セット]に変換する
'''

dict(_Counter_)
'''
_Counter_を辞書に変換する
'''

_Counter_.items()
'''
_Counter_のキーとカウントを列挙する
'''

pairs = [('A', 1)]

collections.Counter(dict(pairs))
'''
ペアリストpairsからカウンタを[作成する|構築する]
'''

+_Counter_
'''
_Counter_から[ゼロ|マイナス]カウントを取り除きたい
_Counter_の正の[数|カウント][のみ|だけ][残|に]する
'''
_Counter_ & _Counter_
'''
@alt(インターセクション=[積集合|共通部分|[交わり|交差]|インターセクション|∩])
@alt(同士で|間で|の)

[_Counter_同士|_Counter_と_Counter_][で|の]インターセクション[||を取りたい]
２つの_Counter_の共通する要素[|]
_Counter_同士でインターセクション演算する
'''

_Counter_ | _Counter_
'''
@alt(ユニオン|和集合|∪)

_Counter_同士でユニオン[||を取りたい]
２つの_Counter_のいずれかに含まれる要素[|]
_Counter_同士でユニオン演算する
'''

name = 'A'
name2 = 'B'

クラス名 = 'C'
プロパティ名のリスト = ['A', 'B']

C = collections.namedtuple('クラス名', プロパティ名のリスト)
'''
@alt(名前付きタプル|ネームドタプル)

名前付きタプルを定義する
'''

issubclass(_型名_, tuple)
'''
_型名_[が|は]名前付きタプルかどうか
'''

パラメータ = (1, 2, 3)

名前付きタプルのクラス名._make(パラメータ)
'''
@alt(パラメータ|引数|データ)

{名前付きタプル[のクラス名|]を|パラメータから}インスタンス化する
'''

[結果 = C(1, 2, 3)

hasattr([結果]_str_, '_asdict') and hasattr([結果]_str_, '_fields')
'''
[結果]_str_が名前付きタプル[|型|のインスタンス]かどうか
'''

aNamedTupleObject = C(1, 2, 3)

aNamedTupleObject._asdict()
'''
名前付きタプルを辞書に変換する
'''

###

collections.ChainMap()
'''
@alt(チェーンマップ|階層化[マップ|辞書])

[空|ルート]のチェーンマップ
'''

collections.ChainMap(_dict_)
'''
@alt(階層化する|ネスト化する)

_dict_をチェーンマップに変換する
_dict_を階層化する
'''

collections.ChainMap(_dict_, _dict_)
'''
@alt(チェーンする|階層的につなぎたい|ネストする)

２つの_dict_をチェーンする
[２つの_dict_|_dict_と_dict_]を階層化する
'''
import copy

_dict_ = {'A': 1}
_list_ = ['A', 'B']
[キー = 'A'
_str_ = 'A'

[要素]_str_ = 1
'''
@poly([キー]_str_;_str_;キー)
@poly([要素]_str_;_str_;_int_;_tuple_)
'''

{}
'''
@alt(得る|参照する|見る)

空の_dict_を作成する
[空の|]_dict_
'''

dict(name='kogi', age=6)
'''
@alt(キー|項目名)
変数名をキーとして、_dict_を作成する
'''

_dict_[[キー]_str_]
'''
_dict_の[キー]_str_の値
_dict_の[キー]_str_に対応した値
'''

list(_dict_)
'''
_dict_のキーを列挙する
_dict_のキーの一覧
'''

len(_dict_)
'''
@alt(エントリ|項目|値)
_dict_のエントリ数
'''

_dict_.clear()
'''
@alt(クリアする|消去する|空にする)
_dict_[の全[エントリ]|]をクリアする
'''

_dict_.copy()
'''
_dict_を[|浅く]コピーする
_dict_の[浅い|]コピーを作る
'''

見つからない場合の値 = None

_dict_.get([キー]_str_, 見つからない場合の値)
'''
{[辞書]_dict_から|エラーなく}[キー]_str_の値
_dict_の[キー]_str_に対応した値
'''


_dict_[[要素]_str_]= _dict_.get([要素]_str_, 0) + 1
'''
_dict_で[要素]_str_[|の数]を[数えたい|カウントする]
'''


[キー]_str_ in _dict_
'''
@alt(存在する|ある|存在している)
@alt(定義済み|[|既に]定義されている)

{[キー]_str_が|_dict_に}存在するかどうか
{[キー]_str_が|_dict_上で}定義済みかどうか
'''

[キー]_str_ not in _dict_
'''
@alt(存在しない|ない|存在していない)
@alt(未定義|[まだ|]定義されていない)

{[キー]_str_が|_dict_に}存在するかどうか
{[キー]_str_が|_dict_上で}未定義かどうか
'''

if [キー]_str_ in _dict_:
    print(_dict_[[キー]_str_])  # 具体的に
'''
_dict_に[キー]_str_が存在するとき、
'''

if [キー]_str_ not in _dict_:
    print(_dict_[[キー]_str_])  # 具体的に
'''
_dict_に[キー]_str_が存在しないとき、
'''

_dict_.items()
'''
_dict_のキーとその[値|エントリ]を列挙する
[_dict_から|]キーとその[値|エントリ]を[ペア|組|タプル]として取り出する
'''

for key, value in _dict_.items():
    print(key, value)  # 具体的に
'''
_dict_の内容を[|取り出し、][繰り返し|ひとつずつ]処理する
'''

_dict_.keys()
'''
_dict_のキーを列挙する
'''

list(_dict_.keys())
'''
_dict_のキーをリストに変換する
_dict_のキーの一覧
'''

for key in _dict_.keys():
    print(_dict_[key])  # 具体的に
'''
_dict_のキーを[繰り返し|ひとつずつ]処理する
'''

_dict_.values()
'''
_dict_の[値|エントリ]を列挙する
_dict_の[値|エントリ]の一覧
'''

list(_dict_.values())
'''
_dict_の[値|エントリ]の一覧
_dict_内の値をリストとして[|得る]
'''

for value in _dict_.values():
    print(value)  # 具体的に
'''
_dict_の[値|エントリ]を[繰り返し|ひとつずつ]処理する
'''

[要素]_str_ in _dict_.values()
'''
{[要素]_str_[が|は]|_dict_の値として}含まれているかどうか
'''

[要素]_str_ not in _dict_.values()
'''
{[要素]_str_[が|は]|_dict_の値に}含まれていないかどうか
'''

_dict_[[キー]_str_] = [要素]_str_
'''
_dict_の[キー]_str_を[要素]_str_に[設定|変更|]する
_dict_に[要素]_str_を[キー]_str_として加えたい
'''



_dict_.setdefault([キー]_str_, [要素]_str_)
'''
{[キー]_str_が|_dict_に}存在しないとき、[要素]_str_を追加する
'''


_dict_.update(_dict_)
'''
@alt(追加する=[更新する|追加する|加えて、更新する])

_dict_を[別の|]_dict_を追加する
'''

kwargs = dict(A=1, B=2)

_dict_.update(**kwargs)  # キーワード引数
'''
{[辞書]_dict_に|キーワード引数を}追加する
'''

_dict_ | _dict_
'''
@alt(合体する|結合する|マージする)

ふたつの_dict_を合体する
'''

_dict_.pop([キー]_str_)
'''
@alt(ポップする|取り除きたい)

{[辞書]_dict_から|キーで指定されたエントリを}ポップする
'''

_dict_.popitem()
'''
{[辞書]_dict_から|最後[の|に追加した]エントリを}ポップする
'''


{v: k for k, v in _dict_.items()}
'''
_dict_のキーと値を入れ替えたい
'''

リスト = [1, 2, 3]
リスト2 = [4, 5, 6]

dict(zip(_list_, _list_))
'''
２つの_list_から_dict_を作成する
'''

dict(_dict_)
'''
@alt(コピーする|複製する)
_dict_を[浅く|]コピーする
_dict_のコピーを作成する
'''

{k: copy.copy(v) for k, v in _dict_.items()}
'''
_dict_の[内部|値]もコピーする
'''


import janome

from janome.tokenizer import Tokenizer
janome = Tokenizer()
for token in janome.tokenize(_str_):
    print(token)
'''
_str_を形態素解析する
'''
# 整数

[整数]_int_ = 2


"@root_cause_analysis"
'''
[エラーの|][原因|理由][は[|？]|が知りたい]
'''


"@hint"
'''
どうしたらいいの？
ヒント[|が|を][ください|ちょうだい|欲しい]
'''


"@help"
'''
助けて[|ほしい|みて]
困った
'''


"@fix_code"
'''
[コードを|][修正|直]して[|ほしい|みて]
[間違い|エラー]を直して[|ほしい|みて]
ワンチャン
'''

"@emergency_call"
'''
[先生|TA]を[よんで|呼んで|読んで]ください
'''

"@thank"
'''
ありがとう
素晴らしい
[カワイイ|かわいい|可愛い][|ね]
'''

"@sorry"
'''
ひどい
あんまりだ
'''

"@vow"
'''
[狂った|馬鹿な|バカな|アホな]犬め
狂犬病なの
ダメ[|ダメ]だね
'''

"@dic term=プログラミング"
'''
プログラミング[とは|って[何|]]
'''

"@show_len target=_list_"
'''
_list_の[大きさ|長さ]を[見|み]たい
'''
# list

_list_, [数列 | リスト]_list_ = [1, 2, 3]
_list_ = [4, 5]
_tuple_ = (1, 2, 3)
[リスト_list_ = _list_
step = 2
iterable = [1, 2, 3]
[整数]_int_ = 2
[要素]_str_, [要素]_str_ = 1, 1
'''
@poly([要素]_str_;_str_;_int_;[結果]_str_)
@poly([要素;_str_;_int_;[結果]_str_)
@poly([リスト|タプル_list_;_list_;_tuple_)
@poly([数列|リスト]_list_;_list_;数列)
@poly(_整数;_int_;n)
@poly(_int_;_int_;m)
'''


# リスト

[]
'''
[空列|空のリスト]
'''

()
'''
空の[タプル|組]
'''

([要素]_str_,)
'''
[要素]_str_一つの[タプル|組]
'''

([要素]_str_, [要素]_str_)
'''
[要素]_str_と[要素]_str_[から成る|の]ペア
'''

[[要素]_str_]
'''
[要素]_str_一つのりスト
'''

[[要素]_str_] * _int_
'''
[整数]_int_個の[要素]_str_があるリスト
'''

[0] * _int_
'''
長さ_int_の[リスト|数列]
'''

行数, 列数= 2, 2

[[0] * 列数 for _ in range(行数)]
'''
２次元リスト
'''

[[0] * _int_ for _ in range(_int_)]
'''
[整数]_int_行_int_列の[２|二]次元リスト
[整数]_int_[×|x]_int_の[２|二]次元リスト
'''

tuple(_list_)
'''
@alt(に変換する|[に|化]する)
リストを[タプル|組]に変換する
リストをイミュータブルにする
'''

list(_tuple_)
'''
タプルをリストに変換する
タプルをミュータブルにする
'''

len(_list_)
'''
@alt(|を調べたい||)
@alt(長さ|要素数|個数)

[リスト|タプル]_list_の長さ
'''

len(_list_) == 0
'''
[リスト|タプル]_list_が空かどうか
'''

len(_list_) != 0
'''
[リスト|タプル]_list_が空でないかどうか
'''

_list_ + _list_
'''
@alt(連結する|結合する|接続する|加えたい)

[二つの|][リスト|タプル]_list_を連結する
'''

_list_ * _int_
'''
[リスト|タプル]_list_を_int_倍する
[リスト|タプル]_list_を_int_回、連結する
'''

_list_[0]
'''
@alt(先頭|最初)
@alt(末尾|最後)

[リスト|タプル]_list_の先頭[|の[要素|値]]
'''

_list_[-1]
'''
[リスト|タプル]_list_の末尾[|の[要素|値]]
'''

_list_[_int_]
'''
[リスト|タプル]_list_の_int_番目の[|の[要素|値]]
'''

_list_[1:]
'''
@alt(取り除きたい|除きたい|捨てたい)
[リスト|タプル]_list_の先頭を[取り除きたい|除きたい|捨てたい]
'''

_list_[_int_:]
'''
@alt(取り出する|得る|抽出する)
[リスト|タプル]_list_の先頭の_int_個を取り除きたい
[リスト|タプル]_list_の_int_番目以降の[部分|要素]を取り出する
'''

_list_[:-1]
'''
[リスト|タプル]_list_の末尾を取り除きたい
'''

_list_[:-_int_]
'''
[リスト|タプル]_list_の末尾の_int_要素を取り除きたい
[リスト|タプル]_list_の末尾から_int_番目以前の[部分|要素]を取り出する
'''

_list_[::-1]
'''
[リスト|タプル]_list_の[要素|値]を逆順にする
[リスト|タプル]_list_を逆順にする
'''

_list_[::2]
'''
{[リスト|タプル]_list_を|[ひとつ置きに|ひとつ飛ばしで]}取り出する
'''

_list_[_int_:_int_]
'''
[リスト|タプル]_list_の_int_番目から_int_番目[まで][の部分][|を取り出する]
'''

slice(_int_)
'''
[整数]_int_までのスライス
'''

slice(_int_, _int_)
'''
[整数]_int_から_int_までのスライス
'''

slice(_int_, _int_, step)
'''
nからn2までのstepごとによるスライス
'''


sum([数列 | リスト]_list_)
'''
@alt(|計算する|)

[数列|リスト]_list_の[合計値|合計|総和]
'''

min([数列 | リスト]_list_)
'''
@alt(一番|最も)

[数列|リスト]_list_[の中|]の[[最小値]_int_|一番小さい値]
'''

max([数列 | リスト]_list_)
'''
[数列|リスト]_list_[|の中]の[[最大値]_int_|一番大きい値]
'''

sum([数列 | リスト]_list_)/len([数列 | リスト]_list_)
'''
[数列|リスト]_list_の[平均値|平均]
'''


range(len(_list_))
'''
リストの長さだけ繰り返す
'''

range(n)
'''
@test(list(_))
n[個|回]の数値イテラブル
0からnの範囲[|で|を得る]
'''

range(n, n2)
'''
@test(list(_))
nからn2の範囲[|で|を得る]
'''

list(range(_int_))
'''
@alt(数列|整数列|整数リスト)
[整数]_int_個の数列
'''

list(range(_int_, _int_+1))
'''
[整数]_int_から_int_までの数列
'''

list(range(_int_, _int_+1, 2))
'''
@alt(ひとつ飛ばし|一つ置き)
[整数]_int_から_int_までの数列がひとつ飛ばしで欲しい
'''

list(range(0, _int_, 2))
'''
[整数]_int_までの偶数列
'''

list(range(1, _int_, 2))
'''
[整数]_int_までの奇数列
'''


_list_.append([要素]_str_)
'''
@alt(追加する|加えたい)

_list_[に|の末尾に][要素]_str_を追加する
'''

_list_.extend(_list_)
'''
_list_[に|の末尾に]_list_を[追加する|展開する]
_list_[に|の末尾に]_list_を追加して[拡張する|広げたい]
'''

_list_.insert(_int_, [要素]_str_)
'''
@alt(挿入する|差し込む)

_list_の_int_番目に[要素]_str_を[挿入する|追加する]
'''

_list_.pop()
'''
_list_の末尾から[要素|値]を[ポップする|取り出する|取り除きたい]
'''

_list_.pop(_int_)
'''
_list_の_int_番目から[要素|値]を[ポップする|取り出する|取り除きたい]
'''

_list_.clear()
'''
@alt(消去する|消する)

_list_の[全ての|全|][要素|値]を[クリアにする|取り除きたい|消去する|空にする]
'''

_list_.remove([要素]_str_)
'''
_list_から[要素]_str_を[取り除きたい|取り出する]
'''

del _list_[_int_]
'''
_list_の_int_番目[の[要素|値]|]を[削除する|消する]
'''

[要素]_str_ in _list_
'''
[要素]_str_[が|は][リスト|タプル]_list_の要素かどうか
[要素]_str_[が|は][リスト|タプル]_list_に含まれるかどうか
'''

[要素]_str_ not in _list_
'''
[要素]_str_[が|は][リスト|タプル]_list_の要素でないかどうか
[要素]_str_[が|は][リスト|タプル]_list_に含まれないかどうか
'''

_list_.index([要素]_str_)
'''
@alt(内|中)
@alt(インデックス|位置|場所)

[リスト|タプル]_list_[|中]の_要素_のインデックス
[リスト|タプル]_list_[|中]の最初の_要素_を探する
'''

sorted(_list_)
'''
@alt(ソートする|並べたい|並べ直する)
[リスト|タプル]_list_[の[要素|値]]をソートする
'''

sorted(_list_, reverse=False)
'''
@alt(昇順に|小さい[順に|方から])

{[リスト|タプル]_list_[の[要素|値]]を|昇順に}ソートする
'''

sorted(_list_, reverse=True)
'''
@alt(降順に|大きい[順に|方から])

{[リスト|タプル]_list_[の[要素|値]]を|昇順に}ソートする
'''


_list_.index([要素]_str_) if [要素]_str_ in _list_ else -1
'''
{[リスト]_list_[|中]の_要素_の位置を|エラーなく}[得たい|知りたい]
'''

def _function_(x): return x+1


sorted(_list_, key=_function_)
'''
{[リスト|タプル]_list_を|_function_を使って}ソートする
'''

_list_.copy()
'''
@alt(複製する|コピーする)

リストを複製する
'''

reversed(_list_)
'''
@test(list(_))
@alt(反転する|逆順にする|リバースする|逆さにする)

[リスト|タプル]_list_を反転する
'''

all(_list_)
'''
[リスト|タプル]_list_[内の要素][が|は]全て真かどうか
'''

any(_list_)
'''
[リスト|タプル]_list_[内の要素][が|は]少なくとも一つ真かどうか
'''

print(*_list_)
'''
[リスト|タプル]_list_を[引数として展開して|順に]プリントする
{[リスト|タプル]_list_[の[各|]要素|]を|空白区切りで}プリントする
'''

print(*_list_, sep=',')
'''
[リスト|タプル]_list_を[引数として展開して|カンマ区切りで]プリントする
'''

sum(_list_)
'''
@alt(フラット化する|flattenする)

２次元[リスト|タプル]_list_をフラット化する
'''

enumerate(_list_)
'''
@alt(ナンバリングし|[番号|順番|順序]付けし)

[リスト|タプル]_list_をナンバリングする
'''

enumerate(_list_, start=n)
'''
[リスト|タプル]_list_をnからナンバリングする
'''

for i, value in enumerate(_list_):
    print(i, value)
'''
@alt(繰り返し処理|順に処理|一つずつ処理)
[リスト|タプル]_list_をナンバリングしながら、繰り返し処理する
'''


filter(_function_, _list_)
'''
@alt(のそれぞれ||の各要素)
{[リスト|タプル]_list_のそれぞれを|_function_[で|を使って]}フィルタする
'''

map(_function_, _list_)
'''
{[リスト|タプル]_list_のそれぞれを|_function_[で|を使って]}[変換する|マップする]
'''

list(filter(_function_, _list_))
'''
@alt(のそれぞれ||の各要素)
{[リスト|タプル]_list_のそれぞれを|_function_[で|を使って]}フィルタしたリスト
'''

list(map(_function_, _list_))
'''
[リスト|タプル]_list_のそれぞれを|_function_[で|を使って]変換したリスト
'''
import numpy as np

import matplotlib.pyplot as plt
'''
@alt(描画する|描きたい|プロットする)
@alt(可視化する|[図示|作図|描画]する)

@alt(グラフの中|グラフ|グラフ[内|中|])
@alt(できる|可能な)
@alt(に設定する|[に|と]する|に[セット|指定]する|に変更する|変えたい)


グラフを描画する[準備をする|]
グラフを使う[準備をする|]
'''

# title

plt.title('(グラフのタイトル)')
'''
@alt(タイトル|[題名|名前|名称])

[グラフの|グラフで使う]タイトルを設定する
{グラフに|タイトル}を付けたい
'''

[[横幅]_int_]_int_ = 8
[[高さ]_int_]_int_ = 6

plt.figure(figsize=(_int_, _int_))  # 単位はインチ
'''
[グラフ|図]の[大きさ|[縦横|]サイズ]を設定する
'''

plt.xlabel('(x軸ラベル)')
'''
[グラフの|]横軸の軸ラベルを設定する
'''

plt.ylabel('(y軸ラベル)')
'''
@alt(縦軸|y軸|y座標)

[グラフの|]縦軸の軸ラベルを設定する
[グラフの|]縦軸に軸ラベルを付けたい
'''

[最小値]_int_, [最大値]_int_ = 0, 100

plt.xlim([最小値]_int_, [最大値]_int_)
'''
[グラフの|]横軸の表示範囲を[変更|調整]する
横軸の[最大[|値]|最小[|値]]を[変更|設定]する
'''

plt.ylim([最小値]_int_, [最大値]_int_)
'''
[グラフの|]縦軸の表示範囲を[変更|変更|調整]する
縦軸の[最大[|値]|最小[|値]]を[変更|設定]する
'''

目盛りの値リスト = []

plt.xticks(目盛りの値リスト)
'''
横軸の目盛[|り]の[表示|値|表示値]を変更する
'''

plt.yticks(目盛りの値リスト)
'''
縦軸の目盛[|り]の[表示|値|表示値]を変更する
'''

間隔 = 1

plt.xticks(np.arange([最小値]_int_, [最大値]_int_+1, 間隔))
'''
[|グラフの]横軸の目盛[|り]を設定する
横軸の目盛[|り]を整数[のみに|化]する
'''

plt.yticks(np.arange([最小値]_int_, [最大値]_int_+1, 間隔))
'''
[|グラフの]縦軸の目盛[|り]を設定する
縦軸の目盛[|り]を整数[のみに|化]する
'''

plt.xticks([0, 60, 90], ['不可', '可', '秀'])
'''
横軸の目盛[|り]を文字列に[変えたい|する|変更する]
'''

plt.yticks([0, 60, 90], ['不可', '可', '秀'])
'''
縦軸の目盛[|り]を文字列に[変えたい|する|変更する]
'''

plt.xticks([])
'''
[|グラフの]横軸の目盛[|り]を[非表示にする|表示し[|たく]ない]
'''

plt.yticks([])
'''
[|グラフの]縦軸の目盛[|り]を[表示し[たく|]ない|非表示にする]
'''

plt.xscale("log")
'''
[グラフの|]横軸を対数[スケール|目盛]に変更する
横軸の目盛[|り]を対数に変更する
'''

plt.yscale("log")
'''
[グラフの|]縦軸を対数[スケール|目盛]に変更する
縦軸の目盛[|り]を対数に変更する
'''

plt.minorticks_on()
'''
[グラフの|]補助目盛[|り]を有効にする
'''


plt.grid(True)
'''
@alt(入れたい|付けたい|加えたい|描画する|表示する)
@alt(グリッド|[グリッド|目盛り|目盛]線|格子|格子線)

{グラフに|[グリッド]を}入れたい
'''

plt.grid(False)
'''
{グラフから|[グリッド]を}[消す|表示しない]
'''

plt.grid(axis='x')
'''
横軸だけグリッドを[引く|入れたい]
'''

plt.grid(axis='y')
'''
縦軸だけグリッドを[引く|入れたい]
'''

plt.grid(color='#800080')
'''
グリッドの色を変更する
'''

plt.grid(linewidth=3.0)
'''
グリッド[の線|][の太さ|幅]を変更する
グリッド[の線|]を[太く|細く]する
'''

plt.grid(linestyle='--')
'''
グリッドの線[の種類|種|スタイル]を変更する
'''

plt.grid(alpha=0.5)
'''
グリッド[の線|]の透明度を変更する
グリッド[の線|]を半透明にする
'''


plt.legend()
'''
@alt(凡例|凡例|データラベル|補足|[簡単な|短い]説明)

{[グラフの|]|凡例を}表示する
'''

plt.legend(['(凡例A)', '(凡例B)'])
'''
[グラフに|]凡例を[加えたい|追記する]
'''

x, y = 0.5, 0.5

plt.legend(loc=(x, y))
'''
@alt(位置|場所)

[グラフの|]凡例の位置を指定する
[グラフの|]凡例の位置を(x, y)に設定する
{グラフ中の(x, y)の位置に|凡例を}表示する
'''

plt.legend(loc="best")
'''
{[最適な|ベストな|グラフに被らない]位置に|凡例を}表示する
'''

plt.legend(frameon=False)
'''
反例の枠を取りたい
{[グラフの中に|]|枠なしの凡例を}入れたい
'''


# プロット

データ列 = np.array([1, 2, 3])
[データ列]_ndarray_ = np.array([1, 2, 3])
[データ列]_ndarray_ = np.array([1, 2, 3])
[データ列]_DataFrame_[_ColumnName_]] = np.array([1, 2, 3])
[データ列]_DataFrame_[_ColumnName_]] = np.array([1, 2, 3])
df, column, column = {}, 'A', 'B'
'''
@poly([データ列]_DataFrame_[_ColumnName_]];[カラム名]_ColumnName_ _データ列_;[配列]_ndarray_;_list_;データフレームの[カラム|列] df['(列名)'])
@poly([データ列]_DataFrame_[_ColumnName_]];[カラム名]_ColumnName_ _データ列_;[配列]_ndarray_;_list_)
'''


plt.plot([データ列]_ndarray_, [データ列]_ndarray_)
'''
@alt(折れ線グラフ|線グラフ|[ライン|線])
@alt(と指定して|[と|に]して|[と|に]設定して)

折れ線グラフを描画する
{[データ列]_ndarray_を|折れ線グラフで}可視化する
'''

plt.plot([データ列]_DataFrame_[_ColumnName_]], [データ列]_DataFrame_[_ColumnName_]])
'''
[データ列]_DataFrame_[_ColumnName_]]と[データ列]_DataFrame_[_ColumnName_]]を折れ線グラフに[|描画]する
'''

plt.plot(range(len([データ列]_DataFrame_[_ColumnName_]])), [データ列]_DataFrame_[_ColumnName_]])
'''
@alt(推移|変遷|移り変わり|変化)

{[データ列]_DataFrame_[_ColumnName_]]の推移を|折れ線グラフで}可視化する
[データ列]_DataFrame_[_ColumnName_]]の推移を折れ線グラフにする
'''

plt.plot([データ列]_ndarray_, [データ列]_ndarray_, label='(説明)')
'''
@alt(説明|凡例|簡単な説明)

折れ線グラフの説明を設定する
折れ線グラフに説明を[付けたい|加えたい]
折れ線グラフを描画する。説明[付きで|を付けたい]
'''

plt.plot([データ列]_DataFrame_[_ColumnName_]], [データ列]_DataFrame_[_ColumnName_]], label='(説明)')
'''
[データ列]_DataFrame_[_ColumnName_]]と[データ列]_DataFrame_[_ColumnName_]]を折れ線グラフにする。説明を付けたい
'''

plt.scatter([データ列]_ndarray_, [データ列]_ndarray_, label='(説明)')
'''
散布図を描画する。説明を付けたい
'''

plt.plot([データ列]_ndarray_, [データ列]_ndarray_, color='#808080')
'''
@alt(カラーコード|RGB)

{折れ線グラフの色を|[カラーコードで|]}設定する
[[データ列]_ndarray_の|]折れ線グラフを描画する。{色を|[カラーコードで|]}設定する
'''

__線種__ = 'dashed'
'''
@poly(__線種__;補助線 "dashed";破線 "dashed";一点鎖線 "dashbot";点線 "dotted";実線 "solid")
'''

plt.plot([データ列]_ndarray_, [データ列]_ndarray_, linestyle=__線種__)
'''
{[データ列]_ndarray_を|__線種__の折れ線グラフで}描画する
{[データ列]_ndarray_を|折れ線グラフで}描画する。[線の種類|スタイル]は__線種__にする
'''

plt.axvline(x=0, linestyle=__線種__)
'''
{グラフに|[鉛直|縦][方向|]の__線種__を}[付けたい|加えたい]
'''

plt.axhline(y=0, linestyle=__線種__)
'''
{グラフに|[水平|横][方向|]の__線種__を}[付けたい|加えたい]
'''


# https://own-search-and-study.xyz/2016/08/08/matplotlib-pyplotのplotの全引数を使いこなす/


###


# linewidth = n
# '''
# ただし、[|グラフの]線幅をnに設定する
# '''

# plt.plot([データ列]_ndarray_, [データ列]_ndarray_, linewidth=n)
# '''
# 折れ線グラフの線幅を指定する
# 折れ線グラフの線幅をnに設定する
# 線幅nの折れ線グラフを描画する
# {xdataとydataで|折れ線グラフを}描画して、[その|]線幅をnに設定する
# '''

# plt.plot([データ列]_ndarray_, [データ列]_ndarray_, linestyle=__X__, linewidth=n)
# '''
# [__Y__グラフ|__Y__の折れ線グラフ]の線幅を指定する
# [__Y__グラフ|__Y__の折れ線グラフ]の線幅をnに設定する
# {[xdataとydataで|]|[__Y__グラフ|__Y__の折れ線グラフ]を}描画して、[その|]線幅をnに設定する
# '''

# plt.plot([データ列]_ndarray_, [データ列]_ndarray_, linestyle=__X__, color=rgb)
# '''
# [__Y__グラフ|__Y__の折れ線グラフ]の色をrgbに設定する
# xdataとydata[の|について]rgbの__Y__グラフを描画する
# {[xdataとydataで|]|[__Y__グラフ|__Y__の折れ線グラフ]を}描画して、[その|]線幅をnに設定する
# '''

# plt.plot([データ列]_ndarray_, [データ列]_ndarray_, linestyle=__X__, color='r')
# '''
# @alt(赤い|赤色の)
# 赤い[__Y__グラフ|__Y__の折れ線グラフ]を描画する
# [__Y__グラフ|__Y__の折れ線グラフ]の色を[赤にする|赤くする|赤色に設定する]
# {[xdataとydataで|]|[__Y__グラフ|__Y__の折れ線グラフ]を}描画して、[その|]線幅をnに設定する
# '''

# plt.plot([データ列]_ndarray_, [データ列]_ndarray_, linestyle=__X__, color='b')
# '''
# @alt(青い|青色の)
# 青い__Y__グラフを描画する
# __Y__グラフの色を[青にする|青くする|青色に設定する]
# xdataとydata[の|について]青い__Y__グラフを描画する
# xdataとydata[の|について]__Y__グラフを描画して、[その|]色を[青にする|青くする|青色に設定する]
# '''

# plt.plot([データ列]_ndarray_, [データ列]_ndarray_, linestyle=__X__, color='k')
# '''
# @test(plt=missing;xdata=ydata=aList;$$)
# @alt(黒い|黒色の)
# 黒い__Y__グラフを描画する
# __Y__グラフの色を[黒にする|黒くする|黒色に設定する]
# xdataとydata[の|について]黒い__Y__グラフを描画する
# xdataとydata[の|について]__Y__グラフを描画して、[その|]色を[黒にする|黒くする|黒色に設定する]
# '''


# 散布図

plt.scatter([データ列]_ndarray_, [データ列]_ndarray_)
'''
@alt(散らばり|相関|分布|関係性)

[[データ列]_ndarray_の|]散布図を描画する
[[データ列]_ndarray_の|]散らばりを可視化する
'''

plt.scatter([データ列]_DataFrame_[_ColumnName_]], [データ列]_DataFrame_[_ColumnName_]])
'''
[データ列]_DataFrame_[_ColumnName_]]と[データ列]_DataFrame_[_ColumnName_]]を散布図に[|描画|図示|プロット]する
'''

plt.scatter([データ列]_ndarray_, [データ列]_ndarray_, s=5)  # sはサイズ
'''
@alt(マーカーを大きくする|マーカの大きさを変更する)
[[データ列]_ndarray_の|]散布図を描画する。マーカーを大きくする
散布図のマーカーを大きくする
'''

plt.plot([データ列]_ndarray_, [データ列]_ndarray_, c='#800080')
'''
[[データ列]_ndarray_の|]散布図を描画する。色を変更する。
散布図の色を変更する。
'''


plt.plot([データ列]_ndarray_, [データ列]_ndarray_, marker=__X__)
'''
@test(plt=missing;xdata=ydata=aList;$$)
@X('.';'o';'^';'v';'<';'>';'x';'X';'s';'D';'*')
@Y(ポイント;丸;[[|上]三角|▲|△];[下三角|▽|▼];左三角;右三角;[バツ|クロス];大バツ;四角;[ダイアモンド|菱形];星)
{散布図に|__Y__マーカーを}使う
{__Y__マーカーで|散布図を}描画する
xdataとydata[について|の]散布図を描画して、マーカーを__Y__に設定する
xdataとydata[について|]の散布図に__Y__マーカーを描画する
'''


plt.plot([データ列]_ndarray_, [データ列]_ndarray_, marker=__X__, c='r')
'''
@test(plt=missing;xdata=ydata=aList;$$)
{散布図に|赤い__Y__マーカーを}使う
{赤い__Y__マーカーで|散布図を}描画する
{xdataとydata[について|]の散布図に|赤い__Y__マーカーを}描画する
'''

plt.plot([データ列]_ndarray_, [データ列]_ndarray_, marker=__X__, c='k')
'''
@test(plt=missing;xdata=ydata=aList;$$)
{散布図に|黒い__Y__マーカーを}使う
{黒い__Y__マーカーで|散布図を}描画する
{xdataとydata[について|]の散布図に|黒い__Y__マーカーを}描画する
'''


# https: // yyousuke.github.io/matplotlib/matplotlib.html

plt.scatter([データ列]_ndarray_, [データ列]_ndarray_, c=aList, cmap='Blues')
'''
aListに応じて、散布図の色を変えたい
xdataとydata[について|]aList[の値|]に応じて、散布図の色を変えたい
'''

plt.colorbar()
'''
@alt(縦向き|鉛直)
{カラーバーを|縦向き[で|に]}描画する
{カラーバーを|縦向き[で|に]}付けたい
'''

plt.colorbar(orientation='horizontal')
'''
@alt(横向き|水平)
{カラーバーを|横向き[で|に]}描画する
{カラーバーを|横向き[で|に]}付けたい
'''


# ヒストグラム

plt.hist([データ列]_ndarray_)
'''
@alt(ヒストグラム|ヒストグラム|[度数分布図|柱状図|柱状グラフ])

[[データ列]_ndarray_の|]ヒストグラムを描画する
[[データ列]_ndarray_の|]出現頻度を可視化する
{ヒストグラムで|[データ列]_ndarray_を}可視化する
[データ列]_ndarray_をヒストグラムにする
'''

plt.hist([データ列]_DataFrame_[_ColumnName_]])
'''
[データ列]_DataFrame_[_ColumnName_]]のヒストグラムを描画する
[データ列]_DataFrame_[_ColumnName_]]の出現頻度を可視化する
{ヒストグラムで|[データ列]_DataFrame_[_ColumnName_]]を}可視化する
[データ列]_DataFrame_[_ColumnName_]]をヒストグラムにする
'''

区関数 = 10

plt.hist([データ列]_ndarray_, bins=区関数)
'''
@alt(ビン数|ビン[|の数]|区間[数|の数|])

ヒストグラムのビン数を設定する
{ビン数を設定して|ヒストグラムを}描画する
ヒストグラムを描画して、ビン数を設定する
'''

start = 0
end = 100

plt.hist([データ列]_ndarray_, range=(start, end))
'''
@alt(範囲|区間|上限下限)

ヒストグラムの範囲を設定する
{ヒストグラムを|上限から下限[まで|]の範囲で}描画する
'''

plt.hist([データ列]_ndarray_, density=True)
'''
ヒストグラムの描画して、正規化する
正規化されたヒストグラムを描画する
ヒストグラムを描画し、合計を1にする
'''

plt.hist([データ列, _ndarray_], color=['b', 'r'])
'''
{ヒストグラムを|[２つ|横に]並べて}描画する
{[データ列]_ndarray_を|[２つ|横に]並べて}ヒストグラムにする
'''

# 箱ヒゲ図

plt.boxplot([データ列]_ndarray_)
'''
@alt(箱ひげ図|箱[髭|ヒゲ]図|ボックスチャート)

{[データ列]_ndarray_を|箱ひげ図で}描画する
[データ列]_ndarray_を箱ひげ図にする
{箱ひげ図で|[データ列]_ndarray_を}可視化する
[データ列]_ndarray_の[四分位|パーセンタイル]を可視化する
'''

plt.boxplot([データ列]_DataFrame_[_ColumnName_]])
'''
{[データ列]_DataFrame_[_ColumnName_]]を|箱ひげ図で}描画する
[データ列]_DataFrame_[_ColumnName_]]を箱ひげ図にする
{箱ひげ図で|[データ列]_DataFrame_[_ColumnName_]]を}可視化する
[データ列]_DataFrame_[_ColumnName_]]の[四分位|パーセンタイル]を可視化する
'''

plt.boxplot([[データ列]_DataFrame_[_ColumnName_]], [データ列]_DataFrame_[_ColumnName_]]], labels=['(解説)', '(解説2)'])
'''
{[データ列]_DataFrame_[_ColumnName_]]を|並べて}箱ひげ図にする
[２つの|複数の][データ列]_DataFrame_[_ColumnName_]]を[ひとつの|]箱ひげ図にする
'''

vert = False
'''
ただし、箱ひげ図を[水平方向|横[方向|向き]]にする
'''

plt.boxplot([データ列]_ndarray_, vert=False)
'''
箱ひげ図を横[方向|向き]にする
'''

showmeans = False
'''
ただし、[箱ひげ図に|]平均を[加えたい|追記する]
'''

plt.boxplot([データ列]_ndarray_, showmeans=True)
'''
箱ひげ図を描画して、平均[値|]を[加えたい|追加する]
平均[値|]付き箱ひげ図を描画する
'''

plt.boxplot([データ列]_ndarray_, meanline=True)
'''
箱ひげ図を描画して、平均線を[加えたい|追加する]
平均線付き箱ひげ図を描画する
'''


# 棒グラフ

ラベル列 = ['A', 'B', 'C']
データ列 = [10, 8, 6]
plt.bar(ラベル列, _ndarray_)
'''
@alt(縦棒グラフ|棒グラフ|[縦向き|縦方向の|鉛直|垂直]棒グラフ)

縦棒グラフを描画する
[データ列]_ndarray_を縦棒グラフにする
'''

ラベル列 = ['A', 'B', 'C']
データ列 = [10, 8, 6]
plt.barh(ラベル列, _ndarray_)
'''
@alt(横棒グラフ|横[向き|方向の]棒グラフ|[水平|平行][な|]棒グラフ)

横棒グラフを描画する
[データ列]_ndarray_を横棒グラフにする
'''

plt.bar(ラベル列, [データ列]_DataFrame_[_ColumnName_]])  # ラベル列と[データ列]_DataFrame_[_ColumnName_]]は同じサイズ
'''
{[データ列]_DataFrame_[_ColumnName_]]を|縦棒グラフとして}可視化する
'''

plt.barh(ラベル列, [データ列]_DataFrame_[_ColumnName_]])  # ラベル列と[データ列]_DataFrame_[_ColumnName_]]は同じサイズ
'''
{[データ列]_DataFrame_[_ColumnName_]]を|横棒グラフとして}可視化する
'''


plt.bar(ラベル列, _ndarray_, bottom=[データ列]_ndarray_, color='#800080')
'''
縦棒グラフを積み上げにする
積み上げ棒グラフを描画する
'''

plt.barh(ラベル列, _ndarray_, bottom=[データ列]_ndarray_, color='#800080')
'''
横棒グラフを積み上げにする
積み上げ横棒グラフを描画する
'''

plt.bar(ラベル列, _ndarray_, width=0.5)
'''
縦棒グラフを描画して、[バー|棒]の[横|]幅を[調整する|設定する]
棒グラフの[横|]幅を[調整する|設定する]
'''

plt.barh(ラベル列, _ndarray_, width=0.5)
'''
横棒グラフを描画して、[バー|棒]の[縦|]幅を[調整する|設定する]
横棒グラフの[縦|]幅を[調整する|設定する]
'''

plt.bar(ラベル列, _ndarray_, align='center')
'''
@alt(中央寄せ|センタリング)
縦棒グラフを描画して、[ラベルを|]中央寄せする
'''

plt.barh(ラベル列, _ndarray_, align='center')
'''
横棒グラフを描画して、[ラベルを|]中央寄せする
'''

plt.bar(ラベル列, _ndarray_, align='edge')
'''
縦棒グラフを描画して、[ラベルを|]左寄せする
'''

plt.barh(ラベル列, _ndarray_, align='edge')
'''
横棒グラフを描画して、[ラベルを|]下寄せする
'''

plt.bar(ラベル列, _ndarray_, color=rgb)
'''
{棒グラフの色を|[rgbに|]}設定する
'''

plt.barh(ラベル列, _ndarray_, color=rgb)
'''
{横棒グラフの色を|[rgbに|]}設定する
'''

# 円グラフ

plt.pie([データ列]_ndarray_, startangle=90)
'''
[データ列]_ndarray_を円グラフにする
'''

plt.pie([データ列]_DataFrame_[_ColumnName_]], startangle=90)
'''
[データ列]_DataFrame_[_ColumnName_]]を円グラフにする
'''

plt.pie([データ列]_ndarray_, startangle=90, autopct='%.2f%%')
'''
{円グラフに|[割合|パーセント|百分率]を}[表示する|加えたい]
{円グラフで|[データ列]_ndarray_の[割合|比率|パーセント]を}可視化する
'''

plt.pie([データ列]_DataFrame_[_ColumnName_]], startangle=90, autopct='%.2f%%')
'''
{円グラフに|[割合|パーセント|百分率]を}[表示する|加えたい]
{円グラフで|[データ列]_DataFrame_[_ColumnName_]]の[割合|比率|パーセント]を}可視化する
'''

plt.pie([データ列]_ndarray_, startangle=90, labels=ラベル列)
'''
円グラフにラベルを付けたい
ラベル付きの円グラフを描画する
'''

plt.pie([データ列]_ndarray_, startangle=90, counterclock=False)
'''
{円グラフを|時計回りに}描画する
'''

plt.pie([データ列]_ndarray_, startangle=90, explode=[0, 0.3, 0])
'''
円グラフの特定の要素[だけ|を][切り出する|目立たせたい]
'''

plt.axis("equals")
'''
[グラフを|作画を]正方形にする
円グラフを[真円|[正|完全な|きれいな|正確な]円]にする
[グラフの|作画の|][x軸とy軸|縦横]の比率を[同じに|等しく]する
[グラフの|作画の|]縦横比を[等しく|同じに]する
'''

plt.savefig('file.png')
'''
{グラフを|[画像|PNG]ファイル[として|に]}[保存|出力]する
'''

plt.show()
'''
グラフを表示する
'''
import matplotlib
import matplotlib.pyplot as plt

[データ列]_DataFrame_[_ColumnName_]] = [1, 2, 3]
[データ列]_DataFrame_[_ColumnName_]] = [2, 3, 4]
__色名__ = "blue"
__色名2__ = "blue"
__色名3__ = "blue"
__和色名__ = "blue"
'''
@poly(__色名__;青 "blue";緑 "green";赤 "red";シアン "cyan";マゼンタ "magenta";黄 "yellow";黒 "black";白 "white")
@poly(__色名2__;[水|海|アクア] 'aqua';[青|蒼|ブルー] 'blue';[青紫|ブルーバイオレット] 'blueviolet';[茶|褐|ブラウン] 'brown';ベージュ 'beige';[黒|ブラック] 'black';[黄金|ゴールド] 'gold';[鼠|ねずみ|グレー|灰] 'gray';[緑|グリーン] 'green';[黄緑|グリーンイエロー] 'greenyellow';マゼンタ 'magenta';[橙|オレンジ] 'orange';[桃|石竹|撫子|ピンク] 'pink';[紫|パープル] 'purple';[赤] 'red';[白|ホワイト] 'white';[銀|シルバー] 'silver';[空|スカイブルー] 'skyblue';[黄|イエロー] 'yellow';[黄緑|イエローグリーン] 'yellowgreen';[桜|さくら] "#feeeed")
@poly(__和色名__;[桜|さくら] "#feeeed";藍 "#165e83";青緑 "#0090a8";青紫 "#6f51a1";[茜|赤褐] "#b13546";赤紫 "#eb6ea5";灰汁 "#bcb09c";浅黄 "#ffcc33";浅葱 "#00a4ac";浅緑 "#9bcf97";小豆 "#98514b";杏 "#f4a466";苺 "#bb5561";鶯 "#918d40";柿 "#ed6d3d";黄 "#ffd400";桔梗 "#6a4c9c";紅 "#c22047";群青 "#465daa";焦茶 "#6a4d32";朱 "#ef454a";真紅 "#b1063a";墨 "#343434";深緑 "#004025";藤 "#afb4db";萌葱 "#006c4f";山吹 "#f8b400";若草 "#abc900")
@poly(__色名3__;アクアマリン 'aquamarine';[琥珀|アンバー] "#b97e54";[紺碧|アジュール] 'azure';チョコレート 'chocolate';[コーラル|珊瑚] 'coral';[クリムゾン|真紅|深紅] 'crimson';シアン 'cyan';[ディープ|濃い]ピンク 'deeppink';[煉瓦|レンガ] 'firebrick';ホットピンク 'hotpink';[藍|インディゴ] 'indigo';[象牙|アイボリー] 'ivory';[国防|砂|黄土|カーキ] 'khaki';ラベンダー 'lavender';ライム[|グリーン] 'limegreen';ミッドナイトブルー 'midnightblue';ネイビー[|ブルー] 'navy';オリーブ 'olive';[赤橙|オレンジレッド] 'orangered';オーキッド 'orchid';オフホワイト "#fff9ee";ロイヤルブルー 'royalblue';サーモン[|ピンク] 'salmon';[牡蠣|貝殻] 'seashell';[雪|スノー] 'snow';[春|スプリンググリーン] 'springgreen';[タン|淡い茶色] 'tan';[青緑|ティール] 'teal';トマト 'tomato';[ターコイズ|青緑] 'turquoise';[菫|スミレ|バイオレット] 'violet';小麦 'wheat';ホワイトスモーク 'whitesmoke';サファイア "#0054a6";[珊瑚|コーラルレッド] "#f8a7a0";[紫紺|紫根] "#411445";シグナルレッド "#EF4050";セピア "#6b4a2b";[ブロンズ|青銅] "#9a6229";[栗|マルーン] 'maroon';[緋|スカーレット|アカネ] "#da523a";[翡翠|ヒスイ] "#3f9877";[向日葵|ヒマワリ|ひまわり] "#ffc20e";[薔薇|ばら|ローズ] "#f0566e";[乳白|ミルキーホワイト|牛乳] "#fffef6";茄子紺 #451F49;チャコールグレ[イ|ー] "#4c444d";[萌黄|もえぎ] "#a9d159";[赤ワイン|ワインレッド|葡萄] "#8d3043";[瑠璃|ラピスラズリ] "#426ab3")
'''

matplotlib.colors.cnames
'''
@alt(matplotlibで|)
@alt(色の名前|色)
matplotlibで[使える|利用可能な]色の名前の一覧
色の名前とカラーコード[の[対応表|一覧]]
'''

色名 = 'red'

matplotlib.colors.cnames[色名]
'''
色の名前からカラーコード
色の名前からコードに変換する
'''

# アルファ値

alpha = 0.5
'''
@alt(透明度|アルファ[|値])

<option>[色を|表示を|]半透明にする
<option>色の透明度を設定する
'''

color = __色名__
'''
<option>色は__色名__
<option>__色名__[色|]を使用する
'''

color = __色名2__
'''
<option>色は__色名2__
<option>__色名2__色を使用する
'''

color = __色名3__
'''
<option>色は__色名3__
<option>__色名3__色を使用する
'''

color = __和色名__
'''
<option>色は__和色名__[色|]
<option>__和色名__色を使用する
'''

markerfacecolor = __色名__
'''
<option>マーカーの色は__色名__
<option>マーカーは__色名__色
'''

markerfacecolor = __色名2__
'''
<option>マーカーの色は__色名2__
<option>マーカーは__色名2__色
'''

markerfacecolor = __和色名__
'''
<option>マーカーの色は__和色名__[|色]
<option>マーカーは__和色名__色
'''

plt.plot([データ列]_DataFrame_[_ColumnName_]], [データ列]_DataFrame_[_ColumnName_]], alpha=0.5)
'''
折れ線グラフの透明度を設定する
折れ線グラフを半透明にする
'''

plt.hist([データ列]_DataFrame_[_ColumnName_]], alpha=0.5)
'''
ヒストグラムを半透明[に|化]する
ヒストグラムを描画して、半透明[に|化]にする
'''

plt.plot([データ列]_DataFrame_[_ColumnName_]], [データ列]_DataFrame_[_ColumnName_]], color=__色名__)
'''
[折れ|]線グラフの色を__色名__に設定する
__色名__色の[|折れ]線グラフを描画する
{[折れ|]線グラフを|__色名__色で_}描画する
'''

plt.hist([データ列]_DataFrame_[_ColumnName_]], color=__色名__)
'''
{ヒストグラムの色を|__色名__に}設定する
__色名__色のヒストグラムを描画する
{ヒストグラムを|__色名__色で_}描画する
'''

plt.scatter([データ列]_DataFrame_[_ColumnName_]], [データ列]_DataFrame_[_ColumnName_]], color=__色名__)
'''
散布図の色を__色名__にする
__色名__色の散布図を描画する
{散布図を|__色名__色で_}描画する
'''

plt.scatter([データ列]_DataFrame_[_ColumnName_]], [データ列]_DataFrame_[_ColumnName_]], color=__和色名__)
'''
散布図を__和色名__[|色]にする
'''

plt.bar([データ列]_DataFrame_[_ColumnName_]], [データ列]_DataFrame_[_ColumnName_]], color=__色名__)
'''
[|縦]棒グラフの色を__色名__にする
__色名__色の[|縦]棒グラフを描画する
{[|縦]棒グラフを|__色名__色で_}描画する
'''

plt.bar([データ列]_DataFrame_[_ColumnName_]], [データ列]_DataFrame_[_ColumnName_]], color=__色名2__)
'''
[|縦]棒グラフを__色名2__[|色]にする
'''

plt.barh([データ列]_DataFrame_[_ColumnName_]], [データ列]_DataFrame_[_ColumnName_]], color=__色名__)
'''
横棒グラフの色を__色名__にする
__色名__色の横棒グラフを描画する
{横棒グラフを|__色名__色で_}描画する
'''

plt.bar([データ列]_DataFrame_[_ColumnName_]], [データ列]_DataFrame_[_ColumnName_]], color=__色名3__)
'''
横棒グラフを__色名3__[|色]にする
'''

_ = None


plt.hist([データ列]_DataFrame_[_ColumnName_]], alpha=_, color=_)
'''
ヒストグラムを描画する
'''
import numpy as np
import matplotlib.pyplot as plt
'''
@alt(描画する|書きたい)
@alt(可視化する|[作図する|図示する]|描画する)
@alt([データ列]_ndarray_=[データ列|[リスト|配列]|[数列|イテラブル]])
@alt(推移|変遷|移り変わり|変化)

@alt(折れ線グラフ|折れ線グラフ|線グラフ|[ライン|線])

'''

データ列 = np.array([1, 2, 3])
[データ列]_ndarray_ = np.array([1, 2, 3])
[データ列]_ndarray_ = np.array([2, 3, 4])

__線種__ = 'dashed'
'''
@poly(__線種__;破線 "dashed";一点鎖線 "dashbot";点線 "dotted";実線 "solid")
@alt(に設定する|[に|と]する|に[セット|指定]する|に変更する|に変えたい)
'''

__赤い__ = 'r'
__赤く__ = 'r'
'''
@poly(__赤い__;赤い "r";青い "b";黒い "k";白い "w";黄色い "y")
@poly(__赤く__;赤く "r";青く "b";黒く "k";白く "w";黄色く "y")
'''


linestyle = __線種__
'''
@alt(ラインスタイル|線[|の][種類|スタイル])

ただし、グラフ[の種類|]を__線種__に設定する
ただし、[|グラフの]ラインスタイルを__線種__に設定する
'''

linewidth = 3.0  # 単位はポイント
'''
@alt(線幅=[線の幅|線幅])

ただし、[|グラフの]線幅を[3.0ポイントに|]設定する
ただし、[線|ライン]を[太く|細く]する
'''

plt.grid(linestyle=__線種__)
'''
グリッドを__線種__にする
グリッドのラインスタイルを__線種__に変更する
'''

plt.plot([データ列]_ndarray_, [データ列]_ndarray_, linestyle=__線種__)
'''
{折れ線グラフ[のラインスタイル|]を|__線種__に}設定する
{折れ線グラフを|__線種__で_}描画する
{__線種__で_|[データ列]_ndarray_の推移を}描画する
__線種__[|の折れ線]グラフを描画する
'''

plt.plot([データ列]_ndarray_, [データ列]_ndarray_, linestyle=__線種__, color=__赤い__)
'''
{折れ線グラフを|__赤い____線種__で_}描画する
{__赤い____線種__で_|[データ列]_ndarray_の推移を}描画する
'''

plt.plot([データ列]_ndarray_, [データ列]_ndarray_, linestyle=__線種__, alpha=0.5)
'''
{折れ線グラフを|半透明の__線種__で_}描画する
{半透明の__線種__で_|[データ列]_ndarray_の推移を}描画する
'''

plt.hist([データ列]_ndarray_, linestyle=__線種__)
'''
{ヒストグラム[のラインスタイル|]を|__線種__に}設定する
{ヒストグラムを|__線種__で_}描画する
'''
# 整数

[整数]_int_ = 2
[整数]_int_ = 2
[整数]_int_ = 2
'''
@poly([整数]_int_;_int_;_実数_)
@poly([整数]_int_;_int_;_実数_)
'''

[整数]_int_ + [整数]_int_
'''
@alt(求めたい|計算する)

[足し算する|加算する]
[整数]_int_に[整数]_int_を[加えたい|加算する]
[整数]_int_[プラス|足す|＋][整数]_int_
[二つの|][整数]_int_の和
'''

[整数]_int_ - [整数]_int_
'''
[引き算する|減算する]
[整数]_int_から[整数]_int_を[引きたい|減算する]
[整数]_int_[マイナス|引く|ー][整数]_int_
[二つの|][整数]_int_の差
'''

[整数]_int_ * [整数]_int_
'''
[掛け算する|掛算する|乗算する|積]
[整数]_int_に[整数]_int_を[かけたい|掛けたい]
[整数]_int_[かける|掛ける|×][整数]_int_
'''

[整数]_int_ / [整数]_int_
'''
[割り算|徐算|割算]する
[整数]_int_を[整数]_int_で[割りたい|わりたい]
[整数]_int_[わる|割る|÷][整数]_int_
[二つの|][整数]_int_の商
'''

[整数]_int_ // [整数]_int_
'''
整数で[割り算|徐算|割算]する
[整数]_int_を[整数]_int_で割って[小数点以下|その結果]を切り捨てたい
[整数]_int_を[|[整数]_int_で]整数除算する
'''

[整数]_int_ % [整数]_int_
'''
[整数]_int_を[整数]_int_で割った[余り|モジュロ|剰余|mod]
[整数の|][割り算の余り|モジュロ]
'''

[整数]_int_ ** _int_
'''
[整数]_int_の_int_乗
'''

[整数]_int_ / _int_
'''
[整数]_int_の_int_分の[一|1]
'''


# 比較演算子

[整数]_int_ == [整数]_int_
'''
@alt(かどうか|か知りたい|か[調べたい|判定する])
@alt(数値同士が|２つの数値が|[整数]_int_と[整数]_int_が)

数値同士が[等しい|同じ値]かどうか
[整数]_int_[が|は][整数]_int_と等しいかどうか
[整数]_int_[が|は][整数]_int_かどうか
'''

[整数]_int_ > [整数]_int_
'''
[整数]_int_[が|は][整数]_int_より大きいかどうか
[整数]_int_[が|は][整数]_int_よりも大きいかどうか
'''

[整数]_int_ < [整数]_int_
'''
[整数]_int_[が|は][整数]_int_より小さいかどうか
[整数]_int_[が|は][整数]_int_よりも小さいかどうか
'''

[整数]_int_ >= [整数]_int_
'''
[整数]_int_[が|は][整数]_int_以上かどうか
'''

[整数]_int_ <= [整数]_int_
'''
[整数]_int_[が|は][整数]_int_以下かどうか
'''

[整数]_int_ < [整数]_int_ or [整数]_int_ >= n3
'''
[整数]_int_[が|は][整数]_int_未満、[または|もしくは|それか]n3以上かどうか
'''

[整数]_int_ <= [整数]_int_ or [整数]_int_ >= n3
'''
[整数]_int_[が|は][整数]_int_以下、[または|もしくは|それか]、n3以上かどうか
'''

[整数]_int_ <= [整数]_int_ and [整数]_int_ <= n3
'''
[整数]_int_がn以上、かつ、n3以下かどうか
'''

[整数]_int_ < [整数]_int_ and [整数]_int_ < n3
'''
[整数]_int_がnより大きく、かつ、n3[未満|より小さい]かどうか
'''

[整数]_int_ % 2 == 0
'''
[整数]_int_[が|は]偶数かどうか
'''

[整数]_int_ % 2 == 1
'''
[整数]_int_[が|は]奇数かどうか
'''

[整数]_int_ % _int_ == 0
'''
[整数]_int_[が|は]_int_の倍数かどうか
[整数]_int_[が|は]_int_で割り切れるかどうか
'''

if [整数]_int_ % _int_ == 0:
    print([整数]_int_, _int_)
'''
[整数]_int_[が|は]_int_の倍数のとき、
'''

[整数]_int_ % [整数]_int_ != 0
'''
[整数]_int_[が|は][整数]_int_の倍数でないかどうか
[整数]_int_[が|は][整数]_int_で割り切れないかどうか
'''

if [整数]_int_ % _int_ != 0:
    print([整数]_int_, _int_)
'''
[整数]_int_[が|は]_int_の倍数でないとき、
'''

[整数]_int_ > 0
'''
[整数]_int_[が|は]正の[数|整数]かどうか
'''

[整数]_int_ >= 0
'''
[整数]_int_[が|は]非負数でないかどうか
'''

[整数]_int_ < 0
'''
[整数]_int_[が|は]負の[数|整数]かどうか
'''

- 9 <= [整数]_int_ <= 9
'''
[整数]_int_[が|は]一桁の[数|整数]かどうか
[整数]_int_[が|は]-9以上、9以下かどうか
'''

0 <= [整数]_int_ <= 9
'''
[整数]_int_[が|は]一桁の[数|整数]かどうか
'''

[整数]_int_ in _list_
'''
[整数]_int_[が|は][リスト|タプル]_list_の[どれか|いづれか|一つ[|である]]かどうか
'''

[整数]_int_ in ([整数]_int_, [整数]_int_)
'''
[整数]_int_[が|は][整数]_int_、もしくは[整数]_int_かどうか
'''

[整数]_int_ in ([整数]_int_, [整数]_int_, [整数]_int_)
'''
[整数]_int_[が|は][整数]_int_、もしくは[整数]_int_、もしくは[整数]_int_に等しいかどうか
'''
# 整数

n = 2
_str_ = '1101'
[整数]_int_ = 2
[整数]_int_ = 2

int(_str_, 10)
'''
@alt(に変換する|[化|に]する)
_str_を整数に変換する
'''

int(_str_, 2)
'''
{_str_を|[２|二]進数として}整数に変換する
'''

int(_str_, 8)
'''
{_str_を|[８|八]進数として}整数に変換する
'''

int(_str_, 16)
'''
{_str_を|[１６|十六]進数として}整数に変換する
'''

int(_str_, n)
'''
{_str_を|n進数として}整数に変換する
'''

バイト数 = 8

int(_str_, 16).to_bytes(length=バイト数, byteorder='big')
'''
@alt(バイト列|バイナリ)
@alt(進数表現|進数表記)

[１６|十六]進数表現[の_str_|]をバイト列に変換する
'''

int(_str_, 2).to_bytes(length=バイト数, byteorder='big')
'''
@alt(バイト列|バイナリ)

[２|二]進数表現[の_str_|]をバイト列に変換する
'''

bin(_int_)
'''
[整数]_int_を[２|二]進数表現[|の文字列]に変換する
'''

oct(_int_)
'''
[整数]_int_を[８|八]進数表現[|の文字列]に変換する
'''

hex(_int_)
'''
[整数]_int_を[１６|十六]進数表現[|の文字列]に変換する
'''

[整数]_int_.bit_length()
'''
@alt(|を調べたい|)

[整数]_int_のビット長[|]
'''

(_int_.bit_length() + 7) // 8
'''
@alt(|を調べたい|)

[整数]_int_のビット長[|]
'''

[整数]_int_.to_bytes((_int_.bit_length() + 7) // 8, byteorder='big')
'''
[整数]_int_をバイト列に変換する
'''

[整数]_int_.to_bytes((_int_.bit_length() + 7) // 8, byteorder='big', signed=True)
'''
{_int_を|符号付きで}バイト列に変換する
'''

[整数]_int_.to_bytes(length=バイト数, byteorder='big')
'''
{_int_を|[|符号なしで]}バイト列に変換する
'''

[整数]_int_.to_bytes(length=バイト数, byteorder='big', signed=True)
'''
{_int_を|符号付きで}バイト列に変換する
'''

[整数]_int_ + _int_
'''
@alt(求めたい|計算する)

[足し算する|加算する]
[整数]_int_に_int_を[加えたい|加算する]
[整数]_int_[プラス|足す|＋]_int_
[二つの|]整数の和
'''

[整数]_int_ - _int_
'''
[引き算する|減算する]
[整数]_int_から_int_を[引きたい|減算する]
[整数]_int_[マイナス|引く|ー]_int_
[二つの|]整数の差
'''

[整数]_int_ * _int_
'''
[掛け算する|掛算する|乗算する]
[整数]_int_に_int_を[かけたい|掛けたい]
[整数]_int_[かける|掛ける|×]_int_
[二つの|]整数の積
'''

[整数]_int_ / _int_
'''
[割り算|徐算|割算]する
[整数]_int_を_int_で[割りたい|わりたい]
[整数]_int_[わる|割る|÷]_int_
[二つの|]整数の商
'''

[整数]_int_ // _int_
'''
整数で[割り算|徐算|割算]する
[整数]_int_を_int_で割って[小数点以下|その結果]を切り捨てたい
[整数]_int_を[|_int_で]整数除算する
'''

[整数]_int_ % _int_
'''
[整数]_int_を_int_で割った[余り|モジュロ|剰余|mod]
[整数の|][割り算の余り|モジュロ]
'''

(_int_ + _int_ - 1) // _int_
'''
[整数]_int_を_int_で割って[小数点以下|その結果]を切り上げたい
整数[除算|割り算]の切り上げ
'''


__X__ = 2
'''
@X(2;3;4;5;8;n)
@Y([二|2];[三|3];[四|4];[五|5];[八|8];n)
'''

[整数]_int_ ** __X__
'''
整数の__Y__乗
'''

[整数]_int_ / __X__
'''
整数の__Y__分の[一|1]
'''

# ビット演算

[整数]_int_ & _int_
'''
@alt(整数同士の||２つの整数の|_int_と_int_の)
整数同士の[論理|ビット]積
'''

[整数]_int_ | _int_
'''
整数同士の[論理|ビット]和
'''

[整数]_int_ ^ _int_
'''
整数同士の[排他的論理和|XOR]
'''

[整数]_int_ << n
'''
整数を[nだけ|]左シフトする
整数の左シフト
'''

[整数]_int_ >> n
'''
整数を[nだけ|]右シフトする
整数の右シフト
'''

# 比較演算子

[整数]_int_ == _int_
'''
@alt(かどうか|か知りたい|か[調べたい|判定する])
@alt(整数同士が|２つの整数が|_int_と_int_が)

整数同士が[等しい|同じ値]かどうか
[整数]_int_[が|は]_int_と等しいかどうか
[整数]_int_[が|は]_int_かどうか
'''

[整数]_int_ > _int_
'''
[整数]_int_[が|は]_int_より大きいかどうか
[整数]_int_[が|は]_int_よりも大きいかどうか
'''

[整数]_int_ < _int_
'''
[整数]_int_[が|は]_int_より小さいかどうか
[整数]_int_[が|は]_int_よりも小さいかどうか
'''

[整数]_int_ >= _int_
'''
[整数]_int_[が|は]_int_以上かどうか
'''

[整数]_int_ <= _int_
'''
[整数]_int_[が|は]_int_以下かどうか
'''

[整数]_int_ < _int_ or _int_ >= n3
'''
[整数]_int_[が|は]_int_未満、[または|もしくは|それか]n3以上かどうか
'''

[整数]_int_ <= _int_ or _int_ >= n3
'''
[整数]_int_[が|は]_int_以下、[または|もしくは|それか]、n3以上かどうか
'''

[整数]_int_ <= _int_ and _int_ <= n3
'''
[整数]_int_がn以上、かつ、n3以下かどうか
'''

[整数]_int_ < _int_ and _int_ < n3
'''
[整数]_int_がnより大きく、かつ、n3[未満|より小さい]かどうか
'''

[整数]_int_ % 2 == 0
'''
[整数]_int_[が|は]偶数かどうか
[整数]_int_[が|は]2で割り切れるかどうか
'''

[整数]_int_ % 2 == 1
'''
[整数]_int_[が|は]奇数かどうか
[整数]_int_[が|は]2で割り切れないかどうか
'''

[整数]_int_ % 3 == 0
'''
[整数]_int_[が|は]3の倍数かどうか
[整数]_int_[が|は]3で割り切れるかどうか
'''

[整数]_int_ % 5 == 0
'''
[整数]_int_[が|は]5の倍数かどうか
[整数]_int_[が|は]5で割り切れるかどうか
'''

[整数]_int_ % _int_ == 0
'''
[整数]_int_[が|は]_int_の倍数かどうか
[整数]_int_[が|は]_int_で割り切れるかどうか
'''

[整数]_int_ % _int_ != 0
'''
[整数]_int_[が|は]_int_の倍数でないかどうか
[整数]_int_[が|は]_int_で割り切れないかどうか
'''

[整数]_int_ > 0
'''
[整数]_int_[が|は]正の[数|整数]かどうか
'''

[整数]_int_ >= 0
'''
[整数]_int_[が|は]非負数でないかどうか
'''

[整数]_int_ < 0
'''
[整数]_int_[が|は]負の[数|整数]かどうか
'''

- 9 <= _int_ <= 9
'''
[整数]_int_[が|は]一桁の[数|整数]かどうか
[整数]_int_[が|は]-9以上、9以下かどうか
'''

0 <= _int_ <= 9
'''
[整数]_int_[が|は]一桁の[数|整数]かどうか
'''

[整数]_int_ in _list_
'''
[整数]_int_[が|は][リスト|タプル]_list_の[どれか|いづれか|一つ[|である]]かどうか
'''

[整数]_int_ == 1 or _int_ == 2
'''
[整数]_int_[が|は]1、もしくは2かどうか
'''

[整数]_int_ == 1 or _int_ == 2 or _int_ == 3
'''
[整数]_int_[が|は]1、もしくは2、もしくは3に等しいかどうか
'''

len(str(_int_))
'''
[整数]_int_の桁数
整数[が|は]何桁[|になる]か知りたい
'''

sum(map(int, str(_int_)))
'''
@alt(総和|和)

[整数]_int_の[各|それぞれの]桁の総和[||]
'''
import numpy as np
'''
@alt(配列|行列|ベクトル)
@alt(作成する=[作成する|作成する|初期化する])
@alt(求める=[求める|[計算|算出]する|[得る|調べる]])

@alt(要素ごと|各要素)

ベクトル[の|][演算|計算]を[する|行う]
行列[の|][演算|計算]を[する|行う]
numpyを[使う|入れる|インポートする]
'''

[配列]_ndarray_ = np.array([1, 2, 3, 4])
[行列]_ndarray_ = np.array([[1, 2], [3, 4]])
[配列]_ndarray_ = _list_
_list_ = [1, 2]
n = 3

要素数 = 3
行数 = 2
列数 = 2
初期値 = 0
行番号 = 0
列番号 = 0

N = 10
[開始値]_int_ = 0
[終了値]_int_ = 10
[等差]_int_ = 2

[行列 | 配列]_ndarray_ = [配列]_ndarray_
'''
@poly([行列|配列]_ndarray_;[配列]_ndarray_;[行列]_ndarray_)
'''

__D型__ = np.int

dtype = __D型__
'''
@poly(__D型__;整数 np.int;８ビット整数 np.int8;符号なし８ビット整数 np.uint8;３２ビット整数 np.int32;[ブール|論理値] bool;複素数 complex)

<option>データ型は__D型__
<option>[|データ型として]__D型__を使う
'''

np.array(_list_)
'''
_list_を配列に変換する
{[リスト]_list_から|配列を}作成する
'''

np.array(_list_)
'''
_list_を配列に変換する
{[リスト]_list_から|配列を}作成する
'''

np.zeros(要素数)
'''
{全要素が|0で}初期化した配列
ゼロ埋めされた配列
'''

np.zeros(要素数, dtype=__D型__)
'''
{ゼロ埋めされた|__D型__型の}配列
'''

np.zeros(行数, 列数)
'''
{全要素を|０で}初期化した行列
ゼロ埋めされた行列
'''

np.zeros(行数, 列数, dtype=__D型__)
'''
{{全要素を|０で}初期化した|__D型__型の}行列
'''

np.ones(要素数, dtype=np.int)
'''
{全要素を|1で}初期化した配列
要素が全て1の配列
'''

np.ones(行数, 列数, dtype=np.int)
'''
{全要素を|1で}初期化した行列
全要素が1の行列
'''

np.full(要素数, 初期値, dtype=np.int)
'''
{全要素を|初期値で}初期化した配列
要素が全て初期値の配列
'''

np.full((行数, 列数), 初期値, dtype=np.int)
'''
{全要素を|初期値で}初期化した行列
全要素が初期値の行列
'''

np.eye(行数, 列数)
'''
単位行列
'''

np.identity(n)
'''
[単位正方行列|正方単位行列]
'''

np.empty(要素数, dtype=np.int)
'''
未初期化の配列
'''

np.empty((行数, 列数), dtype=np.int)
'''
未初期化の行列
'''

np.empty_like([配列]_ndarray_)
'''
[配列]_ndarray_と同じ大きさの[空配列|空の配列]を作成する
'''

np.arange(_int_)
'''
[0から|]_int_未満までの配列
'''

np.arange(1, _int_+1)
'''
1から_int_までの配列
'''

np.arange([開始値]_int_, [終了値]_int_, [等差]_int_)
'''
[連続した|連番の]配列の[自動|]作成する
等間隔の配列[を作成する＼]
[等差]_int_数列を配列に変換する
'''

np.linspace([最小値]_int_, [最大値]_int_, 要素数)
'''
[最大最小|範囲|区間]から配列
'''

np.random.random(N)
'''
乱数[で要素を埋めた|の]配列
'''

np.random.random((行数, 列数))
'''
乱数[の|で要素を埋めた]行列
'''

np.random.randint([開始値]_int_, [終了値]_int_, N)
'''
整数乱数[で要素を埋めた|の]配列
'''

np.random.randint([開始値]_int_, [終了値]_int_, (行数, 列数))
'''
整数乱数[で要素を埋めた|の]行列
'''


[配列]_ndarray_.reshape(行数, 列数)
'''
[配列]_ndarray_[の[次元|形状]|]を変形する
'''

[配列]_ndarray_.reshape(-1, 1)
'''
[配列]_ndarray_を[2次元1列|縦ベクトル]に変形する
'''

[配列]_ndarray_.reshape(1, -1)
'''
[配列]_ndarray_を[2次元1行|横ベクトル]に変形する
'''

np.zeros_like([配列]_ndarray_)
'''
@alt(ベースに=[元に|ベースに][|して])

[既存の|][配列]_ndarray_をベースに全要素が0の配列
'''

np.ones_like([配列]_ndarray_)
'''
[既存の|][配列]_ndarray_をベースに全要素が1の配列
'''

np.full_like([配列]_ndarray_, 初期値)
'''
[既存の|][配列]_ndarray_をベースに全要素が初期値の配列
'''

指定の値 = 0

[配列]_ndarray_[: , : ] = 指定の値
'''
[配列]_ndarray_の全要素の値を変更する
[配列]_ndarray_の全要素を指定の値にする
'''

[配列]_ndarray_[行番号, 列番号]
'''
[行列|配列]_ndarray_の値[|を得る]
'''

[配列]_ndarray_[行番号, 列番号] = 指定の値
'''
[行列|配列]_ndarray_の値を変更する
'''

[配列]_ndarray_[行番号]
'''
[行列|配列]_ndarray_の行[|を選択する]
'''

[配列]_ndarray_[:, 列番号]
'''
[行列|配列]_ndarray_の列[|を選択する]
'''

# ユニーク

np.unique([配列]_ndarray_)
'''
[|[配列]_ndarray_の]ユニークな値を要素とする配列[|を得る]
'''

np.unique([配列]_ndarray_, return_counts=True)
'''
[|[配列]_ndarray_の]ユニークな要素ごとの[頻度|出現回数][|を得る]
'''


# 転置行列

[list(x) for x in list(zip(*_list_))]
'''
２次元リストを転置する
２次元リストの転置行列
'''

[配列]_ndarray_.T
'''
[配列]_ndarray_を転置する
[行列|配列]_ndarray_の転置行列
'''

[配列]_ndarray_ + [配列]_ndarray_
'''
[配列]_ndarray_の和
[配列]_ndarray_の要素ごとに加算する
'''

[配列]_ndarray_ - [配列]_ndarray_
'''
[配列]_ndarray_の差
'''

[配列]_ndarray_ * n
'''
[配列]_ndarray_のスカラー[倍|積]
'''

np.multiply([配列]_ndarray_, [配列]_ndarray_)
'''
[配列]_ndarray_の要素ごとの[積|アダマール積]
'''

np.dot([配列]_ndarray_, [配列]_ndarray_)
'''
[配列]_ndarray_の内積
'''

np.matmul([行列]_ndarray_, [行列]_ndarray_)
'''
[[[行列]_ndarray_と|][行列]_ndarray_の|]行列積
'''

np.linalg.inv([行列]_ndarray_)
'''
[[行列]_ndarray_の|]逆行列
'''

np.linalg.pinv([行列]_ndarray_)
'''
[[行列]_ndarray_の|]ムーア・ペンローズの擬似逆行列
'''


np.linalg.det([行列]_ndarray_)
'''
[[行列]_ndarray_の|]行列式
'''

np.linalg.eig([配列]_ndarray_)
'''
FIXME
'''

# ユニバーサル関数

np.gcd([配列]_ndarray_, [配列]_ndarray_)
'''
[配列]_ndarray_[間|]の要素ごとの最大公約数
'''

np.lcm([配列]_ndarray_, [配列]_ndarray_)
'''
[配列]_ndarray_[間|]の要素ごとの最小公倍数
'''

[行列 | 配列]_ndarray_.shape
'''
[行列|配列]_ndarray_の[形状|形|シェイプ]
'''

[行列 | 配列]_ndarray_.dtype()
'''
[行列|配列]_ndarray_の[データ型|型]
[行列|配列]_ndarray_[が|は]何のデータ型か調べる
'''

[行列 | 配列]_ndarray_.ndim
'''
[行列|配列]_ndarray_の[次元数|次元の数]
[行列|配列]_ndarray_[は|が]何次元か調べる
'''

[配列]_ndarray_.size
'''
[配列]_ndarray_の[要素数|個数]
[配列]_ndarray_にはいくつ要素が[ある|含まれる|存在する]か調べる
'''


np.concatenate([[行列 | 配列]_ndarray_, [行列 | 配列]_ndarray_], axis=0)
'''
{[２つの|[行列|配列]_ndarray_と][行列|配列]_ndarray_を|[列方向|縦方向]に}連結する
'''

np.concatenate([[行列 | 配列]_ndarray_, [行列 | 配列]_ndarray_], axis=1)
'''
{[２つの|[行列|配列]_ndarray_と][行列|配列]_ndarray_を|[行方向|横方向]に}連結する
'''

np.sum([配列]_ndarray_)
'''
[配列]_ndarray_の[合計値|合計]
'''

np.sum([行列 | 配列]_ndarray_, axis=0)
'''
[行列|配列]_ndarray_の列ごとの[合計値|合計]
'''

np.sum([行列 | 配列]_ndarray_, axis=1)
'''
[行列|配列]_ndarray_の行ごとの[合計値|合計]
'''

np.mean([配列]_ndarray_)
'''
[配列]_ndarray_の[平均値|平均]
'''

np.mean([行列 | 配列]_ndarray_, axis=0)
'''
[行列|配列]_ndarray_の列ごとの[平均値|平均]
'''

np.mean([行列 | 配列]_ndarray_, axis=1)
'''
[行列|配列]_ndarray_の行ごとの[平均値|平均]
'''

np.min([配列]_ndarray_)
'''
[配列]_ndarray_の[[最小値]_int_|最小]
'''

np.min([行列 | 配列]_ndarray_, axis=0)
'''
[行列|配列]_ndarray_の列ごとの[[最小値]_int_|最小]
'''

np.min([行列 | 配列]_ndarray_, axis=1)
'''
[行列|配列]_ndarray_の行ごとの[[最小値]_int_|最小]
'''

np.max([配列]_ndarray_)
'''
[配列]_ndarray_の[[最大値]_int_|最大]
'''

np.max([行列 | 配列]_ndarray_, axis=0)
'''
[行列|配列]_ndarray_の列ごとの[[最大値]_int_|最大]
'''

np.max([行列 | 配列]_ndarray_, axis=1)
'''
[行列|配列]_ndarray_の行ごとの[[最大値]_int_|最大]
'''

np.std([配列]_ndarray_)
'''
[配列]_ndarray_の標準偏差
'''

np.std([行列 | 配列]_ndarray_, axis=0)
'''
[行列|配列]_ndarray_の列ごとの標準偏差
'''

np.std([行列 | 配列]_ndarray_, axis=1)
'''
[行列|配列]_ndarray_の行ごとの標準偏差
'''

np.var([配列]_ndarray_)
'''
[配列]_ndarray_の分散
'''

np.var([行列 | 配列]_ndarray_, axis=0)
'''
[行列|配列]_ndarray_の列ごとの分散
'''

np.var([行列 | 配列]_ndarray_, axis=1)
'''
[行列|配列]_ndarray_の行ごとの分散
'''

np.cumsum([配列]_ndarray_)
'''
[配列]_ndarray_の累積和
'''

np.cumprod([配列]_ndarray_)
'''
[配列]_ndarray_の累積積
'''

np.unique([配列]_ndarray_)
'''
[配列]_ndarray_から重複を除きたい
[配列]_ndarray_から重複を除いた配列を作成する
[配列]_ndarray_のユニークな要素
'''

u, counts = np.unique([配列]_ndarray_, return_counts=True)
'''
[配列]_ndarray_のユニークな要素とその個数
'''

u, indices = np.unique([配列]_ndarray_, return_index=True)
'''
[配列]_ndarray_のユニークな要素とその[位置|インデックス]
'''

[配列]_ndarray_.flatten()
'''
[配列]_ndarray_を[平坦化|フラット化|一次元化]する
[配列]_ndarray_を[平坦|フラット|一次元]にする
'''
# Python 基本文法

# 演算子

# 識別子 => _クラス名_, _変数_
# コード => [結果]_str_

_クラス名_ = int
_str_ = 'A'
__オブジェクト__ = 'A'
__オブジェクト2__ = 'A'
__プロパティ__ = 'age'
__型名__ = int

'''
@poly(__オブジェクト__;オブジェクト;_変数_;[結果]_str_)
@poly(__オブジェクト2__;オブジェクト;_変数_;[結果]_str_)
@poly(__プロパティ__;[プロパティ|フィールド|属性] _プロパティ名_;_str_)
@poly(__型名__;_クラス名_;整数 int;[浮動小数点数|実数] float;文字列 str;論理値 bool;リスト list;タプル tuple;辞書 dict;集合 set;バイト列 bytes)
'''

__オブジェクト__ == __オブジェクト2__
'''
@alt(かどうか=[か知りたい|か調べたい])

２つの__オブジェクト__[が|は][等しい|同じ値]かどうか
'''

__オブジェクト__ is __オブジェクト2__
'''
@alt(同一|同じ)

２つの__オブジェクト__[が|は]同一[参照|]かどうか
'''

repr(__オブジェクト__)
'''
__オブジェクト__をデバッグ向けの文字列に変換する
'''

str(__オブジェクト__)
'''
__オブジェクト__を[|ユーザ向けの]文字列に変換する
'''

# 組み込み関数（リスト）

iter(__オブジェクト__)
'''
__オブジェクト__のイテレータ
__オブジェクト__を[イテラブル|イテレータ]に変換する
'''

# 組み込み関数（バイト列、IO）


bytearray(_str_)
'''
_str_をバイト配列に変換する
'''

bytes(_str_)
'''
_str_をバイト列に変換する
'''

memoryview(__オブジェクト__)
'''
__オブジェクト__のメモリビュー
'''

# 組み込み関数（関数）

callable(__オブジェクト__)
'''
__オブジェクト__[が|は][関数|呼び出し可能|コール可能]かどうか
'''

eval(_str_)
'''
_str_を[式として|]評価する
'''

globals()
'''
グローバル変数の一覧[|を列挙する]
'''


class Person:
    def __init__(self):
        self.TYPE = 'Konoha'
        self.age = 17


__オブジェクト__ = Person()
text = 'age'
s = 'age'

# 組み込み関数（オブジェクト）

プロパティ名 = 'age'

delattr(__オブジェクト__, __プロパティ__)
'''
@alt(プロパティ|属性|フィールド)
@alt(削除する|消する|取り除く)

__オブジェクト__[の|から]__プロパティ__を削除する
'''

getattr(__オブジェクト__, __プロパティ__)
'''
__オブジェクト__の__プロパティ__の値
'''

hasattr(__オブジェクト__, __プロパティ__)
'''
@alt(存在する|ある)
__オブジェクト__に__プロパティ__が存在するかどうか
__オブジェクト__が__プロパティ__を持つかどうか
'''

値 = 'A'

setattr(__オブジェクト__, __プロパティ__, 値)
'''
__オブジェクト__の__プロパティ__[の値|]を値に設定する
__オブジェクト__の__プロパティ__の値を設定する
'''

hash(__オブジェクト__)
'''
__オブジェクト__のハッシュ値[|求めたい]
'''

isinstance(__オブジェクト__, __型名__)
'''
__オブジェクト__[は|が]__型名__かどうか
'''

isinstance(__オブジェクト__, __X__)
'''
__オブジェクト__[は|が]__Y__かどうか
'''


issubclass(_クラス名_, _クラス名2_)
'''
_クラス名_は_クラス名2_のサブクラスかどうか
'''

id(__オブジェクト__)
'''
@alt(オブジェクト識別子|固有のID|ポインタ)

__オブジェクト__のオブジェクト識別子
'''

type(__オブジェクト__)
'''
__オブジェクト__の[クラス|型|種類][を調べたい|[を|が]知りたい]
'''
import pandas as pd
'''
@alt(表データ=[データフレーム|データフレーム|表[データ|]])
@alt(カラム=[列|列|カラム])
@alt(インデックス|行)
@alt(欠損値|NaN|未入力値)
@alt(抽出する|取り出す|[選択する|選ぶ])
'''

[カラム名]_ColumnName_ = '列A'
[データフレーム]_DataFrame_ = pd.DataFrame(
    data=[[1, 2, 3], [4, 5, 6]], columns=[[カラム名]_ColumnName_, [カラム名]_ColumnName_, '列C'])
[データフレーム]_DataFrame_ = pd.DataFrame(
    data=[[1, 1, 1], [1, 1, 1]], columns=[[カラム名]_ColumnName_, [カラム名]_ColumnName_, '列C'])
[データフレーム]_DataFrame_3 = pd.DataFrame(
    data=[[9, 9, 9], [9, 9, 9]], columns=[[カラム名]_ColumnName_, [カラム名]_ColumnName_, '列C'])
_データ列_ = [データフレーム]_DataFrame_[[カラム名]_ColumnName_]
[整数]_int_ = 1
__外部__ = 'outer'
'''
@poly(__外部__;[外部|全] 'outer';左 'left';右 'right';内部 'inner')
'''

# concat
pd.concat([[データフレーム]_DataFrame_, [データフレーム]_DataFrame_])
'''
@alt(連結する|合体[させたい|する]|[つなぎたい|くっつけたい])
@alt(結合する|一つに[する|まとめたい])

[２つの|][データフレーム]_DataFrame_を連結する
[データフレーム]_DataFrame_と[データフレーム]_DataFrame_を連結する
'''

pd.concat([[データフレーム]_DataFrame_, [データフレーム]_DataFrame_], axis=0)
'''
@alt(縦方向に|縦[|向き]に)

{[２つの|][データフレーム]_DataFrame_を|縦方向に}結合する
{[データフレーム]_DataFrame_と[データフレーム]_DataFrame_を|縦方向に}連結する
'''

pd.concat([[データフレーム]_DataFrame_, [データフレーム]_DataFrame_], axis=1)
'''
@alt(横方向に|横[向き|]に)

{[２つの|][データフレーム]_DataFrame_を|横方向に}連結する
{[データフレーム]_DataFrame_と[データフレーム]_DataFrame_を|横方向に}結合する
'''
pd.concat([[データフレーム]_DataFrame_, [データフレーム]_DataFrame_, [データフレーム]_DataFrame_3], axis=0)
'''
{[３つ|複数]の[データフレーム]_DataFrame_を|縦方向に}連結する
{[データフレーム]_DataFrame_と[データフレーム]_DataFrame_と[データフレーム]_DataFrame_を|縦方向に}結合する
'''

pd.concat([[データフレーム]_DataFrame_, [データフレーム]_DataFrame_, [データフレーム]_DataFrame_3], axis=1)
'''
{[３つ|複数]の[データフレーム]_DataFrame_を|横方向に}連結する
{[データフレーム]_DataFrame_と[データフレーム]_DataFrame_と[データフレーム]_DataFrame_を|縦方向に}結合する
'''

pd.concat([[データフレーム]_DataFrame_, _データ列_], axis=1)
'''
[データフレーム]_DataFrame_と_データ列_を[横方向に|]連結する
'''

[データフレーム]_DataFrame_[[データフレーム]_DataFrame_.columns[1:]]
'''
@alt(カラム|列)

[最初の|一番左[側]の|先頭の]カラムを[除いた|外した][データフレーム]_DataFrame_
'''

[データフレーム]_DataFrame_[[データフレーム]_DataFrame_.columns[: -1]]
'''
[最後の|一番右[側]の|末尾の]カラムを[除いた|外した][データフレーム]_DataFrame_
'''

[データフレーム]_DataFrame_.drop([データフレーム]_DataFrame_.columns[_int_], axis=1)
'''
[_int_番目の|1行だけ]カラムを[除いた|外した][データフレーム]_DataFrame_
'''

# マージ

pd.merge([データフレーム]_DataFrame_, [データフレーム]_DataFrame_)
'''
@alt(ジョインする|結合[を行いたい|する])

{２つの[データフレーム]_DataFrame_を|横方向に}マージする
[２|二]つの[データフレーム]_DataFrame_をジョインする
'''

pd.merge([データフレーム]_DataFrame_, [データフレーム]_DataFrame_, on=[カラム名]_ColumnName_)
'''
{[データフレーム]_DataFrame_[|とデータフレーム]|[カラム名]_ColumnName_で}をジョインする
'''

pd.merge([データフレーム]_DataFrame_, [データフレーム]_DataFrame_, left_on=[カラム名]_ColumnName_, right_on=[カラム名]_ColumnName_)
'''
[データフレーム]_DataFrame_[|と[データフレーム]_DataFrame_]をジョインする
[カラム名]_ColumnName_と列名_をジョインする
'''


pd.merge([データフレーム]_DataFrame_, [データフレーム]_DataFrame_, on=[カラム名]_ColumnName_, how=__外部__)
'''
{[データフレーム]_DataFrame_[|と[データフレーム]_DataFrame_]を|[カラム名]_ColumnName_で}__外部__ジョインする
'''

pd.merge([データフレーム]_DataFrame_, [データフレーム]_DataFrame_, left_on=[カラム名]_ColumnName_, right_on=[カラム名]_ColumnName_, how=__外部__)
'''
[カラム名]_ColumnName_と[カラム名]_ColumnName_を__外部__ジョインする
'''

# ダミー処理

pd.get_dummies([データフレーム]_DataFrame_)
'''
@alt(ダミー変数|[ワンホット・ベクトル|ベクトル])

[データフレーム]_DataFrame_[のカテゴリデータ|]をダミー変数[化|に変換]する
'''

pd.get_dummies([データフレーム]_DataFrame_[[カラム名]_ColumnName_])
'''
@alt(あるカラム|[指定した|指定された|]カラム)

[カラム名]_ColumnName_をダミー変数[化|に変換]する
'''

pd.get_dummies([データフレーム]_DataFrame_[[カラム名]_ColumnName_], drop_first=True)
'''
@alt(除外する|除く|無視する)

[カラム名]_ColumnName_をダミー変数[化|に変換]する。最初のカテゴリを[無視|除外]
'''

pd.get_dummies([データフレーム]_DataFrame_[[カラム名]_ColumnName_], dummy_na=True)
'''
@alt(欠損値|NaN)

[カラム名]_ColumnName_をダミー変数[化|に変換]する。欠損値も含め[たい|て]
'''
import numpy as np
import pandas as pd
'''
[Pandas|データフレーム]を使用する
'''

import seaborn as sns

[整数]_int_ = 1
_型名_ = int

[カラム名]_ColumnName_ = 'A'
列名のリスト = ['A', 'B', 'C']
[データフレーム]_DataFrame_ = pd.DataFrame(data=[[1, 2, 3], [4, 5, 6]], columns=列名のリスト)


# 確認系

[データフレーム]_DataFrame_.head()
'''
@alt(が見たい|を確認する|を表示する)
[データフレーム]_DataFrame_[|の内容]が見たい
[データフレーム]_DataFrame_の[先頭|最初]が見たい
'''

[データフレーム]_DataFrame_.tail()
'''
[データフレーム]_DataFrame_の[末尾|最後]が見たい
'''

[データフレーム]_DataFrame_.head(_int_)  # 行数
'''
@alt(抽出する|取り出する)
[データフレーム]_DataFrame_の[先頭|最初|上]_int_行を抽出する
'''

[データフレーム]_DataFrame_.tail(_int_)  # 行数
'''
[データフレーム]_DataFrame_の[末尾|最後|下]_int_行を抽出する
'''

行数 = 10

[データフレーム]_DataFrame_.sample(行数)
'''
@alt(データ行|行)
{[データフレーム]_DataFrame_から|ランダムに|データ行}を抽出する
[データフレーム]_DataFrame_を[|ランダム]サンプリングする
'''

[データフレーム]_DataFrame_.sample(_int_)
'''
{[データフレーム]_DataFrame_から|ランダムに|_int_行を}抽出する
[データフレーム]_DataFrame_から_int_行、[|ランダム]サンプリングする
'''

[データフレーム]_DataFrame_.sample(_int_, replace=True)
'''
@alt(重複ありで|重複を認めて)
{[データフレーム]_DataFrame_から|重複ありで|ランダムに|_int_行を}サンプリングする
'''

開始行 = 0
終了行 = 2

[データフレーム]_DataFrame_[開始行: 終了行+1]
'''
@alt(新しく表にする|抽出する)
{[データフレーム]_DataFrame_のデータ行を|[範囲指定して|一部]}新しく表にする
'''

[データフレーム]_DataFrame_[_int_: _int_]
'''
{[データフレーム]_DataFrame_を|_int_行目から_int_行目まで}新しく表にする
'''

[データフレーム]_DataFrame_[_int_:]
'''
[データフレーム]_DataFrame_の_int_行[|目][以降|より後ろ][|を]新しく表にする
'''

[データフレーム]_DataFrame_[: _int_]
'''
[データフレーム]_DataFrame_の_int_行[|目][まで|より前][|を]新しく表にする
'''

[データフレーム]_DataFrame_.loc[_int_]
'''
[データフレーム]_DataFrame_の_int_[行目|番目の行]を抽出する
[データフレーム]_DataFrame_のインデックスが_int_の行を抽出する
'''

# 列名

[データフレーム]_DataFrame_[[カラム名]_ColumnName_]
'''
@alt(抽出する|取り出する)
[データフレーム]_DataFrame_から一列、抽出する
[[データフレーム]_DataFrame_から|][カラム名]_ColumnName_を抽出する
'''

[データフレーム]_DataFrame_[[カラム名]_ColumnName_].values
'''
@alt(に変換する|にする)
[[データフレーム]_DataFrame_の|][カラム名]_ColumnName_を配列に変換する
{[[データフレーム]_DataFrame_の|][カラム名]_ColumnName_を|配列として}抽出する
'''

[データフレーム]_DataFrame_[[カラム名]_ColumnName_].values.tolist()
'''
[[データフレーム]_DataFrame_の|][カラム名]_ColumnName_をリストに変換する
{[[データフレーム]_DataFrame_の|][カラム名]_ColumnName_を|リストとして}抽出する
'''

[データフレーム]_DataFrame_[[[カラム名]_ColumnName_]]
'''
[データフレーム]_DataFrame_からカラムを１つ[|のみ|だけ]選択する
[カラム名]_ColumnName_[のみ|だけ]の[新しい|]データフレーム
'''

[データフレーム]_DataFrame_[[[カラム名]_ColumnName_, [カラム名]_ColumnName_]]
'''
[データフレーム]_DataFrame_からカラムを２つ[|のみ|だけ]選択する
[カラム名]_ColumnName_と[カラム名]_ColumnName_[のみ|だけ]の[新しい|]データフレーム
'''

[データフレーム]_DataFrame_[[[カラム名]_ColumnName_, [カラム名]_ColumnName_, [カラム名]_ColumnName_]]
'''
[データフレーム]_DataFrame_からカラムを３つ[|のみ|だけ]選択する
[カラム名]_ColumnName_と[カラム名]_ColumnName_と[カラム名]_ColumnName_[のみ|だけ]の[新しい|]データフレーム
'''

[データフレーム]_DataFrame_[列名のリスト]
'''
[データフレーム]_DataFrame_から列名のリストを指定して選択する
'''

[データフレーム]_DataFrame_.info()
'''
[データフレーム]_DataFrame_の[列名の一覧|概要]が見たい
'''

[データフレーム]_DataFrame_.columns
'''
@alt(列挙する|全て見たい)
[データフレーム]_DataFrame_の列名の一覧
[データフレーム]_DataFrame_の列名を列挙する
'''

[データフレーム]_DataFrame_.columns = 列名のリスト
'''
[[データフレーム]_DataFrame_の|]カラム名を[列名のリストで|全て]置き替えたい
'''

[データフレーム]_DataFrame_.select_dtypes('object').columns
'''
@alt(カテゴリデータ|[質的データ|数値データ以外])

[データフレーム]_DataFrame_からカテゴリデータの列名の一覧
[データフレーム]_DataFrame_からカテゴリデータの列名を列挙する
'''

[データフレーム]_DataFrame_.select_dtypes(_型名_).columns
'''
[データフレーム]_DataFrame_から_型名_の列名の一覧
[データフレーム]_DataFrame_の_型名_の列名を列挙する
'''

[データフレーム]_DataFrame_.index
'''
[データフレーム]_DataFrame_のインデックス[|の名前]の一覧
'''

[データフレーム]_DataFrame_.values
'''
[データフレーム]_DataFrame_を[まとめて|全て|]配列に変換する
'''

[データフレーム]_DataFrame_.dtypes
'''
[データフレーム]_DataFrame_のデータ型の一覧
'''

[データフレーム]_DataFrame_.select_dtypes(include=[_型名_])
'''
[データフレーム]_DataFrame_からある型の列[を|のみ|だけ]抽出する
'''

[データフレーム]_DataFrame_.select_dtypes(exclude=[_型名_])
'''
[データフレーム]_DataFrame_からtypeList[で指定した|の]データ型のカラム[を|のみ|だけ]除外する
'''

__X__ = 'object'
'''
@X('object';'number';ty)
@Y(カテゴリデータ;数値データ;ty[|型])
'''

[データフレーム]_DataFrame_.select_dtypes(__X__)
'''
[データフレーム]_DataFrame_から__Y__[のカラム][を|のみ|だけ]抽出する
'''

[データフレーム]_DataFrame_.shape
'''
[データフレーム]_DataFrame_の[シェイプ|形状]が見たい
[データフレーム]_DataFrame_の[次元[の大きさ|数]|行数と列数]が見たい

'''

[データフレーム]_DataFrame_.T
'''
[データフレーム]_DataFrame_を転置する
[データフレーム]_DataFrame_の[行と列|行列]を[入れ替えたい|ひっくり返する]
'''

__表__ = [データフレーム]_DataFrame_
'''
@poly(__表__;[データフレーム]_DataFrame_;[カラム名]_ColumnName_と[カラム名]_ColumnName_ [データフレーム]_DataFrame_[[[カラム名]_ColumnName_, [カラム名]_ColumnName_]])
'''

[データフレーム]_DataFrame_.corr()
'''
[データフレーム]_DataFrame_のカラム間の[相関行列|相関[係数|]]を[まとめて|]求めたい
'''

__表__.corr()
'''
__表__[相関行列|相関[係数|]]を[まとめて|]求めたい
__表__の相関行列[|]
'''

__表__.corr(method='pearson')
'''
{[ピアソン|[|積率]相関係数]で_|__表__の相関行列を}求めたい
'''

__表__.corr(method='kendall')
'''
{[ケンドール[|順位]相関係数|]で_|__表__の相関行列を}求めたい
'''

__表__.corr(method='spearman')
'''
{スピアマン[[|順位]相関係数|]で_|__表__の相関行列を}求めたい
'''

sns.heatmap(__表__.corr())
'''
@alt(描画する|グラフ化する)

{__表__の相関行列を|[ヒートマップで_|]}描画する
{__表__の相関行列を|[ヒートマップで_|]}可視化する
'''

[データフレーム]_DataFrame_.round()
'''
@alt(丸めたい|四捨五入する)
@alt(丸めて|四捨五入して)
@alt[まとめて|全て|]
@alt(インプレイスする|更新する|置き替えたい)
[データフレーム]_DataFrame_[の数値|]をまとめて[|整数に]丸めたい
'''

[データフレーム]_DataFrame_.round(_int_)
'''
[データフレーム]_DataFrame_[の数値|]をまとめて小数点以下_int_桁で丸めたい
'''

# 変更する

[データフレーム]_DataFrame_.rename(columns={[カラム名]_ColumnName_: [カラム名]_ColumnName_, [カラム名]_ColumnName_: [カラム名]_ColumnName_})
'''
@alt(リネームする|名前[|を]変更する)
@alt(付け直する|変更する)

[データフレーム]_DataFrame_のカラムをリネームする
[データフレーム]_DataFrame_のカラムの名前を付け直する
'''

[データフレーム]_DataFrame_.columns = [str(x).replace(s, s2) for x in [データフレーム]_DataFrame_.columns]
'''
@alt(まとめて|一度に|全て)

{[データフレーム]_DataFrame_のカラムの名前を|まとめて}[|文字列]置換する
'''

[データフレーム]_DataFrame_.rename(index={x: y})
'''
[データフレーム]_DataFrame_のインデックスの名前をまとめて付け直する
'''

[データフレーム]_DataFrame_.set_index([カラム名]_ColumnName_)
'''
[[データフレーム]_DataFrame_の|][カラム名]_ColumnName_をインデックスに設定する
'''

[データフレーム]_DataFrame_.reset_index()
'''
[データフレーム]_DataFrame_のインデックスを[リセットする|振り直する]
'''

# datetime
__値__ = 1

[データフレーム]_DataFrame_[[データフレーム]_DataFrame_[[カラム名]_ColumnName_] == __値__]
'''
@poly(__値__;_int_;_str_)
@poly(__値2__;_int_;_str_)
@alt(を抽出する|[のみ|だけ]残する)

[[データフレーム]_DataFrame_の|][カラム名]_ColumnName_が__値__[と同じ|に等しい]行データを抽出する
[カラム名]_ColumnName_[|の値]が__値__の行[だけ|のみ]のデータフレーム
'''

[データフレーム]_DataFrame_[[データフレーム]_DataFrame_[[カラム名]_ColumnName_] != __値__]
'''
[[データフレーム]_DataFrame_の|][カラム名]_ColumnName_が__値__[でない|に等しくない]行データを抽出する
[カラム名]_ColumnName_[|の値]が__値__でない行[だけ|のみ]のデータフレーム
'''

[データフレーム]_DataFrame_[([データフレーム]_DataFrame_[[カラム名]_ColumnName_] == __値__) & ([データフレーム]_DataFrame_[[カラム名]_ColumnName_] == __値2__)]
'''
[[データフレーム]_DataFrame_|]の行データを条件で[フィルタする|抽出する]
[カラム名]_ColumnName_が__値__に等しく、[かつ|][カラム名]_ColumnName_が__値2__に等しい行データを抽出する
'''

[データフレーム]_DataFrame_[[データフレーム]_DataFrame_[[カラム名]_ColumnName_] < __値__]
'''
[[データフレーム]_DataFrame_の|][カラム名]_ColumnName_が__値__より[小さい|少ない]行データを抽出する
[カラム名]_ColumnName_[|の値]が__値__より[小さい|少ない]行[だけ|のみ]のデータフレーム
'''

[データフレーム]_DataFrame_[[データフレーム]_DataFrame_[[カラム名]_ColumnName_] <= __値__]
'''
[[データフレーム]_DataFrame_の|][カラム名]_ColumnName_が__値__以下の行データ[のみ|だけ|を]抽出する
[カラム名]_ColumnName_[|の値]が__値__以下の行[だけ|のみ]のデータフレーム
'''

[データフレーム]_DataFrame_[[データフレーム]_DataFrame_[[カラム名]_ColumnName_] > __値__]
'''
[[データフレーム]_DataFrame_の|][カラム名]_ColumnName_が__値__より[大きい|多い]行データを抽出する
[カラム名]_ColumnName_[|の値]が__値__より[大きい|多い][だけ|のみ]のデータフレーム
'''

[データフレーム]_DataFrame_[[データフレーム]_DataFrame_[[カラム名]_ColumnName_] >= __値__]
'''
[[データフレーム]_DataFrame_の|][カラム名]_ColumnName_が__値__以上の行データを抽出する
[カラム名]_ColumnName_[|の値]が__値__以上の行[だけ|のみ]のデータフレーム
'''

[データフレーム]_DataFrame_[(__値__ < [データフレーム]_DataFrame_[[カラム名]_ColumnName_]) & ([データフレーム]_DataFrame_[[カラム名]_ColumnName_] < __値__)]
'''
[カラム名]_ColumnName_が__値__より大きく、__値__より小さい行データを抽出する
'''

[データフレーム]_DataFrame_[(__値__ <= [データフレーム]_DataFrame_[[カラム名]_ColumnName_]) & ([データフレーム]_DataFrame_[[カラム名]_ColumnName_] <= __値__)]
'''
[カラム名]_ColumnName_が__値__以上、__値__以下の行データを抽出する
'''

[データフレーム]_DataFrame_[(__値__ <= [データフレーム]_DataFrame_[[カラム名]_ColumnName_]) & ([データフレーム]_DataFrame_[[カラム名]_ColumnName_] < __値__)]
'''
[カラム名]_ColumnName_が__値__以上、__値__未満の行データを抽出する
'''

_list_ = ['A', 'B']

[データフレーム]_DataFrame_[[データフレーム]_DataFrame_[[カラム名]_ColumnName_].isin(_list_)]
'''
_list_の値が[カラム名]_ColumnName_に含まれる行データを抽出する
[カラム名]_ColumnName_において_list_内の値[だけ|のみ]抽出する
'''

[データフレーム]_DataFrame_[~[データフレーム]_DataFrame_[[カラム名]_ColumnName_].isin(_list_)]
'''
_list_の値が[カラム名]_ColumnName_に含まれない行データを抽出する
[カラム名]_ColumnName_において_list_外の値[だけ|のみ]抽出する
'''

_str_ = 'a'
正規表現 = 'b'

[データフレーム]_DataFrame_[[データフレーム]_DataFrame_[[カラム名]_ColumnName_].str.contains(_str_)]
'''
{[データフレームの|][カラム名]_ColumnName_において|_str_が}[含まれる|ある|存在する]行データを抽出する
'''

[データフレーム]_DataFrame_[~[データフレーム]_DataFrame_[[カラム名]_ColumnName_].str.contains(_str_)]
'''
{[データフレームの|][カラム名]_ColumnName_に|_str_が}[含まれない|ない|存在しない]行データを抽出する
'''

[データフレーム]_DataFrame_[[データフレーム]_DataFrame_[[カラム名]_ColumnName_].str.match(正規表現)]
'''
[データフレームの|][カラム名]_ColumnName_が正規表現にマッチする行データを抽出する
'''

[データフレーム]_DataFrame_[~[データフレーム]_DataFrame_[[カラム名]_ColumnName_].str.match(正規表現)]
'''
[データフレームの|][カラム名]_ColumnName_が正規表現にマッチしない行データを抽出する
'''

[データフレーム]_DataFrame_[[データフレーム]_DataFrame_[[カラム名]_ColumnName_].str.startswith(_str_)]
'''
[カラム名]_ColumnName_が_str_で始まる行データを抽出する
[カラム名]_ColumnName_の接頭辞が_str_である行データを抽出する
'''

[データフレーム]_DataFrame_[~[データフレーム]_DataFrame_[[カラム名]_ColumnName_].str.startswith(_str_)]
'''
[カラム名]_ColumnName_が_str_で始まらない行データを抽出する
[カラム名]_ColumnName_の接頭辞が_str_でない行データを抽出する
'''

[データフレーム]_DataFrame_[[データフレーム]_DataFrame_[[カラム名]_ColumnName_].str.endswith(_str_)]
'''
[カラム名]_ColumnName_が_str_で終わる行データを抽出する
_str_が[カラム名]_ColumnName_の接尾辞である行データを抽出する
'''

[データフレーム]_DataFrame_[~[データフレーム]_DataFrame_[[カラム名]_ColumnName_].str.endswith(_str_)]
'''
[カラム名]_ColumnName_が_str_で終わらない行データを抽出する
_str_が[カラム名]_ColumnName_の接尾辞でない行データを抽出する
'''

# ドロップ・欠損値処理

[データフレーム]_DataFrame_.style.highlight_null()
'''
@alt(付け|つけ)

[データフレーム]_DataFrame_の欠損値が[含まれる|ある][箇所|部分][に[色を付ける]|を[色付けする]]
'''

[データフレーム]_DataFrame_.drop(_int_, axis=0)
'''
@alt(ドロップする|[削除する|消する]|[除きたい|取り除きたい])

[データフレーム]_DataFrame_の_int_行目をドロップしてみたい
'''

[データフレーム]_DataFrame_.drop(_int_, axis=0, inplace=True)
'''
@alt(破壊的に|インプレイスで)

[データフレーム]_DataFrame_の_int_行目を[|破壊的に]ドロップする
'''

[データフレーム]_DataFrame_.drop([カラム名]_ColumnName_, axis=1)
'''
[[データフレーム]_DataFrame_の|][カラム名]_ColumnName_をドロップしてみたい
'''

[データフレーム]_DataFrame_.drop([カラム名]_ColumnName_, axis=1, inplace=True)
'''
@alt(_変更を反映する|入れ替えたい|更新する)

[[データフレーム]_DataFrame_の|][カラム名]_ColumnName_を[|破壊的に]ドロップする
'''

[データフレーム]_DataFrame_ = pd.DataFrame(data={'A': ['A', 'B'], 'B': ['B', 'A']})

[データフレーム]_DataFrame_.drop([[カラム名]_ColumnName_, [カラム名]_ColumnName_], axis=1)
'''
[データフレーム]_DataFrame_の[複数の|二つの]カラムをドロップしてみたい
'''

[データフレーム]_DataFrame_.drop([[カラム名]_ColumnName_, [カラム名]_ColumnName_], axis=1, inplace=True)
'''
[データフレーム]_DataFrame_の[複数の|二つの]カラムをドロップする
'''

[データフレーム]_DataFrame_ = pd.DataFrame(data={[カラム名]_ColumnName_: ['A', 'B'], [カラム名]_ColumnName_: ['B', 'A']})

[データフレーム]_DataFrame_.drop(columns, axis=1, inplace=True)
'''
[データフレーム]_DataFrame_のcolumnsで指定したカラムをドロップする
'''

# 欠損値

[データフレーム]_DataFrame_.dropna()
'''
@alt(の中|の内)
[データフレーム]_DataFrame_[中|]の欠損値をドロップしてみたい
欠損値が[ある|存在する]行をドロップしてみたい
'''

[データフレーム]_DataFrame_.dropna(inplace=True)
'''
[データフレーム]_DataFrame_[中|]の欠損値を[|破壊的に]ドロップする
欠損値[が|の][ある|存在する]行を[|破壊的に]ドロップする
'''

# 重複

[データフレーム]_DataFrame_ = pd.DataFrame(data={[カラム名]_ColumnName_: [1, 1], [カラム名]_ColumnName_: [1, 1]})

[データフレーム]_DataFrame_.duplicated()
'''
@alt(重複行|重複した行|重複)

[データフレーム]_DataFrame_の重複行が見たい
[データフレーム]_DataFrame_[に重複があるか|が重複しているか]見たい
[データフレーム]_DataFrame_の重複行のマスク
'''

[データフレーム]_DataFrame_.duplicated().sum()
'''
[データフレーム]_DataFrame_の重複行を数えたい
[データフレーム]_DataFrame_[は|が]何行重複しているか見たい
'''

[データフレーム]_DataFrame_[[データフレーム]_DataFrame_.duplicated(keep=False)]
'''
[[データフレーム]_DataFrame_の|]重複した行[のみ|だけ|]新しいデータフレームにする
'''

[データフレーム]_DataFrame_[~ [データフレーム]_DataFrame_.duplicated(keep=False)]
'''
[[データフレーム]_DataFrame_の|]重複して[|い]ない行[のみ|だけ|]新しいデータフレームにする
'''

[データフレーム]_DataFrame_.duplicated(subset=[カラム名]_ColumnName_)
'''
[カラム名]_ColumnName_[について|の]重複行が見たい
'''

[データフレーム]_DataFrame_.duplicated(subset=[[カラム名]_ColumnName_, [カラム名]_ColumnName_])
'''
[カラム名]_ColumnName_と[カラム名]_ColumnName_[について|の]重複が見たい
複数の[カラム名]_ColumnName_[について|の]重複が見たい
'''

[データフレーム]_DataFrame_.drop_duplicates(inplace=True)
'''
[データフレーム]_DataFrame_から重複を[|破壊的に]ドロップする
[データフレーム]_DataFrame_から同じ[内容の|]行データを[|破壊的に]ドロップする
'''


[データフレーム]_DataFrame_.drop_duplicates(keep=False, inplace=True)
'''
[データフレーム]_DataFrame_から重複を残さず重複をドロップする
[データフレーム]_DataFrame_から重複した行データを残さずドロップする
'''

[データフレーム]_DataFrame_.drop_duplicates(subset=[カラム名]_ColumnName_, inplace=True)
'''
[カラム名]_ColumnName_[で|において]重複があれば、ドロップする
'''

[データフレーム]_DataFrame_.drop_duplicates(subset=[[カラム名]_ColumnName_, [カラム名]_ColumnName_], inplace=True)
'''
[カラム名]_ColumnName_と[カラム名]_ColumnName_において重複が除去する
複数の[カラム名]_ColumnName_の重複を取り除きたい
'''
import pandas as pd
'''
@test($$;type(pd))
@alt(全ての|すべての|全)
@alt(の名前|名)
@alt(見る|知る|調べる)

@prefix(value;[文字列|日付|])
'''

dateList = [pd.to_datetime('12-12-12'), pd.to_datetime('12-12-12')]
[データフレーム]_DataFrame_ = pd.DataFrame(data={'列A': dateList, '列B': [1, 2]})
[カラム名]_ColumnName_ = '列A'


日付を表現した文字列 = '11-01-01'  # 例
pd.to_datetime(日付を表現した文字列)
'''
@alt(日付データ|タイムスタンプ[型|]|Pandasの日付[型|データ]|datetime64型)
[日付を表現した|]文字列を日付データに変換する
'''

[データ列]_DataFrame_[_ColumnName_]] = [データフレーム]_DataFrame_[[カラム名]_ColumnName_]
__データシリーズ__ = [データ列]_DataFrame_[_ColumnName_]]
'''
@poly([データ列]_DataFrame_[_ColumnName_]];[カラム名]_ColumnName_ [データフレーム]_DataFrame_[[カラム名]_ColumnName_];_list_)
@poly(__データシリーズ__;[カラム名]_ColumnName_ [データフレーム]_DataFrame_[[カラム名]_ColumnName_];_データ列_)
'''

pd.to_datetime([データ列]_DataFrame_[_ColumnName_]])
'''
[データ列]_DataFrame_[_ColumnName_]]を[全て|]日付データに変換する
'''

pd.to_datetime([データ列]_DataFrame_[_ColumnName_]], format='%Y-%m-%d')
'''
@alt(フォーマット|書式)

{[データ列]_DataFrame_[_ColumnName_]]を|フォーマット[にしたがって|を指定して]}[全て|]日付データに変換する
'''

# エポック秒

pd.to_datetime([データ列]_DataFrame_[_ColumnName_]], unit='s', utc=True)
'''
@alt(エポック秒|UNIX秒|UNIX時間)

エポック秒から日付データに変換する
[データ列]_DataFrame_[_ColumnName_]]のエポック秒を[全て|]日付データに変換する
'''

[データフレーム]_DataFrame_.set_index([カラム名]_ColumnName_, inplace=True)
'''
[データフレーム]_DataFrame_のあるカラムをインデックスにする
'''

[データフレーム]_DataFrame_.index = pd.DatetimeIndex([データフレーム]_DataFrame_[[カラム名]_ColumnName_])
'''
[カラム名]_ColumnName_の日付を[[データフレーム]_DataFrame_の|]インデックスにする
'''

[データフレーム]_DataFrame_.index = pd.DatetimeIndex(pd.to_datetime([データフレーム]_DataFrame_[[カラム名]_ColumnName_]))
'''
[カラム名]_ColumnName_を日付データに変換し、[[データフレーム]_DataFrame_の|]インデックスにする
'''

__データシリーズ__.tz_convert('Asia/Tokyo')
'''
__データシリーズ__のタイムゾーンを[日本|東京]に設定する
__データシリーズ__のタイムゾーンを設定する
'''

__データシリーズ__.dt.year
'''
__データシリーズ__の年[|度]
__データシリーズ__[が|は]何年か調べたい
'''

__データシリーズ__.dt.month
'''
__データシリーズ__の月
__データシリーズ__[が|は]何月か調べたい
'''

__データシリーズ__.dt.day
'''
__データシリーズ__の[日|日にち]
__データシリーズ__[が|は]何日か調べたい
'''

__データシリーズ__.dt.hour
'''
__データシリーズ__の[時|時刻]
__データシリーズ__[が|は]何時か調べたい
'''

__データシリーズ__.dt.minute
'''
__データシリーズ__の分
__データシリーズ__[が|は]何分か調べたい
'''

__データシリーズ__.dt.second
'''
__データシリーズ__の秒
__データシリーズ__[が|は]何秒か調べたい
'''

__データシリーズ__.dt.weekday_name
'''
__データシリーズ__の曜日[の名前|]
__データシリーズ__[が|は]何曜日か調べたい
'''

__データシリーズ__.dt.dayofweek
'''
__データシリーズ__の曜日数
__データシリーズ__の曜日[[が|は]何日目か|を]調べたい
'''
import numpy as np

import pandas as pd
'''
@alt(の名前|名)
'''

import seaborn as sns

[整数]_int_ = 1

_CSVファイル_ = 'file.csv'
_TSVファイル_ = 'file.tsv'
_エクセルファイル_ = 'file.xslx'
_JSONファイル_ = 'file.json'
_JSONLファイル_ = 'file.jsonl'
[データフレーム]_DataFrame_ = pd.DataFrame()


__CSV__ = _CSVファイル_
'''
@poly(__CSV__;_CSVファイル_ _CSVファイル_, sep=',';_TSVファイル_ _TSVファイル_, sep='\t')
'''

df = pd.read_csv(__CSV__)
'''
{__CSV__から|データフレームを}読みたい
{__CSV__を|データフレーム[に|として]}読みたい
'''

df = pd.read_csv(__CSV__, header=None)
'''
{__CSV__を|[ヘッダ|カラム名][を指定せず|なしで]}}読みたい
{__CSV__から|データフレームを}読みたい。ヘッダは[無視|なし]
'''

df = pd.read_csv(__CSV__, index_col=_int_)
'''
{__CSV__の_int_[列|カラム]目を|インデックス[と|に]して}}読みたい
{__CSV__を|データフレーム[に|として]}読みたい。インデックスは_int_[列|カラム]目
'''

df = pd.read_csv(__CSV__, index_col=None)
'''
{__CSV__を|データフレーム[に|として]}読みたい。どの[列|カラム]もインデックスにしない
'''

df = pd.read_csv(__CSV__, encoding='shift_jis')
'''
{__CSV__を|[SJISで|文字化けしないように]}}読みたい
__CSV__から{CSVファイルを|[SJISで|文字化けしないように]}}読みたい
'''

_str_ = 'utf-8'

df = pd.read_csv(__CSV__, encoding=_str_)
'''
@alt(文字コード|文字エンコーディング)

{__CSV__から|[データフレームを|]}読みたい。文字コードは_str_
'''

df = pd.read_excel(_エクセルファイル_)
'''
@alt(エクセル|[エクセル|表計算|Excel][ファイル|])
@alt(読みたい|読み込みたい|ロードする)
@alt(読んで|読み込んで|ロードして)

{[エクセル|_エクセルファイル_]から|データフレームを}読みたい
_エクセルファイル_を読んで、新しいデータフレームを作成する
'''

df = pd.read_excel(_エクセルファイル_, sheet_name=['A', 'B'])
'''
[エクセルの|]シートの名前を指定する
{_エクセルファイル_から|シートの名前を指定して|データフレームを}読みたい
_エクセルファイル_を読んで、新しいデータフレームを作成する
'''

df = pd.read_excel(_エクセルファイル_, sheet_name=[0, 2])
'''
[エクセルの|]シートの番号を指定する
{_エクセルファイル_から|シートの番号を指定して|データフレームを}読みたい
'''

pd.read_json(_JSONLファイル_, orient='records', lines=True)
'''
{JSONL[形式の|]ファイルから|データフレームを}}読みたい
{_JSONLファイル_から|データフレームを}読みたい
{_JSONLファイル_を|データフレーム[に|として]}読みたい
'''

# write

[データフレーム]_DataFrame_.to_excel(_エクセルファイル_)
'''
@alt(保存する|出力する|書き込みたい)

{[データフレーム]_DataFrame_を|_エクセルファイル_[で|に]}保存する
'''

[データフレーム]_DataFrame_.to_csv(__CSV__)
'''
{[データフレーム]_DataFrame_を|__CSV__に}保存する
'''

[データフレーム]_DataFrame_.to_csv(__CSV__, header=None)
'''
@alt(ヘッダを付けず|[ヘッダ|カラム名]なしで)

{[データフレーム]_DataFrame_を|ヘッダを付けず|__CSV__[に|で]}保存する
{[データフレーム]_DataFrame_を|__CSV__に}保存する。ヘッダは[不要|なし]
'''

[データフレーム]_DataFrame_.to_csv(__CSV__, index=None)
'''
{[データフレーム]_DataFrame_を|インデックスを付けず|__CSV__[に|で]}保存する
{[データフレーム]_DataFrame_を|__CSV__に}保存する。インデックスは[不要|なし]
'''

[データフレーム]_DataFrame_.to_csv(__CSV__, encoding='utf_8_sig')
'''
@alt(BOM付きで|BOMを付けて|Windows向けに|文字化けしないように)

{[データフレーム]_DataFrame_を|BOM付きで|__CSV__}保存する
'''

[データフレーム]_DataFrame_.to_csv(__CSV__, encoding=_str_)
'''
{[データフレーム]_DataFrame_を|__CSV__[に|で]}保存する。文字コードは_str_
'''

[データフレーム]_DataFrame_.to_csv(__CSV__, float_format='%.3f')
'''
@alt(精度|小数点以下の桁数)

{[データフレーム]_DataFrame_を|精度付きで|__CSV__に}保存する
'''

[データフレーム]_DataFrame_.to_json(force_ascii=False)
'''
{[データフレーム]_DataFrame_を|JSON形式[の文字列|][に|へ]}変換する
'''

[データフレーム]_DataFrame_.to_json(_JSONファイル_, force_ascii=False)
'''
{[データフレーム]_DataFrame_を|_JSONファイル_[に|へ]|}保存する
'''

[データフレーム]_DataFrame_.to_json(_JSONLファイル_, force_ascii=False, orient='records', lines=True)
'''
{[データフレーム]_DataFrame_を|_JSONLファイル_[に|へ]|}保存する
{[データフレーム]_DataFrame_を|[一行ずつ|]_JSONファイル_[に|へ]|}保存する
'''

[データフレーム]_DataFrame_.to_dict()
'''
{[データフレーム]_DataFrame_を|辞書[に|へ]}変換する
'''

[データフレーム]_DataFrame_.to_dict(orient='list')
'''
{[データフレーム]_DataFrame_を|列名とリストの辞書[に|へ]}変換する
'''

[データフレーム]_DataFrame_.to_dict(orient='split')
'''
{[データフレーム]_DataFrame_を|[分解|バラバラに]して辞書[に|へ]}変換する
'''

[データフレーム]_DataFrame_.to_dict(orient='records')
'''
{[データフレーム]_DataFrame_を|行[単位|ごと]で辞書[に|へ]}変換する
'''
import pandas as pd

[データフレーム]_DataFrame_ = pd.DataFrame(
    data=[[1, 2, 3], [4, 5, 6]], columns=['列A', '列B', '列C'])

[カラム名]_ColumnName_ = 'A'


def func(x): return '列A'


関数 = func

# グループ化


[データフレーム]_DataFrame_.groupby(グループ化するカテゴリのある列名)
'''
@alt(グループ化する|集[約|計]する|分類する])

[データフレーム]_DataFrame_をグループ化する
'''

[データフレーム]_DataFrame_.groupby(by=[カラム名]_ColumnName_)
'''
@alt(ごと|毎|)
@alt(それぞれの|各|)

[カラム名]_ColumnName_のカテゴリごとにグループ化する
{[データフレーム]_DataFrame_を|[カラム名]_ColumnName_[の値|のカテゴリ|][によって|で]}グループ化する
'''

[データフレーム]_DataFrame_.groupby(by=[[カラム名]_ColumnName_, [カラム名]_ColumnName_])
'''
{[[データフレーム]_DataFrame_を|[カラム名]_ColumnName_と[カラム名]_ColumnName_][によって|で]}グループ化する
{[データフレーム]_DataFrame_を|[二つの|複数の][カラム名]_ColumnName_[によって|で]}グループ化する
'''

[データフレーム]_DataFrame_.groupby([カラム名]_ColumnName_, dropna=False)
'''
{[[データフレーム]_DataFrame_|[カラム名]_ColumnName_]を|欠損値を[含めて|省略せずに]}グループ化する
'''

[データフレーム]_DataFrame_.groupby(by=関数)
'''
{[データフレーム]_DataFrame_を|関数適用[によって|で]}グループ化する
'''

[データフレーム]_DataFrame_.groupby([カラム名]_ColumnName_).describe()
'''
@alt(要約統計量|記述統計量|[|基本]統計量)

[カラム名]_ColumnName_のカテゴリごとの要約統計量
{[データフレーム]_DataFrame_を|[カラム名]_ColumnName_[の値|][によって|で]}グループ化し、要約統計量
'''

dropna = True
'''
ただし、欠損値[は無視する|を含めない]
'''

dropna = False
'''
ただし、欠損値[も無視しない|[も|を]含める]
'''

[(name, group_[データフレーム]_DataFrame_) for name, group_[データフレーム]_DataFrame_ in [データフレーム]_DataFrame_.groupby([カラム名]_ColumnName_)]
'''
{[データフレーム]_DataFrame_を|[カラム名]_ColumnName_[の値|][によって|ごとに|で]}グループ化して、列挙する
'''

[name for name, _ in [データフレーム]_DataFrame_.groupby([カラム名]_ColumnName_)]
'''
[[データフレーム]_DataFrame_|[カラム名]_ColumnName_]をグループ化して、そのグループ名[の一覧|を列挙する]
'''

グループ名 = 'A'

[データフレーム]_DataFrame_.groupby([カラム名]_ColumnName_).get_group(グループ名)
'''
@alt(のカテゴリ|の値|)

[[データフレーム]_DataFrame_|[カラム名]_ColumnName_]をグループ化して、グループ名で取り出す
'''

[データフレーム]_DataFrame_.groupby([カラム名]_ColumnName_).size()
'''
[データフレーム]_DataFrame_をあるカラムのカテゴリで_グループ化して、それぞれのグループごとの件数を知る
'''

[データフレーム]_DataFrame_.groupby([カラム名]_ColumnName_).size()[s]
'''
[データフレーム]_DataFrame_を各column毎にグループ化して、sというグループの[個数|大きさ]
'''


[データフレーム]_DataFrame_.groupby([カラム名]_ColumnName_).__集約__
'''
@poly(__集約__;合計 sum();平均値 mean();個数 count();[最大値]_int_ max();[最小値]_int_ min();分散 var();標準偏差 std())

[[データフレーム]_DataFrame_|[カラム名]_ColumnName_]をグループ化して、[それぞれの|]__集約__
[カラム名]_ColumnName_のカテゴリごとの__集約__[|]
'''

[データフレーム]_DataFrame_.groupby(['列A', '列B'], as_index=False).__集約__
'''
[ふたつ|２つ|複数]のカラム[から|を組み合わせて|で_]グループ化し、[カラム名]_ColumnName_
'''

[データフレーム]_DataFrame_.groupby('列A')['列B'].__集約__
'''
[データフレーム]_DataFrame_をグループ化し、あるカラムに対し[カラム名]_ColumnName_
'''

[データフレーム]_DataFrame_.groupby('列A').describe()['列B']
'''
[データフレーム]_DataFrame_をグループ化し、あるカラムの要約統計量
'''
import pandas as pd

# 設定

print(pd.__version__)
'''
@alt(確認する|プリントし[|ておき]たい)
Pandasのバージョンを確認する
'''

pd.set_option('display.max_columns', n)
'''
@alt(表示可能な|表示できる|表示する|表示される)
@alt(変更する|設置する|増やする|表示される)

{データフレームの|[表示可能な|]}[最大|]列数を変更する
'''

pd.set_option('display.max_rows', n)
'''
{データフレームの|[表示可能な|]}[最大|]行数を変更する
'''

pd.set_option('precision', n)
'''
{データフレームの|[表示可能な|]}[|表示]精度を変更する
'''

pd.set_option('expand_frame_repr', False)
'''
[データフレームを表示するとき、|]折り返しをしない[|ようにする]
[データフレームを表示するとき、|]折り返しを[オフ|無効]に設定する
'''

pd.set_option('max_colwidth', n)
'''
[データフレームを表示するとき、|]カラムの最大幅をnに設定する
'''

pd.set_option('colheader_justify', 'right')
'''
[データフレームを表示するとき、|]ヘッダー行を右寄せに設定する
'''

pd.set_option('colheader_justify', 'left')
'''
[データフレームを表示するとき、|]ヘッダー行を左寄せに設定する
'''

# 読み込み系

index_col = n
'''
ただし、n番目のカラムをインデックスに設定する
'''

index_col = None
'''
ただし、インデックスを[自動的な|]連番に設定する
ただし、どのカラムもインデックスに[設定|]しない
'''

header = 0
'''
@alt(ヘッダ|カラムの名前)
ただし、[先頭の|最初の]行をヘッダに設定する
'''

header = None
'''
ただし、ヘッダを[自動的な|]連番に設定する
ただし、どの行もヘッダに[|設定]しない
'''

列名リスト = ['列A', '列B']

names = 列名リスト
'''
ただし、カラムの名前をリストで設定する
'''

usecols = names
'''
ただし、読みたい行番号をnamesで指定する
'''

skiprows = names
'''
ただし、[読み込まない|スキップする|無視する]列番号をnamesで指定する
'''

skipfooter = n
'''
ただし、[読み込まない|スキップする|無視する]フッタをnに設定する
'''
import pandas as pd

[データフレーム]_DataFrame_ = pd.DataFrame(
    data=[[1, 2, 3], [4, 5, 6]], columns=['列A', '列B', '列C'])

[カラム名]_ColumnName_ = 'A'


# オプション

inplace = True
'''
ただし、[値を置き換える|更新する]
ただし、破壊的に操作する
'''

na_position = 'first'
'''
<option>欠損値を先頭に[|来るように]する
'''

ascending = False
'''
<option>[降順|大きい順]にする
'''

ascending = True
'''
<option>[昇順|小さい順]にする
'''

_ = None

# 大雑把

[データフレーム]_DataFrame_.sort_values(by=[カラム名]_ColumnName_, ascending=_)
'''
@alt(ソートする|並べ直する|並べたい|整列する)

データフレームをソートする
'''

[データフレーム]_DataFrame_.sort_values(by=['列A', '列B'], ascending=_)
'''
{[データフレーム]_DataFrame_を|[二つの|複数の]列名[で|から|によって]}ソートする
'''

[データフレーム]_DataFrame_.sort_values(by=[カラム名]_ColumnName_, ascending=_)
'''
@alt(によって|で|を用いて|をキーにして)

{[データフレーム]_DataFrame_を|[カラム名]_ColumnName_によって}ソートする
'''

[データフレーム]_DataFrame_.sort_values(by=[[カラム名]_ColumnName_, [カラム名]_ColumnName_], ascending=_)
'''
{[データフレーム]_DataFrame_を|[カラム名]_ColumnName_と[カラム名]_ColumnName_によって}ソートする
'''

[データフレーム]_DataFrame_.sort_values(by=[カラム名]_ColumnName_, ascending=True)
'''
@alt(昇順に|小さい順に)
@alt(降順に|大きい順に)

{[カラム名]_ColumnName_を|昇順に}ソートする
{[データフレーム]_DataFrame_を|[カラム名]_ColumnName_によって|昇順に}ソートする
'''

[データフレーム]_DataFrame_.sort_values(by=[カラム名]_ColumnName_, ascending=False)
'''
{[カラム名]_ColumnName_を|降順に}ソートする
{[データフレーム]_DataFrame_を|[カラム名]_ColumnName_によって|降順に}ソートする
'''

[データフレーム]_DataFrame_.sort_values(by=[カラム名]_ColumnName_, na_position='first')
'''
[カラム名]_ColumnName_をNaNが先頭に[なる|来る]ようにソートする
{[データフレーム]_DataFrame_を|[カラム名]_ColumnName_によって}ソートして、NaNを先頭に[|来るように]する
'''


# 連携
[整数]_int_ = 10

[データフレーム]_DataFrame_.sort_values(by=[カラム名]_ColumnName_).head(_int_)
'''
@alt(上位|上の方)

[データフレーム]_DataFrame_をソートして、上位[_int_件|][[を|だけ|のみ]取り出する|欲しい]
'''

[データフレーム]_DataFrame_.sort_values(by=[カラム名]_ColumnName_).tail(_int_)
'''
@alt(下位|下の方)

[データフレーム]_DataFrame_をソートして、下位[_int_件|][[を|だけ|のみ]取り出する|欲しい]
'''

[データフレーム]_DataFrame_.sort_values(by=[カラム名]_ColumnName_).reset_index()
'''
[データフレーム]_DataFrame_をソートして、[新しい|上から]インデックスを[振り|付け]直する
'''

# ソートインデックス

[データフレーム]_DataFrame_.sort_index()
'''
{[データフレーム]_DataFrame_を|インデックスによって}ソートする
'''

[データフレーム]_DataFrame_.sort_index(ascending=True)
'''
{[データフレーム]_DataFrame_を|インデックスによって|昇順に}ソートする
'''

[データフレーム]_DataFrame_.sort_index(ascending=False)
'''
{[データフレーム]_DataFrame_を|インデックスによって|降順で}ソートする
'''

[データフレーム]_DataFrame_[[カラム名]_ColumnName_].value_counts().sort_index().index
'''
FIXME: カテゴリーデータを出現頻度順にソートする
'''
# 論理演算
_条件_ = True

_条件_ and _条件_
'''
@alt(二つ|ふたつ)
@alt(三つ|みっつ)

_条件_が二つとも[|同時に]成り立つ
_条件_と_条件_が[|同時に]成り立つ
_条件_かつ_条件_
'''

_条件_ and _条件_ and _条件_
'''
_条件_が三つとも[|同時に]成り立つ
[複数の|三つの]_条件_が[|同時に]成り立つ
_条件_かつ_条件_かつ_条件_
'''

_条件_ or _条件_
'''
@alt(いずれか|何れか|何か)

二つの_条件_[が|のうち]いずれか成り立つ
_条件_または_条件_
'''

_条件_ or _条件_ or _条件_
'''
[複数の|三つ]の_条件_[が|のうち]いずれか成り立つ
_条件_または_条件_または_条件_

'''

not _条件_
'''
[_条件_を|]否定する
'''

True
'''
真
'''

False
'''
偽
'''

None
'''
[null|NULL|nil]に等しい[値|識別子|もの]
未定値
'''
import sys


import os
'''
osモジュールをインポートする
'''

# os

os.sep
'''
@alt(ファイルパス|パス|ファイル名)
@alt(セパレータ|区切り)
ファイルパスのセパレータ記号
'''

os.getcwd()
'''
[[現在の|カレント|][作業|ワーキング]]ディレクトリ
'''

filepath = '/etc/man.conf'

os.chdir(os.dirname(filepath))
'''
@test(os=missing;$$)
{[[現在の|カレント|][作業|ワーキング]]ディレクトリを|filepathに}[変更する|[設定|]する]
'''

text = "echo 'A'"
os.system(text)
'''
@test(os=missing;text="echo 'A'";$$)
[UNIX|]コマンドtextを実行する
'''

filepath = '/etc/man.conf'

os.path.basename(filepath)
'''
@prefix(filepath;ファイル[|パス];)
filepathの[|拡張子付きの]ファイル名
filepathから[|拡張子付きの]ファイル名を[得る|取り出す]
'''

os.path.splitext(os.path.basename(filepath))[0]
'''
filepathの[拡張子なしの|ベース]ファイル名[を得る]
filepathから[拡張子なしの|ベース]ファイル名を[得る|取り出す]
'''

os.path.splitext(filepath)[1].lstrip('.')
'''
filepathの拡張子
'''

os.path.splitext(filepath)[0] + text
'''
filepathの拡張子をtextに変更する
'''

os.path.dirname(filepath)
'''
@alt(ディレクトリ|フォルダ)
filepathのディレクトリ名
filepathからディレクトリ名[を得る|取り出す]
'''

os.path.abspath(filepath)
'''
filepathの絶対[|ファイル]パス
filepathを絶対[|ファイル]パスに変換する
'''

os.path.split(filepath)
'''
filepathをディレクトリ名とファイル名に分割する
'''

os.path.splitext(filepath)
'''
filepathをベース名と拡張子に分割する
'''

filepath = "../"
filename = "file.txt"

os.path.join(filepath, filename)
'''
filepathとfilenameを結合する
'''


os.path.exists(filepath)
'''
filepathが[存在する|ある]かどうか
'''

not os.path.exists(filepath)
'''
filepathが[存在し|]ないかどうか
'''

os.path.get_size(filepath)
'''
filepathのファイルサイズ
'''

__file__ = 'file.py'

os.path.abspath(__file__)
'''
スクリプトファイルの[絶対|]パス
'''

os.path.dirname(os.path.abspath(__file__))
'''
スクリプトファイルのディレクトリ[名|パス]
'''

os.path.join(os.path.dirname(os.path.abspath(__file__)), filepath)
'''
スクリプトファイルと同じディレクトリのfilepathのパス
'''


open(filepath)
'''
@test(open=missing;$$)
@alt(オープンする|開く]
@alt(オープンして|開[いて|き]]
@alt(からの|から|の)
filepathをオープンする
filepathからの[入力|読み込み|]ストリームを得る
'''

file = open(filepath)
'''
@test(open=missing;$$;file)
filepathからストリームを読み込[み|んで]、fileとする
filepathからストリームをオープンして、fileとする
'''

__X__ = 'a'
open(filepath, mode=__X__)
'''
@test(open=missing;$$)
@X('r'|'rb'|'w'|'wb'|'a')
@Y(読み込み|バイナリ|書き込み|バイナリ書き込み|追加)
{filepathを|__Y__[モードで_|用に]}オープンする
{filepathを|__Y__できるように}オープンする
filepathをオープンして、__Y__ストリームを得る
'''

f = open(filepath, mode=__X__)
'''
@test(open=missing;$$)
{filepathを|__Y__[モードで_|用に]}オープンして、fとする
filepathから__Y__ストリームをオープンして、fとする
'''

mode = __X__
'''
@test($$;mode)
ただし、__Y__[モード|用]に設定する
ただし、__Y__モードを使う
'''


__X__ = 'utf-8'
open(filepath, encoding=__X__)
'''
@test(open=missing;$$)
@alt(エンコーディング|文字コード)
@X('utf-8'|'shift_jis'|'euc_jp'|'utf_8_sig'|text|s)
@Y(UTF8|SJIS|EUC|BOM付き|文字コードtext|sの示すエンコーディング)
{filepathを|__Y__で_}オープンする
'''

open(filepath, mode='w', encoding=__X__)
'''
@test(open=missing;$$)
{filepathを|__Y__で_|書き込み[用|できるよう]に}オープンする
'''

open(filepath, mode='a', encoding=__X__)
'''
@test(open=missing;$$)
{[既存の|]filepathを|__Y__で_|追加できるように}オープンする
'''

encoding = __X__
'''
@test($$;encoding)
ただし、エンコーディングを__Y__に設定する
ただし、__Y__を使う
'''

buffering = 0
'''
ただし、[バッファリングを無効にする|バッファを使用しない]
'''

n = 4096

buffering = 4096
'''
ただし、[バッファリング|バッファ]のサイズを[設定する|大きくする|小さくする]
'''

errors = 'strict'
'''
ただし、エラーがあるとき、例外を発生させる[ように設定する|]
'''

errors = 'ignore'
'''
ただし、エラーを無視する[ように設定する|]
'''

newline = __X__
'''
@X('\n';'\r';'\r\n';None)
@Y(UNIX;旧Mac;Windows;動作環境依存)

ただし、改行コードを__Y__に設定する
'''

f = Missing('f')

f.close()
'''
@alt(クローズする|閉じる|解放する)
@prefix(f;[ファイル|[入力|出力|]ストリーム])

fをクローズする
'''

f.read()
'''
@alt(読み込む|読む)

fを[全部、|全て]読み込む
'''

f.read(1)
'''
fから1[文字|バイト]、読み込む
'''

f.read(n)
'''
fからn[文字|バイト]、読み込む
'''

f.readlines()
'''
f全体を[行[単位で|]分割して|リストとして]読み込む
'''

[s.strip() for s in f.readlines()]
'''
f全体を[行[単位で|ごとに]分割して|]リストに変換する
'''

f.readline()
'''
fを一行ずつ読み込む
'''

f.readline()
'''
{fを|改行[を取り除いて|除外して|なしで]}一行ずつ読み込む
'''

s = ''
f.write(s)
'''
@prefix(f;[ファイル|[出力|]ストリーム])
@alt(書き込む|書く)

{fに|sを}書き込む
'''

x = 0
f.write(str(x))
'''
@test(f=missing;$$)
@alt(書き込む|書く)

{fに|xを文字列に[変換|]して}書き込む
'''

# プラットホーム依存なしに = 安全に | プラットホーム依存なしに | プラットホーム依存せずに |
# 新規に = 新しく | 新たに | 新規に
# ディレクトリ = ディレクトリ | フォルダ
# ファイルパス = ファイルパス | パス

# os.mkdir('dir/')
# '''
# [新規に]/{'dir/'のディレクトリ}を作る
# '''

# os.makedirs('dir/', exist_ok=True)
#    'dir/'のディレクトリを[再帰的に | 階層的に]作る

#    os.listdir('dir/')
#    'dir/'(ファイルパス)のファイル一覧

#    os.path.exists(p)
#    p(ファイルパス)が[存在する]かどうか

#    os.path.isdir(p)
#    p(ファイルパス)がディレクトリかどうか

#    os.path.isfile(p)
#    p(ファイルパス)がファイルかどうか

#    os.path.getsize('file.txt')
#    'file.txt'(ファイル名)の[ファイルサイズ | バイト数 | 大きさ]

#    os.path.join(p, p2)
#    {p(ファイルパス)とp2}を/[プラットホーム依存なしに]結合する
import math
import numbers

import fractions
'''
@alt(有理数|分数)

有理数が使用する
'''

[整数]_int_ = 1
_str_ = "1/2"
_数値_ = 0.5
[結果]_str_ = 1
_有理数_ = fractions.Fraction(1, 2)

分子, 分母 = 1, 2
fractions.Fraction(分子, 分母)
'''
有理数
'''

fractions.Fraction(numerator=_int_, denominator=_int_)
'''
分子_int_、分母_int_の有理数
'''

fractions.Fraction(_str_)
'''
_str_を有理数に変換する
'''

fractions.Fraction(_数値_)
'''
_数値_を有理数に変換する
'''

_有理数_.numerator
'''
_有理数_の分子
'''

_有理数_.denominator
'''
_有理数_の分母
'''

float(_有理数_)
'''
_有理数_を浮動小数点数に変換する
'''

math.ceil(_有理数_)
'''
_有理数_を切り上げたい
_有理数_の天井数
'''

math.floar(_有理数_)
'''
_有理数_を切り下げたい
_有理数_の床数
'''

fractions.Fraction(_数値_).limit_denominator()
'''
_数値_の{有理数|近似}
'''

fractions.Fraction(_数値_).limit_denominator(max_denominator=_int_)
'''
_数値_の{有理数|近似}。分母の[最大値]_int_は_int_
'''


isinstance([結果]_str_, numbers.Number)
'''
[結果]_str_が数かどうか
'''
import operator
# itertools

import itertools
'''
itertoolsモジュールをインポートする
'''

# 設定
[要素]_str_ = 10  # [文字列]
[整数]_int_ = 2
__イテレータ__ = [1, 2]
'''
@poly([要素]_str_;_int_;_str_)
@poly(__イテレータ__;_イテレータ_;_list_;[配列]_ndarray_)
'''

itertools.repeat(_int_)
'''
@alt(数列|[|整数]リスト)

[整数]_int_の無限[|な|の]数列
[整数]_int_が無限に続く数列
'''

itertools.repeat([要素]_str_)
'''
@alt(イテラブル|列|イテレータ)
@alt(無限に|いつまでも)
{[要素]_str_が|無限に}[繰り返す|続く]イテラブル
[要素]_str_の無限[|な|の]イテラブル
'''

itertools.repeat([要素]_str_, _int_)
'''
{[要素]_str_[が|を]|_int_回}[繰り返す|続く]イテラブル
'''

itertools.count()
'''
@alt(カウントアップする|数え上げたい)
無限にカウントアップする
[０から始まる|]無限[|な|の]数列
'''

itertools.count(start=_int_, step=1)
'''
[整数]_int_から始まる無限[|な|の]数列
'''

itertools.count(start=_int_, step=-1)
'''
{_int_から|無限に}カウントダウンする
'''

itertools.cycle(__イテレータ__)
'''
@alt(周期的に|循環的に|サイクリックに|ぐるぐると|何度も|無限に)

{__イテレータ__を|周期的に}結合する
'''

for x in itertools.cycle(__イテレータ__):
    print(x)
'''
{__イテレータ__[の要素|]を|周期的に}繰り返する
'''

itertools.accumulate(__イテレータ__)
'''
__イテレータ__を累加する
__イテレータ__を累加したイテレータ
'''

itertools.accumulate(__イテレータ__, operator.mul)
'''
__イテレータ__を累積する
__イテレータ__を__function__で累積したイテレータ
'''

itertools.chain(__イテレータ__, __イテレータ__)
'''
__イテレータ__と__イテレータ__を[連結する|つなぎたい|チェインする]
__イテレータ__に__イテレータ__を続けたい
__イテレータ__に__イテレータ__を続けた__イテレータ__
'''

itertools.compress(__イテレータ__, selectors=__イテレータ__)
'''
__イテレータ__[の要素|]をマスクする
__イテレータ__でマスクされた__イテレータ__
'''


def _function_(x): return True


itertools.takewhile(_function_, __イテレータ__)
'''
__イテレータ__[の要素|]を_function_で[残する|選びたい]
'''

itertools.dropwhile(_function_, __イテレータ__)
'''
__イテレータ__[の要素|]を_function_で[消する|除去する]
'''

itertools.zip_longest(__イテレータ__, __イテレータ__)
'''
@alt(ペアリングする|ペア化する|[zip|ジップ]する)
__イテレータ__と__イテレータ__をペアリングする
[不揃いな長さの|長さが一致しない[とき|バージョン]]のzip
'''

itertools.product(__イテレータ__, __イテレータ__)
'''
@alt(直積|デカルト積|全要素の[組み合わせ|ペア])
__イテレータ__と__イテレータ__の直積
'''

list(itertools.product(__イテレータ__, __イテレータ__))
'''
__イテレータ__と__イテレータ__の直積がリストとして欲しい
'''

itertools.product(__イテレータ__, repeat=2)
'''
同じ__イテレータ__[|自身]の直積
'''

for x, y in itertools(range(0, _int_), range(0, _int_)):
    print(x, y)
'''
二重ループを[シングル|単一]ループで書きたい
'''

list(itertools.product(range(_int_), range(_int_)))
'''
{_int_と_int_の全[組み合わせ|ペア]が|リストとして}欲しい
'''


itertools.permutations(__イテレータ__)
'''
__イテレータ__の全順列
'''

itertools.permutations(__イテレータ__, _int_)
'''
__イテレータ__[|自身]の長さ_int_の順列
'''

list(itertools.permutations(__イテレータ__))
'''
__イテレータ__の全順列をリストにする
'''

list(itertools.permutations(__イテレータ__, _int_))
'''
__イテレータ__[|自身]の長さ_int_の順列をリストにする
'''

# コンビネーション

itertools.combinations(__イテレータ__, 2)
'''
@alt(コンビネーション|組み合わせ)
__イテレータ__のコンビネーション
'''

itertools.combinations_with_replacement(__イテレータ__, 2)
'''
__イテレータ__の重複コンビネーション
'''

list(itertools.combinations(__イテレータ__, 2))
'''
@alt(コンビネーション|組み合わせ)
__イテレータ__のコンビネーション[をリストにする|_list_[で|として]欲しい]
'''

list(itertools.combinations_with_replacement(__イテレータ__, 2))
'''
__イテレータ__の重複コンビネーション[をリストにする|_list_[で|として]欲しい]
'''


itertools.combinations(__イテレータ__, _int_)
'''
__イテレータ__の長さ_int_のコンビネーション
'''

itertools.combinations_with_replacement(__イテレータ__, _int_)
'''
__イテレータ__の長さ_int_の重複コンビネーション
'''

for x, y in itertools.combinations(__イテレータ__, 2):
    print(x, y)
'''
__イテレータ__のコンビネーションを繰り返する
'''

for x, y in itertools.combinations_with_replacement(__イテレータ__, 2):
    print(x, y)
'''
__イテレータ__の重複コンビネーションを繰り返する
'''

for pairs in itertools.combinations(__イテレータ__, _int_):
    print(pairs)
'''
__イテレータ__の長さ_int_のコンビネーションを繰り返する
'''

for pairs in itertools.combinations_with_replacement(__イテレータ__, _int_):
    print(pairs)
'''
__イテレータ__の長さ_int_の重複コンビネーションを繰り返する
'''
import io

import json
'''
@alt(形式|フォーマット)
JSONを使う
'''

_str_ = "{'A':1}"
_JSONLファイル_ = 'file.jsonl'
_バイト列_ = b"{'A':1}"
_dict_ = {'A': 0}
_list_ = [1, 2, 3]

# ファイル入力 = io.StringIO(_str_)
# ファイル出力 = io.StringIO(mode='w')
# n = 0
# '''
# @alt(ファイル入力|入力ストリーム|入力)
# @alt(ファイル出力|出力ストリーム|出力)
# '''


__ファイル名__ = 'file.json'
__データ__ = _str_
'''
@poly(__データ__;_dict_;_list_;_tuple_;[結果]_str_)
@poly(__ファイル名__;_JSONファイル_;ファイル名)
'''

with open(__ファイル名__) as f:
    data = json.load(f)
'''
@alt(読みたい|読み込みたい|ロードする)
@alt(構文解析する|パースする|デコードする)

__ファイル名__からJSON[形式のデータ|]を読みたい
JSON[形式の|]ファイルを構文解析する
'''

with open(_JSONLファイル_) as f:
    ss = []
    for line in f.readlines():
        data = json.loads(line)
        ss.append(data)
'''
_JSONLファイル_からJSON[形式のデータ|]を読みたい
JSON[形式の|]ファイルを構文解析する
'''

data = json.loads(_str_)
'''
_str_からJSON[形式のデータ|]を読みたい
JSON[形式の|]文字列を構文解析する
JSON[形式の|]文字列を[辞書|オブジェクト|データ]に変換する
'''

json.loads(_バイト列_.decode('unicode-escape'))
'''
_バイト列_からJSON[形式のデータ|]を読みたい
JSON[形式の|]バイト列を構文解析する
'''

json.dumps(__データ__, ensure_ascii=False)
'''
__データ__をJSON[形式の|]文字列に変換する
__データ__をJSON[形式|]にエンコードする
'''

json.dumps(__データ__, ensure_ascii=False, indent=4)
'''
{インデント[|幅]を指定して|__データ__を}JSON文字列に変換する
{__データ__を|インデント[|幅]を指定して}JSON[形式|]にエンコードする
'''

json.dumps(__データ__, ensure_ascii=False, sort_keys=True)
'''
{__データ__を|ソートして}JSON[形式|]にエンコードする
'''

with open(__ファイル名__, 'w') as f:
    json.dump(__データ__, f, ensure_ascii=False)
'''
{__データ__を|JSON形式で}__ファイル名__に[保存する|出力する|ダンプする]
'''

with open(_JSONLファイル_, 'w') as f:
    for data in _list_:
        s = json.dumps(data, ensure_ascii=False)
        print(s, file=f)
'''
_list_の[要素|データ]をJSON形式に[一行|ひとつ]ずつ変換し、[保存する|出力する]
{[リスト]_list_を|JSON[L|]形式で}_JSONLファイル_に[保存する|出力する]
'''
# math

import math
'''
[math[|モジュール]|算術計算ライブラリ]を[インポートする|使用する]
'''

[整数]_int_ = 2
[整数]_int_, [整数]_int_ = 1.5, 3.1
# __int__, __整数3__ = 1, 3, 7
'''
@poly([整数]_int_;_int_;_数値_;[結果]_str_)
@poly([整数]_int_;_int_;_数値_;[結果]_str_)
'''

math.sqrt([整数]_int_)
'''
@alt(が計算する||がほしい)
[[整数]_int_の|][平方根|ルート|スクエアルート]が計算する
'''

math.ceil([整数]_int_)
'''
[[整数]_int_の|][天井|天井数]が計算する
[整数]_int_以上の最小の整数が計算する
[[整数]_int_を|]切り上げて整数に変換する
[整数]_int_[の少数|]を切り上げたい
'''

math.floor([整数]_int_)
'''
[[整数]_int_の|][床|床数]が計算する
[整数]_int_以下の最大の整数が計算する
[[整数]_int_を|]切り下げて整数に変換する
[整数]_int_[の少数|]を切り下げたい
'''

math.gcd(_int_, _int_)
'''
@alt(最大公約数|GCD)

[自然数|_int_と_int_|２つの[_int_|自然数]]の最大公約数が計算する
'''

math.lcm(_int_, _int_)
'''
@alt(最小公倍数|LCM)

[自然数|_int_と_int_|２つの_int_]最小公倍数が計算する
'''

math.gcd(_int_, _int_, _int_)
'''
[３|三][つの|]_int_の最大公約数が計算する
'''

math.lcm(_int_, _int_, _int_)
'''
[３|三][つの|]_int_の最小公倍数が計算する
'''

k = 2

math.comb(_int_, _int_)
'''
@alt(コンビネーション|[組合せ|組み合わせ]|nCk)
[_int_と_int_の|]コンビネーションが計算する
[整数]_int_個の集まりから_int_個[重複なく|]選ぶ方法を計算する
異なる_int_個のものから_int_個選ぶ場合の数
'''

math.copysign([整数]_int_, [整数]_int_)
'''
[整数]_int_の符号を同じにする
[整数]_int_の符号をコピーにする
'''

math.fabs([整数]_int_)
'''
[整数]_int_の絶対値が計算する
'''

math.factorial(_int_)
'''
[_int_の|]階乗が計算する
'''

math.frexp([整数]_int_)[0]
'''
[整数]_int_の仮数[|部[|分]]
'''

math.frexp([整数]_int_)[1]
'''
[整数]_int_の指数[|部[|分]]
'''

math.isclose([整数]_int_, [整数]_int_)
'''
２つの[整数]_int_[が|は][十分に近い|近似値|ほぼ等しい]かどうか
'''

math.isfinite([整数]_int_)
'''
[整数]_int_[が|は]有限かどうか
'''

math.isinf([整数]_int_)
'''
[整数]_int_[が|は]無限大かどうか
'''

math.isnan([整数]_int_)
'''
[整数]_int_[が|は][NaN|非数]かどうか
'''

math.modf([整数]_int_)[0]
'''
[整数]_int_の小数[部[|分]|]
'''

math.modf([整数]_int_)[1]
'''
[整数]_int_の整数[部[|分]|]
'''

math.perm(_int_)
'''
@(総数|数)
[整数]_int_の[順列|並べ方]の総数が計算する
'''

math.perm(_int_, _int_)
'''
@alt(とき|時|場合)
[整数]_int_個から_int_個取り出したときの[順列|並べ方]の総数が計算する
[整数]_int_個のものから_int_個取り出したときの並べ方[の総数|]が計算する
'''

# math.prod(l)
# @type(l, リスト)の要素積

math.remainder([整数]_int_, [整数]_int_)
'''
[整数]_int_を[整数]_int_で割った剰余が計算する
'''

math.exp([整数]_int_)
'''
[e|自然対数の底|ネイピア数]の[整数]_int_乗が計算する
[e|自然対数の底|ネイピア数]の乗数が計算する
'''

math.log([整数]_int_)
'''
[[整数]_int_の|]自然対数が計算する
'''

math.log([整数]_int_, _int_)
'''
{_int_を底とする|[[整数]_int_の|]}対数が計算する
[[整数]_int_の|]_int_進対数が計算する
'''

math.log2([整数]_int_)
'''
[[整数]_int_の|][二進|２進|バイナリ]対数が計算する
２を底と[した|する][[整数]_int_の|]対数が計算する
'''

math.log10([整数]_int_)
'''
[[整数]_int_の|]常用対数が計算する
'''

math.cos([整数]_int_)  # 単位はラジアン
'''
[[整数]_int_の|][余弦|コサイン|cos]が計算する
'''

math.sin([整数]_int_)  # 単位はラジアン
'''
[[整数]_int_の|][正弦|サイン|sin]が計算する
'''

math.tan([整数]_int_)  # 単位はラジアン
'''
[[整数]_int_の|][正接|タンジェント|tan]が計算する
'''

math.acos([整数]_int_)
'''
[[整数]_int_の|][逆余弦|アークコサイン]が計算する
[[整数]_int_の|][余弦|コサイン|cos][の逆数|からラジアン]が計算する
'''

math.asin([整数]_int_)
'''
[[整数]_int_の|][逆正弦|アークサイン]が計算する
[[整数]_int_の|][正弦|サイン|sin][の逆数|からラジアン]が計算する
'''

math.atan([整数]_int_)
'''
[[整数]_int_の|][逆正接|アークタンジェント]が計算する
[[整数]_int_の|][正接|タンジェント|tan][の逆数|からラジアン]が計算する
'''

math.degrees([整数]_int_)  # 単位はラジアン
'''
[ラジアン|[整数]_int_]の角度が計算する
'''

math.radians([整数]_int_)  # 単位は弧度法
'''
[[整数]_int_の|]ラジアンが計算する
'''

math.acosh([整数]_int_)
'''
[[整数]_int_の|]逆双曲線余弦が計算する
[[整数]_int_の|][双曲線余弦|ハイパボリック・コサイン]の逆数が計算する
'''

math.asinh([整数]_int_)
'''
[[整数]_int_の|]逆双曲線正弦が計算する
[[整数]_int_の|][双曲線正弦|ハイパボリック・サイン]の逆数が計算する
'''

math.atanh([整数]_int_)
'''
[[整数]_int_の|]逆双曲線正接が計算する
[[整数]_int_の|][双曲線正接|ハイパボリック・タンジェント]の逆数が計算する
'''

math.cosh([整数]_int_)  # 単位はラジアン
'''
[[整数]_int_の|]の[双曲線余弦|ハイパボリック・コサイン]が計算する
'''

math.sinh([整数]_int_)  # 単位はラジアン
'''
[[整数]_int_の|]の[双曲線正弦|ハイパボリック・サイン]が計算する
'''

math.tanh([整数]_int_)  # 単位はラジアン
'''
[[整数]_int_の|][双曲線正接|ハイパボリック・タンジェント]が計算する
'''


_list_ = (1, 2)
_list_ = (0, 1)

math.dist(_list_, _list_)
'''
[[２|]point間の|]ユークリッド距離が計算する
'''

math.hypot([整数]_int_, [整数]_int_)
'''
[整数]_int_と[整数]_int_の[斜辺|ノルム]が計算する
原点からの|点までの]距離が計算する
'''

math.gamma([整数]_int_)
'''
ガンマ関数を計算する
ガンマ関数の値が計算する
'''

math.lgamma([整数]_int_)
'''
ガンマ関数の絶対値に自然対数をとった値が計算する
'''

math.pi
'''
[円周率|π]
'''

math.e
'''
[ネイピア数|自然対数の底]
'''

math.inf
'''
無限大
'''

- math.inf
'''
無限小
'''

math.nan
'''
[NaN|非数]
'''
import random
import string

random.seed()
'''
@alt(乱数シード|乱数[|生成[|系]列])

乱数シードを初期化する
乱数[|の[発生|生成]]を毎回異なるように[|初期化]する
{[時刻で|毎回異なるように]|乱数シードを}初期化する
'''

random.seed(42)
'''
乱数シードを固定[|化]する
乱数[|の[発生|生成]]を毎回同じように[|初期化]する
{毎回同じ乱数が発生するように|乱数シードを}初期化する
'''

[整数]_int_ = 42

random.seed(_int_)
'''
{乱数シードを|_int_で}初期化する
{乱数シードを|_int_で}固定[|化]する
'''


[最小値]_int_, [最大値]_int_ = 0, 10
[整数]_int_, _int_ = 0, 10

random.randint([最小値]_int_, [最大値]_int_)  # 範囲を指定
'''
@alt(範囲|[最大値]_int_[|・][最小値]_int_|上限下限)

ランダムな整数
[範囲内の|][整数|]乱数
範囲を[指定して|与えて][整数|]乱数を生成する
'''

random.randint(_int_, _int_)
'''
ランダムな整数。範囲は_int_から_int_まで
[整数|]乱数。範囲は_int_から_int_まで
乱数。乱数は整数、範囲は_int_から_int_の間
'''

random.randint(1, 6)
'''
@alt(整数乱数|ランダムな整数[|値])
@alt(を生成する|)
@alt(を振りたい||が作成する)

サイコロ[|を振りたい]
サイコロと同じ乱数[|を生成する]
'''


初項, 終項, 公差 = 0, 10, 2

random.randrange(初項, 終項, 公差)
'''
[等差]_int_数列から[整数|]乱数を生成する
'''

random.random()
'''
@alt(実数|少数[|点数]|浮動少数点数)

[疑似|][乱数|ランダムな数]
'''

random.uniform([最小値]_int_, [最大値]_int_)  # 範囲を指定
'''
一様[|な][|疑似]乱数を生成する
'''

平均値 = 0.5
標準偏差 = 0.2

random.normalvariate(mu=平均値, sigma=標準偏差)
'''
{正規分布[から|で|を用いて]|[|疑似]乱数を}生成する
{平均[|値]と標準偏差[を与えて|から]|[|疑似]乱数}を生成する
'''

_list_ = [1, 2, 3, 3]
_str_ = 'ABC'
_tuple_ = ('A', 'B')

random.choice(_list_)
'''
@alt(選びたい|[選|乱]択する|取り出する)

{[リスト]_list_から|[一つ|1個]|ランダムに|[|要素を]}選びたい
'''

random.choice(_str_)
'''
@alt(選びたい|[選|乱]択する|取り出する)

{_str_から|１文字|ランダムに|}選びたい
'''

random.choice(string.ascii_uppercase)
'''
{[アルファベット|英大文字]から|[一つ|１文字]|ランダムに}選びたい
'''

random.choices(_list_, k=n)  # nに個数指定
'''
_list_から[複数個|n個]、ランダムに[選びたい|抽出する]
'''

標本個数 = 2

random.sample(_list_, 標本個数)
'''
@alt(サンプリングする|標本抽出する)

_list_からサンプリングする
'''

random.sample(_list_, k=n)
'''
_list_からn[個|要素]、[重複なく|]サンプリングする
_list_から複数の要素をランダムに[重複なく|][抽出する|選びたい]
_list_から重複なく、n[個|要素][ランダムに][選びたい|抽出する]
'''

random.sample(range(100), 10)
'''
ランダムな整数のリスト
'''

random.shuffle(_list_)
'''
@alt(の順序=[|の順[序|番|]])
@alt(シャッフルする|ランダムに入れ替えたい)

{[リスト]_list_の順序を|[ランダムに|]}シャッフルする
'''


''.join(random.sample(_str_, len(_str_)))
'''
{_str_の順序を|[|ランダムに]}シャッフルする
'''


tuple(random.sample(_tuple_, len(_tuple_)))
'''
{_tuple_の順序を|[|ランダムに]}シャッフルする
'''
import numpy as np
import pandas as pd
import sklearn
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split

[データフレーム]_DataFrame_ = pd.DataFrame()
[カラム名]_ColumnName_ = 'A'

目的変数 = [データフレーム]_DataFrame_[[カラム名]_ColumnName_]
'''
[データフレーム]_DataFrame_の[カラム名]_ColumnName_を目的変数にする
[データフレーム]_DataFrame_から説明変数を選びたい
'''

説明変数 = [データフレーム]_DataFrame_[[[カラム名]_ColumnName_]]
'''
[データフレーム]_DataFrame_の_[カラム名]_ColumnName_[だけ|のみ|を]説明変数にする
'''

説明変数 = [データフレーム]_DataFrame_[[[カラム名]_ColumnName_, [カラム名]_ColumnName_]]
'''
[カラム名]_ColumnName_と[カラム名]_ColumnName_を説明変数にする
２つの[カラム名]_ColumnName_を説明変数にする
[データフレーム]_DataFrame_から説明変数を選びたい
'''

説明変数= [データフレーム]_DataFrame_[[データフレーム]_DataFrame_.columns[: -1]]
'''
[データフレーム]_DataFrame_の最後の[列|カラム]以外を[全て|]説明変数にする
'''

説明変数 = [データフレーム]_DataFrame_[[データフレーム]_DataFrame_.columns[1:]]
'''
[データフレーム]_DataFrame_の[先頭|最初]の[列|カラム]以外を[全て|]説明変数にする
'''

model = sklearn.linear_model.LinearRegression()
'''
@alt(線形回帰モデル=[線形回帰モデル|[単|重]回帰モデル|[線形|回帰]モデル])
@alt(用意する|準備する)
@alt(作成する|[新規|]作成する)

[新しい|空の|]線形回帰モデルを[作成する|用意する]
[線形|単|重|]回帰分析[の準備をする|を行いたい]
'''

normalize = True
'''
ただし、{説明変数を|事前に}正規化する
'''

fit_intercept = False
'''
ただし、[切片|バイアス]を[算出|計算]しない
'''

正則化項 = 0.1

model = sklearn.linear_model.Ridge(alpha=0.1)  # alphaは正則化項
'''
[新しい|空の|]リッジ回帰モデルを[作成する|用意する]
リッジ回帰分析[の準備をする|を行いたい]
'''

model = sklearn.linear_model.Rosso(alpha=0.1)  # alphaは正則化項
'''
[新しい|空の|]ロッソ回帰モデルを[作成する|用意する]
ロッソ回帰分析[の準備をする|を行いたい]
'''

model = sklearn.linear_model.ElasticNet()
'''
@alt(ハイブリッド|組み合わせた)

[新しい|空の|]リッジ回帰とロッソ回帰のハイブリットモデルを[作成する|用意する]
リッジ回帰とロッソ回帰のハイブリッド分析[の準備をする|を行いたい]
正則化付き線形回帰モデルを[作成する|用意する]
正則化付き[線形|単|重|]回帰分析[の準備をする|を行いたい]
'''

model.fit(説明変数, 目的変数)
'''
@alt(予測モデル=[モデル|回帰モデル|分類モデル])
@alt(教師データ|データ|訓練データ)

予測モデルを[学習する|作成する|訓練する]
{教師データで|予測モデル}を学習する
{説明変数と目的変数で|予測モデルを}学習する
予測モデルの[当てはめを実行する|訓練を開始する]
予測モデルを[当て|あて]はめたい
'''

model = sklearn.linear_model.LinearRegression()
model.fit(説明変数, 目的変数)
'''
[線形|単|重]回帰モデルを[学習する|作成する|訓練する]
'''


model.coef_
'''
@alt(回帰変数|係数)

線形[|回帰]モデルの回帰変数[|を得る]
'''

model.intercept_
'''
@alt(切片|バイアス)

線形[|回帰]モデルの切片[|を得る]
'''

model = sklearn.linear_model.LinearRegression(fit_intercept=False)
'''
切片なしの線形回帰モデルを[作成する|用意する]
切片なしの[線形|単|重|]回帰分析[の準備をする|を行いたい]
'''

y_pred = model.predict(説明変数)
'''
予測モデルから目的変数を予測する
'''

pd.DataFrame({'実測': 目的変数, '予測': model.predict(説明変数)})
'''
@alt(実測値|目的変数)
{予測モデルの予測値と|実測値を}[比較する|対比させる]
'''

plt.scatter(目的変数, model.predict(説明変数))
'''
{予測モデルの予測値と|実測値を}散布図に描く
'''

目的変数 - model.predict(説明変数)
'''
予測モデルの残差
'''

plt.hist(目的変数 - model.predict(説明変数))
'''
予測モデルの残差をヒストグラムにする
'''

sklearn.metrics.mean_absolute_error([データ列]_ndarray_, _ndarray_)
'''
[データ列[間|]の|][平均絶対誤差|MAE]
'''

np.sqrt(sklearn.metrics.mean_squared_error([データ列]_ndarray_, _ndarray_))
'''
[データ列[間|]の|][平方根平均二乗誤差|RMSE]
'''

sklearn.metrics.mean_squared_error([データ列]_ndarray_, _ndarray_)
'''
[データ列[間|]の|]平均[二|２]乗誤差
[MSE|Mean Squared Error]
'''

sklearn.metrics.mean_squared_error(目的変数, model.predict(説明変数))
'''
予測モデルの[平均[二|２]乗誤差|精度|正確さ]
'''

sklearn.metrics.r2_score([データ列]_ndarray_, _ndarray_)
'''
@alt(決定係数|R2|[当て|あて]はまりの良さ|寄与率)
[データ列[間|]の|]決定係数
'''

sklearn.metrics.r2_score(目的変数, model.predict(説明変数))
'''
予測モデルの[当てはまりの良さ|決定係数]
'''

X_train, X_test, y_train, y_test = train_test_split(説明変数, 目的変数, test_size=0.3)
'''
ホールドアウト[法|]を使う
訓練データとテストデータに分割する
'''


sklearn.model_selection.cross_val_score(model, 説明変数, 目的変数, cv=5, scoring='r2')
'''
@alt(交差検証|クロスバリデーション)
回帰モデルを交差検証する
'''


model = sklearn.tree.DecisionTreeRegressor()
'''
[新しい|空の|]回帰木モデルを[作成する|用意する]
回帰木分析[の準備をする|を行いたい]
'''

sklearn.tree.plot_tree(model, feature_names=X.columns, filled=True)
'''
@alt(決定木|回帰木|分類木)

決定木を表示する
決定木を[可視化|グラフ[化|に]]する
'''

plt.barh(X.columns, model.feature_importances_)
'''
@alt(決定木|回帰木|分類木)

決定木の重要度を表示する
決定木の重要度を[可視化|グラフ[化|に]]する
'''

n = 2

maxdepth = n
'''
ただし、[決定木の|][深さを制限する|最大深さを設定する]
'''

# クラス分類

model = sklearn.linear_model.LogisticRegression()
'''
[新しい|空の|]ロジスティック回帰モデルを[作成する|用意する]
線形のクラス分類[をする|を行いたい]
'''

混同行列 = sklearn.metrics.confusion_matrix(正解データ列, 予測データ列)
'''
@alt(クラス分類結果=[クラス分類|[分類|予測]結果|分類モデル])

クラス分類結果の[予測精度|偽陽性|偽陰性|真陽性|真陰性]を見る
[予測データの|][混同行列|コンフュージョン・マトリックス]を[求めたい|算出する]
'''

sns.heatmap(混同行列, annot=True, cmap='Reds')
'''
{混同行列を|ヒートマップで}確認する
'''

sns.heatmap(confusion_matrix(正解データ列, 予測データ列), annot=True, cmap='Reds')
'''
{クラス分類の[予測精度|偽陽性|偽陰性]を|ヒートマップで}見る
'''

sklearn.metrics.accuracy_score(正解データ列, 予測データ列)
'''
クラス分類結果の[正解率|正確さ|アキュレシー|分類精度]
'''

sklearn.metrics.precision_score(正解データ列, 予測データ列)
'''
クラス分類結果の[適合率|PPV]
偽陽性を[避けたい|抑えたい]指標を使う
'''

sklearn.metrics.recall_score(正解データ列, 予測データ列)
'''
クラス分類結果の[再現率|リコール|真陽性率|感度]
偽陰性を[避けたい|抑えたい]指標を使う
'''

sklearn.metrics.f1_score(正解データ列, 予測データ列)
'''
クラス分類結果の[F値|適合率と再現率の調和平均]
'''


# 回帰

model = sklearn.ensemble.RandomForestRegressor(n_estimators=10)  # ランダム性
model.fit(説明変数, 目的変数)
'''
@alt(を使って|を用いて|で)
{ランダムフォレストを使って|回帰分析を}[行いたい|する]
'''


model = sklearn.svm.SVR(kernel='rbf', C=1e3, gamma=0.1, epsilon=0.1)
model.fit(説明変数, 目的変数)
'''
{サポートベクターマシンを使って|回帰分析を}[行いたい|する]
'''

model = sklearn.gaussian_process.GaussianProcessRegressor()
model.fit(説明変数, 目的変数)
'''
{ガウス過程を使って|回帰分析を}[行いたい|する]
'''

model = sklearn.neighbors.KNeighborsRegressor(n_neighbors=5)
model.fit(説明変数, 目的変数)
'''
{[K最近傍法|KNN]で|回帰分析を}[行いたい|する]
'''

model = sklearn.linear_model.SGDRegressor()
model.fit(説明変数, 目的変数)
'''
{[確率的勾配降下|SDG]で|回帰分析を}[行いたい|する]
'''

model = sklearn.neural_network.MLPRegressor(hidden_layer_sizes=(10, 10))
model.fit(説明変数, 目的変数)
'''
{[パーセプトロン|ニューラルネット|多層パーセプトロン|MLP]で|回帰分析を}[行いたい|する]
'''

model = sklearn.cross_decomposition.PLSRegression(n_components=10)
model.fit(説明変数, 目的変数)
'''
[|新しい|空の]部分的最小二乗回帰モデルを[作成する|用意する]
{[部分的最小二乗法|PLS]で|回帰分析を}[行いたい|する]
'''

model = sklearn.linear_model.RANSACRegressor(random_state=0)
model.fit(説明変数, 目的変数)
'''
[|新しい|空の]ロバスト回帰モデルを[作成する|用意する]
{[ロバスト推定|RANSAC]で|回帰分析を}[行いたい|する]
'''

model = sklearn.linear_model.HuberRegressor()
model.fit(説明変数, 目的変数)
'''
[ロバストな|外れ値に強い]線形回帰モデルを[作成する|用意する]
[ロバストな|外れ値に強い][線形|単|重|]回帰分析[の準備をする|を行いたい]
'''

model = sklearn.ensemble.GradientBoostingRegressor()
model.fit(説明変数, 目的変数)
'''
[|新しい|空の]勾配ブースティング回帰木を[作成する|用意する]
{勾配ブースティングで|回帰分析を}[行いたい|する]
'''

model = sklearn.ensemble.HistGradientBoostingRegressor()
model.fit(説明変数, 目的変数)
'''
[|新しい|空の]ヒストグラムベースの勾配ブースティング回帰木を[作成する|用意する]
{ヒストグラムと勾配ブースティングで|回帰分析を}[行いたい|する]
'''

model = sklearn.ensemble.AdaBoostRegressor(random_state=0, n_estimators=100)
model.fit(説明変数, 目的変数)
'''
{ブースティングで|回帰分析を}[行いたい|する]
'''

model = sklearn.ensemble.BaggingRegressor(n_estimators=10)
model.fit(説明変数, 目的変数)
'''
{バギングで|回帰分析を}[行いたい|する]
'''

sklearn.ensemble.VotingRegressor()
model.fit(説明変数, 目的変数)
'''
{アンサンブル学習で|回帰分析を}[行いたい|する]
'''

sklearn.ensemble.StackingRegressor()
model.fit(説明変数, 目的変数)
'''
{スタッキングで|回帰分析を}[行いたい|する]
'''

# 分類器

model = sklearn.ensemble.RandomForestClassifier()
model.fit(説明変数, 目的変数)
'''
{ランダムフォレストで|クラス分類を}[行いたい|する]
'''

model = sklearn.ensemble.ExtraTreeClassifier(n_estimators=10)
model.fit(説明変数, 目的変数)
'''
{[ランダム性を強化した|よりランダムな]ランダムフォレストで|クラス分類を}[行いたい|する]
'''

model = sklearn.svm.SVR(kernel='rbf', C=1e3, gamma=0.1, epsilon=0.1)
model.fit(説明変数, 目的変数)
'''
@alt(分類モデル|分類器)

[|新しい]サポート[ベクター|ベクトル]分類モデルを[作成する|用意する]
{サポートベクターマシンで|クラス分類を}[行いたい|する]
'''

model = sklearn.gaussian_process.GaussianProcessClassifier()
model.fit(説明変数, 目的変数)
'''
[|新しい|空の]ガウス過程分類モデルを[作成する|用意する]
{ガウス過程で|クラス分類を}[行いたい|する]
'''

model = sklearn.neighbors.KNeighborsClassifier(n_neighbors=5)
model.fit(説明変数, 目的変数)
'''
{[K最近傍法|KNN]で|クラス分類を}[行いたい|する]
'''

model = sklearn.linear_model.SGDClassifier()
model.fit(説明変数, 目的変数)
'''
{[確率的勾配降下|SDG]で|クラス分類を}[行いたい|する]
'''

model = sklearn.neural_network.MLPClassifier(hidden_layer_sizes=(10, 10))
model.fit(説明変数, 目的変数)
'''
{[パーセプトロン|ニューラルネット|多層パーセプトロン|MLP]で|クラス分類を}[行いたい|する]
'''

model = sklearn.linear_model.RANSACClassifier(random_state=0)
model.fit(説明変数, 目的変数)
'''
[|新しい|空の]ロバスト分類モデルを[作成する|用意する]
{[ロバスト推定|RANSAC]で|クラス分類を}[行いたい|する]
'''

model = sklearn.linear_model.HuberClassifier()
model.fit(説明変数, 目的変数)
'''
[ロバストな|外れ値に強い]線形分類モデルを[作成する|用意する]
[ロバストな|外れ値に強い][線形|単|重|]クラス分類[の準備をする|を行いたい]
'''

model = sklearn.ensemble.GradientBoostingClassifier()
model.fit(説明変数, 目的変数)
'''
[|新しい|空の]勾配ブースティング分類木を[作成する|用意する]
{勾配ブースティングで|クラス分類を}[行いたい|する]
'''

model = sklearn.ensemble.HistGradientBoostingClassifier()
model.fit(説明変数, 目的変数)
'''
[|新しい|空の]ヒストグラムベースの勾配ブースティング分類木を[作成する|用意する]
{ヒストグラムと勾配ブースティングで|クラス分類を}[行いたい|する]
'''

model = sklearn.ensemble.AdaBoostClassifier(random_state=0, n_estimators=100)
model.fit(説明変数, 目的変数)
'''
{ブースティングで|クラス分類を}[行いたい|する]
'''

model = sklearn.ensemble.BaggingClassifier(n_estimators=10)
model.fit(説明変数, 目的変数)
'''
{バギングで|クラス分類を}[行いたい|する]
'''

sklearn.ensemble.VotingClassifier()
model.fit(説明変数, 目的変数)
'''
{アンサンブル学習で|クラス分類を}[行いたい|する]
'''

sklearn.ensemble.StackingClassifier()
model.fit(説明変数, 目的変数)
'''
{スタッキングで|クラス分類を}[行いたい|する]
'''


# 教師なし

model = sklearn.decomposition.PCA(n_components=n)
'''
[主成分分析|固有値分解|因子分析|スペクトル分解][を行いたい|の準備をする]
'''

sklearn.decomposition.PCA(n_components=_int_).fit_transform(多次元データ)
'''
{[多次元データを|]|主成分分析で}_int_次元に[次元|]削減する
'''

model = sklearn.decomposition.TruncatedSVD(n_components=n)
'''
[特異値分解|SVD][を行いたい|の準備をする]
'''

sklearn.decomposition.TruncatedSVD(n_components=_int_).fit_transform(多次元データ)
'''
{[多次元データを|]|[特異値分解|SVD]で}_int_次元に[次元|]削減する
'''

model = sklearn.manifold.MSD(n_components=n)
'''
[多次元尺度構成法|MSD][を行いたい|の準備をする]
'''

sklearn.manifold.MSD(n_components=_int_).fit_transform(多次元データ)
'''
{[多次元データを|]|[多次元尺度構成法|MSD]で}_int_次元に[次元|]削減する
'''

model = sklearn.manifold.TSNE(n_components=n)
'''
[[フィッシャーの|]線形判別分類|t-SNE|t分布型確率的近傍埋め込み法][を行いたい|の準備をする]
'''

sklearn.manifold.TSNE(n_components=_int_).fit_transform(多次元データ)
'''
{[多次元データを|]|[t-SNE|t分布型確率的近傍埋め込み法]で}_int_次元に[次元|]削減する
'''

sklearn.preprocessing.StandardScaler().fit_transform(データ)
'''
@alt(スケール変換|スケーリング)

[データを|][標準化|スケール変換]する
{[データを|]|平均と分散で}標準化を行いたい
'''

sklearn.preprocessing.RobustScaler().fit_transform(データ)
'''
[データを|]外れ値に[頑健な|ロバストな]標準化を行いたい
{[データを|]|四分位点で}[標準化|スケール変換]する
'''

sklearn.preprocessing.MaxAbsScaler().fit_transform(データ)
'''
{[データを|]|[最大値]_int_で}正規化[する|を行いたい]
'''

sklearn.preprocessing.MinMaxScaler().fit_transform(データ)
'''
{[データを|]|[[最大値]_int_と[最小値]_int_|最大最小]で}正規化[する|を行いたい]
{[データを|]|[最大[最小値]_int_|最大最小]で}[標準化|スケール変換]する
'''

sklearn.preprocessing.MinMaxScaler(feature_range=(0, 1)).fit_transform(データ)
'''
{[データを|]|[[最大値]_int_と[最小値]_int_|最大最小]で}[正規化する|揃える]
'''

np.log([データ列]_ndarray_)
'''
データ列[の偏り|]を対数変換する
'''

np.sqrt([データ列]_ndarray_)
'''
データ列[の偏り|]を平方根変換する
'''

sklearn.preprocessing.Normalizer(norm="l1").fit_transform([データ列]_ndarray_)
'''
{[データを|]|L1ノルムで}正則化[する|を行いたい]
'''

sklearn.preprocessing.Normalizer(norm="l2").fit_transform([データ列]_ndarray_)
'''
{[データを|]|L2ノルムで}正規化[する|を行いたい]
[データ列]_ndarray_のノルムを[揃える|そろえたい]
'''

sklearn.preprocessing.Binarizer(threshold=閾値).fit_transform([データ列]_ndarray_)
'''
{[[データ列]_ndarray_を|]|[閾値|指定した値]で}[二値化|バイナリ化]する
'''

sklearn.preprocessing.LabelEncoder().fit_transform([データ列]_ndarray_)
'''
[カテゴリ|非数値]データ[列|]を[数値|連番]化する
[カテゴリ|非数値]データ[列|]を連番に変換する
'''

sklearn.preprocessing.OneHotEncoder(sparse=False).fit_transform([データ列]_ndarray_)
'''
[カテゴリ|非数値]データ[列|]を[ワン・ホット|]ベクトル化する
'''
import pandas as pd
import numpy as np
import scipy


# 統計量
_list_ = [1, 2, 3]
[配列]_ndarray_ = np.array([1, 2, 3])
[カラム名]_ColumnName_ = 'A'
_列名2_ = 'B'
[データフレーム]_DataFrame_ = pd.DataFrame(data={[カラム名]_ColumnName_: _list_})
_データ列_ = pd.Series([配列]_ndarray_)

__データフレームまたは列名__ = [データフレーム]_DataFrame_
__リストまたは配列__ = [1, 2, 3]
__配列または列名__ = [配列]_ndarray_
'''
@poly(__データフレームまたは列名__;[データフレーム]_DataFrame_;[カラム名]_ColumnName_ [データフレーム]_DataFrame_[[カラム名]_ColumnName_])
@poly(__リストまたは配列__;_list_;[配列]_ndarray_)
@poly(__配列または列名__;_list_;[配列]_ndarray_;[カラム名]_ColumnName_ [データフレーム]_DataFrame_[[カラム名]_ColumnName_])
'''

_上限値_ = 100
_下限値_ = 0

_何の_ = None

_何の_
'''
@alt(要約統計量|記述統計量|[基本|]統計量|代表値)
@alt(基本統計量=[統計量|記述統計量|[平均|標準偏差|四分位点]など])
@alt(まとめて|一度に|[全部|全て])

要約統計量[|]
基本統計量[|を[|まとめて]見たい]
'''

__データフレームまたは列名__.describe()
'''
__データフレームまたは列名__の要約統計量[|]
__データフレームまたは列名__の基本統計量[|を[|まとめて]知りたい]
'''

[データフレーム]_DataFrame_[[[カラム名]_ColumnName_, _列名2_]].describe()
'''
[カラム名]_ColumnName_と_列名2_の要約統計量[|]
[カラム名]_ColumnName_と_列名2_の基本統計量[|を[|まとめて]知りたい]
'''

pd.Series(__リストまたは配列__).describe()
'''
__リストまたは配列__の要約統計量[|]
__リストまたは配列__の基本統計量[|を[|まとめて]知りたい]
'''

# 平均

__データフレームまたは列名__.mean()
'''
@alt(平均値|平均)

__データフレームまたは列名__の平均値[が求めたい|]
'''


scipy.stats.gmean(__配列または列名__)
'''
__配列または列名__の[幾何平均|相乗平均][|]
'''

scipy.stats.hmean(__配列または列名__)
'''
__配列または列名__の調和平均[|]
'''

## https://docs.scipy.org/doc/scipy/reference/stats.html#

scipy.stats.tmean(__配列または列名__, limits=(_下限値_, _上限値_), inclusive=(True, True))
'''
@alt(外れ値を除いた|[上限|下限|範囲]指定をした)
外れ値を除いた__配列または列名__の算術平均[|]
__配列または列名__のトリム平均値[|]
'''

# 分位数

__データフレームまたは列名__.median()
'''
@alt(中央値|メディアン|[第二四分位数|50パーセンタイル])

__データフレームまたは列名__の中央値[|が知りたい]
'''

__データフレームまたは列名__.quantile(0.25)
'''
@alt(第一四分位数|25パーセンタイル|上位25[％|パーセント])

__データフレームまたは列名__の第一四分位数[|が知りたい]
'''

__データフレームまたは列名__.quantile(0.75)
'''
@alt(第三四分位数|75パーセンタイル|下位25[％|パーセント])

__Y__の第三四分位数[|が知りたい]
'''

_パーセント_ = 50

__データフレームまたは列名__.quantile(_パーセント_/100)
'''
__データフレームまたは列名__の[パーセンタイル|分位数][|が知りたい]
'''

__データフレームまたは列名__.mode()
'''
@alt(最頻値|モード)

__データフレームまたは列名__の最頻値[|が知りたい]
__データフレームまたは列名__において、どの値が[最も多い|頻出]か知りたい
'''

__データフレームまたは列名__.std()
'''
__データフレームまたは列名__の標準偏差[|が知りたい]
__データフレームまたは列名__の不偏標準偏差[|]
'''

__データフレームまたは列名__.std(ddof=0)
'''
__データフレームまたは列名__の母標準偏差[|]
'''

__データフレームまたは列名__.std(ddof=1)
'''
__データフレームまたは列名__の標本標準偏差[|]
'''

__データフレームまたは列名__.var()
'''
__データフレームまたは列名__の分散[|が知りたい]
__データフレームまたは列名__[が|は]どの程度、分散しているか[|知りたい]
'''

__データフレームまたは列名__.var(ddof=0)
'''
__データフレームまたは列名__の標本分散[|が知りたい]
'''

__データフレームまたは列名__.var(ddof=1)
'''
__データフレームまたは列名__の不偏分散[|が知りたい]
'''

__データフレームまたは列名__.kurt()
'''
__データフレームまたは列名__の[歪度|Kurtosis|歪み][|が知りたい]
__データフレームまたは列名__[が|は]{正規分布から|どの程度、}歪んでいるか知りたい
'''

__データフレームまたは列名__.skew()
'''
__データフレームまたは列名__の[尖度|Skewness|尖り][|が知りたい]
__データフレームまたは列名__[が|は]{正規分布から|どの程度、}尖っているか知りたい
'''

# 標準偏差

scipy.stats.moment(__配列または列名__, moment=n)
'''
__配列または列名__のn次モーメント[|]
'''

scipy.stats.zscore(__配列または列名__)
'''
__配列または列名__を標準化する
'''

50 + 10 * scipy.stats.zscore(__配列または列名__)
'''
__配列または列名__の偏差値を求める
'''

scipy.stats.sem(__配列または列名__)
'''
__配列または列名__の[|平均の]標準誤差[|]
'''

scipy.stats.tvar(__配列または列名__, limits=(_下限値_, _上限値_), inclusive=(True, True))
'''
外れ値を[除いた|無視して]__配列または列名__の分散[|]
__配列または列名__のトリム分散[|]
'''

scipy.stats.kurtosis(__配列または列名__, bias=False)
'''
__配列または列名__の[尖度|Kurtosis|尖り][|]
'''

scipy.stats.kurtosis(__配列または列名__, fisher=True, bias=False)
'''
__配列または列名__のフィシャー流の尖度[|]
'''

scipy.stats.skew(__配列または列名__, bias=False)
'''
__配列または列名__の[歪度|Skewness|歪み][|]
'''

scipy.stats.shapiro(__配列または列名__)
'''
[__配列または列名__が|]正規分布かどうか仮説検定する
[シャピロ・ウィルク|SW]検定[を行いたい|]
'''

scipy.stats.kstest(__配列または列名__, 'norm')
'''
__配列または列名__が正規分布かどうか仮説検定する
[コルモゴロフ・スミルノフ|KS]検定[を行いたい|]
'''
# _str_

import keyword
import re
import string
'''
@alt(先頭|最初|左[側|端])
@alt(末尾|最後|後ろ|右[側|端])
@alt(左側|左)
@alt(右側|右)
@alt(小文字|英小文字)
@alt(大文字|英大文字)
'''

_str_ = 'ABC'
_文字_ = 'A'
_list_ = ['A', 'B', 'C']
n = 1


__文字コード__ = ord('A')
__セパレータ__ = ";"
__文字列または文字__ = 'A'
__文字列または書式__ = 'A'
_list_ = []

'''
@poly(__文字コード__;_int_;文字コード)
@poly(__セパレータ__;_str_;_文字_;空白 " ";カンマ ",";改行 "\n";タブ "\t")
@poly(__文字列または文字__;_str_;_文字_;空白 " ";カンマ ",";改行 "\n";タブ "\t")
@poly(__文字列または書式__;_str_;[書式|テンプレート] 書式文字列)
@poly([リスト|タプル]_list_;_list_;_tuple_)
@poly(__文字種__;大文字 upper;小文字 lower;数字 digit;アルファベット alpha;英数字 alnum;空白 space;アスキー文字 ascii)
'''

""
'''
@alt(が使用する||)
空文字[|列]が使用する
'''

"\n"
'''
改行[|文字]が使用する
'''

"\t"
'''
タブ[|文字]が使用する
'''

" "
'''
[空白|スペース][|文字]が使用する
'''

list(string.ascii_letters)
'''
@alt(全文字集合|全ての文字セット)
@alt(アルファベット|英[文|]字)

アルファベットの全文字集合
アルファベットを[全て|]列挙する
'''

list(string.ascii_letters+string.digits)
'''
[英数字の全文字集合|全ての英数字集合]
英数字を[全て|]列挙する
'''

list(string.ascii_lowercase)
'''
小文字の全文字集合
小文字を[全て|]列挙する
'''

list(string.ascii_uppercase)
'''
大文字の全文字集合
大文字を[全て|]列挙する
'''

list(string.digits)
'''
数字の全文字集合
数字を[全て|]列挙する
'''

list(string.hexdigits)
'''
[十六|１６]進数字の全文字集合
[十六|１６]進数字を[全て|]列挙する
'''

list(string.octdigits)
'''
[８|八]進数字の全文字集合
[８|八]進数字を[全て|]列挙する
'''

list(string.punctuation)
'''
@alt(句読点|句点)

句読点の全文字集合
句読点文字を[全て|]列挙する
'''

list(string.printable)
'''
@alt(印字可能な文字|印字できる文字|印字)

印字可能な全文字集合
印字可能な文字を[全て|]列挙する
'''

list(string.whitespace)
'''
空白の全文字集合
空白文字を[全て|]列挙する
'''

for c in string.ascii_lowercase:
    print(c)
'''
{全ての小文字を|順番に}処理する
'''

for c in string.ascii_uppercase + string.digits:
    print(c)
'''
{全ての英数字を|順番に}処理する
'''


chr(__文字コード__)
'''
@alt(文字コード|ユニコード)
__文字コード__[から|を]文字[へ|に]変換する
__文字コード__に[相当|対応]する文字[|が知りたい]
'''

ord(_文字_)
'''
@alt(ユニコード=[文字コード|ユニコード|[ASCII|アスキー]コード])

_文字_をユニコードに変換する
_文字_のユニコード[|が知りたい]
'''

ord(_str_[n])
'''
_str_のn番目をユニコードに変換する
'''

[ord(ch) for ch in _str_]
'''
_str_をユニコード[のリスト|列]に変換する
'''

_str_.upper()
'''
_str_を[全て|]大文字に変換する
[_str_中の|]小文字を大文字に変換する
'''

_str_.lower()
'''
_str_を小文字に[全て|]変換する
[_str_中の|]大文字を小文字に変換する
'''

_str_.casefold()
'''
@alt(ケース|大文字小文字)

_str_のケースを[変換する|整えたい]
_str_を[全て|]小文字に変換する
_str_を[積極的に|特殊文字も含め]小文字に変換する
'''

list(_str_)
'''
_str_を[文字|文字の]リストに変換する
_str_中の文字を列挙する
'''

_str_.split()
'''
@alt(区切りたい|分割する)

{_str_を|空白で}[区切りたい|字句解析する]
'''

list(map(int, _str_.split(__セパレータ__)))
'''
@alt(整数リスト|整数のリスト|[|整]数列)

{_str_を|__セパレータ__で}区切って、整数リストに変換する
'''

_str_.splitlines()
'''
{_str_を|改行で}[分割し|区切り]、_str_リストに変換する
{_str_を|改行で}区切りたい
'''

_str_.rsplit()
'''
{_str_を|[末尾|最後|右]から|空白で}区切りたい
'''

# セパレータ


_str_.split(__セパレータ__)
'''
{_str_を|__セパレータ__で}区切って、列挙する
'''

_str_.rsplit(__セパレータ__)
'''
{_str_を|[末尾|最後|右]から|__セパレータ__で}区切って、列挙する
'''

_str_.partition()
'''
@alt(二分する|[二|]分割する|二つに分けたい)

{_str_を|空白で}二分する
'''

_str_.partition(__セパレータ__)
'''
{_str_を|[|最初の]__セパレータ__で}二分する
'''

_str_.rpartition(__セパレータ__)
'''
{_str_を|最後の__セパレータ__で}二分する
'''

_str_.partition(__セパレータ__)[0]
'''
@alt(とき|時|場合)
@alt(二分し|二つに区切って)
@alt(分けた|分割した)

{_str_を|[|最初の]__セパレータ__で}二分して、[前半|前の方]を得る
'''

_str_.partition(__セパレータ__)[-1]
'''
{_str_を|[|最初の]__セパレータ__で}二分して、[残り|後半|後ろの方]を得る
'''

_str_.rpartition(__セパレータ__)[0]
'''
{_str_を|最後の__セパレータ__で}二分して、[前半|最初の方]を得る
'''

_str_.rpartition(__セパレータ__)[-1]
'''
{_str_を最後の__セパレータ__で}二分して、[残り|後半|後ろの方]を得る
{_str_を最後の__セパレータ__で}分けたときの[後半の|残りの]_str_[|を得る|を取り出す]
'''

__文字列または文字__ = 'A'
置換後の文字列 = 'a'

_str_.replace(__文字列または文字__, 置換後の文字列)
'''
@alt(置き替えたい|置換する)

_str_を置き替えたい
[_str_中の|]__文字列または文字__を置き替えたい
[_str_中の|]__文字列または文字__を[新しい|別の]_str_[に|へ]置き替えたい
[_str_中の|]文字を[新しい|別の]文字[に|へ]置き替えたい
'''


_str_.replace(__文字列または文字__, 置換後の文字列, n)
'''
{_str_を|n回だけ}置き替えたい
{_str_を|回数制限して}置き替えたい
{[_str_中の|]文字を|n回だけ}置き替えたい
'''

_str_.expandtabs(tabsize=n)
'''
_str_中のタブ[文字|]を[|n個の]空白に[置き替えたい|する]
'''

_str_.strip()
'''
@alt(不要な=[|不要な|余分な])

_str_[|の両端]から不要な[空白|空白や改行]を除きたい
_str_をトリムする
'''

_str_.lstrip()
'''
_str_の先頭から不要な[空白|空白やタブ]を除きたい
_str_を左トリムする
'''

_str_.rstrip()
'''
_str_の末尾から不要な[空白|改行]を除きたい
_str_を右トリムする
'''

# 文字/__文字列または文字__

__文字列または文字__ = 'A'

_str_.replace(__文字列または文字__, '')
'''
@alt(除きたい|取り[除|の]きたい|除去する|消する)

_str_から__文字列または文字__を[全て|]除きたい
'''

_str_.strip(__文字列または文字__)
'''
_str_の両端から__文字列または文字__を除きたい
'''

_str_.lstrip(__文字列または文字__)
'''
_str_の先頭から__文字列または文字__を除きたい
'''

_str_.rstrip(__文字列または文字__)
'''
_str_の末尾から__文字列または文字__を除きたい
'''

_str_.zfill(width=40)
'''
@alt(ゼロ埋めする|パディングする)

_str_をゼロ埋めする
'''

str(n).zfill(width=40)
'''
[整数|数値]をゼロ埋めした_str_に変換する
'''

_str_.center(width=40)
'''
_str_を[センタリング|中央寄せ][に|]する
'''

_str_.ljust(width=40)
'''
_str_を左寄せ[に|]する
'''

_str_.rjust(width=40)
'''
_str_を右寄せ[に|]する
'''

_str_.capitalize()
'''
_str_をキャピタライズする
_str_の先頭だけ大文字化する
'''

_str_.swapcase()
'''
[_str_の|]大文字と小文字を[交換する|逆にする|入れ替えたい]
_str_のケースを[入れ替えたい|交換する|逆にする]
'''

# 包含

_文字列またはリスト_ = 'AB'

_str_ in _文字列またはリスト_
'''
_str_[が|は]_文字列またはリスト_に含まれるかどうか
_str_が_文字列またはリスト_のいずれかどうか
'''

_str_ not in _文字列またはリスト_
'''
_str_が_文字列またはリスト_に含まれないかどうか
_str_が_文字列またはリスト_のいずれでもないかどうか
'''

_文字_ in _文字列またはリスト_
'''
文字が_文字列またはリスト_に含まれるかどうか
'''

_文字_ not in _文字列またはリスト_
'''
文字が_文字列またはリスト_に含まれないかどうか
'''

_str_.find(__文字列または文字__)
'''
{_str_[中|]から|__文字列または文字__[の位置|]を}探する
{_str_の先頭から|__文字列または文字__[の位置|]を}探する
'''


_str_.find(__文字列または文字__, 開始位置) != -1
'''
{_str_の[開始|指定した]位置[以降に|より後に|先に]|__文字列または文字__が}含まれるかどうか
'''

_str_.find(__文字列または文字__, 開始位置) == -1
'''
{_str_の[開始|指定した]位置[以降に|より後に|から先に]|__文字列または文字__が}含まれないかどうか
'''

_str_.find(__文字列または文字__, 0, 終了位置) != -1
'''

{_str_の[終了|指定した]位置[より前に|以前に]|__文字列または文字__が}含まれるかどうか
'''

_str_.find(__文字列または文字__, 0, 終了位置) == -1
'''
{_str_の[終了|指定した]位置[より前に|以前に]|__文字列または文字__が}含まれないかどうか
'''


_str_.find(__文字列または文字__, 開始位置, 終了位置) != -1
'''
{_str_の指定した[範囲|区間][位置の間]に|__文字列または文字__が}含まれるかどうか
'''

_str_.find(__文字列または文字__, 開始位置, 終了位置) == -1
'''
_str_の開始位置番目と終了位置番目の間に__文字列または文字__が含まれないかどうか
{_str_の開始位置[|番目]からと終了位置[|番目]までの[間|範囲]に|__文字列または文字__が}含まれないかどうか
'''

_str_.find(__文字列または文字__, 開始位置)  # 見つからない場合は-1
'''
_str_の後半から__文字列または文字__[の位置|]を探する
開始位置を指定して__文字列または文字__[の位置|]を探する
'''

_str_.find(__文字列または文字__, 0, 終了位置)  # 見つからない場合は-1
'''
_str_の前半から__文字列または文字__[の位置|]を探する
終了位置[を指定して|まで]__文字列または文字__[の位置|]を探する
'''

_str_.find(__文字列または文字__, 開始位置, 終了位置)  # 見つからない場合は-1
'''
{__文字列または文字__を|範囲を指定して}探する
{_str_の開始位置から終了位置まで|__文字列または文字__を}探する
'''

_str_.rfind(__文字列または文字__)  # 見つからない場合は-1
'''
{_str_の末尾から|__文字列または文字__を}探する
'''

_str_.find(__文字列または文字__, 開始位置, 終了位置)  # 見つからない場合は-1
'''
{__文字列または文字__を|範囲を指定して|後方から}探する
{_str_の末尾から|範囲を指定して__文字列または文字__を}探する
'''

_list_ = ['A', 'B', 'C']

''.join(map(str, _list_))
'''
@alt(連結する|結合する|つなげる|一つ[|の文字列][に|化]する)

{[リスト]_list_を|文字列として}連結する
'''


__文字列または文字__.join(map(str, _list_))
'''
{[リスト]_list_を|__文字列または文字__[を挟んで|を使って]|文字列として}連結する
'''

_str_.count(__文字列または文字__)
'''
@alt(カウントする|数えたい)
@alt(出現数=出現[|回数]|登場[|回数])

_str_中の__文字列または文字__の出現数[が知りたい|]
_str_中の__文字列または文字__をカウントする
_str_中に__文字列または文字__がいくつか含まれるか[調べたい|カウントする]
'''

_str_.count(__文字列または文字__, 開始位置, 終了位置)
'''
@alt(までの範囲|の[範囲|間])

[_str_中の|]__文字列または文字__の出現数を範囲を指定してカウントする
開始位置から終了位置までに__文字列または文字__がいくつか含まれるか調べる
'''

_str_.startswith(__文字列または文字__)
'''
@alt(接頭辞|先頭|プレフィックス|左[側|端])
@alt(始まる|開始する)

{_str_が|__文字列または文字__で}始まるかどうか
_str_の接頭辞[が|は]__文字列または文字__かどうか
'''

_str_.startswith(__文字列または文字__, 開始位置)
'''
{_str_の開始位置以降が|__文字列または文字__で}始まるかどうか
'''

_str_.endswith(__文字列または文字__)
'''
@alt(接尾辞|末尾|サフィックス|右[側|端])
@alt(終わる|終了する)

{_str_が|__文字列または文字__で}終わるかどうか
_str_の接尾辞[が|は]__文字列または文字__かどうか
'''

_str_.removeprefix(__文字列または文字__)
'''
@alt(安全に|エラーなく)
{[|安全に]|_str_の接頭辞から|__文字列または文字__を}除きたい
_str_から接尾辞を除きたい
'''

_str_.removesuffix(__文字列または文字__)
'''
{[|安全に]|_str_の接尾辞から|__文字列または文字__を}除きたい
_str_から接尾辞を取り除[く|いた_str_]
'''

_ファイル名_ = 'file.txt'  # ファイル name
__ファイル拡張子__ = '.csv'

_ファイル名_.startswith(__ファイル拡張子__)
'''
{_ファイル名_が|__ファイル拡張子__[ファイル|]}かどうか
'''

_str_.isupper()
'''
_str_が[全て|]大文字かどうか
'''

_str_.islower()
'''
_str_が[全て|]小文字かどうか
'''

_str_.isdigit()
'''
_str_が[全て|]数字かどうか
'''

_str_.isalpha()
'''
_str_が[全て|]アルファベットかどうか
'''

_str_.isalnum()
'''
_str_が[全て|]英数字かどうか
'''

_str_.isascii()
'''
@alt(アスキー文字|ASCII文字)

_str_が[全て|]アスキー文字かどうか
'''

_str_.isspace()
'''
_str_が[全て|]空白[文字|][からなる|]かどうか
'''

_str_.isdecimal()
'''
_str_[は|が][全て|]十進数字かどうか
'''

_str_.isnumeric()
'''
_str_[は|が][全て|]数値かどうか
'''

any(c.is__文字種__() for c in _str_)
'''
{_str_中に|[ひとつでも|]__文字種__が}含まれるかどうか
'''

any(not c.is__文字種__() for c in _str_)
'''
{_str_中に|[ひとつも|]__文字種__が}含まれない[かどうか|ことを確認する]
{_str_中に|[ひとつでも|]非__文字種__が}含まれるかどうか
'''

_str_.isidentifier()
'''
_str_[は|が][全て|][識別子|変数名]かどうか
'''

keyword.iskeyword(_str_)
'''
_str_[は|が][Pythonの|]キーワードかどうか
'''

_str_.isprintable()
'''
_str_[は|が][全て|]印字できるかどうか
'''

_str_.istitle()
'''
_str_[は|が]タイトルケースかどうか
'''

_str_.encode(encoding='utf-8', errors='strict')
'''
{_str_を|[UTF8で|]}バイト列に変換する
'''

_str_.encode(encoding='sjis', errors='ignore')
'''
{_str_を|SJISで}バイト列に変換する
'''

_str_.encode(encoding='unicode_escape')
'''
{_str_を|[ユニコードエスケープ|アスキー文字[だけ|のみ]で]}バイト列に変換する
'''

encoding = "utf-8"

_str_.encode(encoding=encoding)
'''
{_str_を|_エンコーディング名_で}バイト列に変換する
'''

_str_.encode(errors="ignore")
'''
{エラーを無視して|_str_を}バイト列に変換する
'''

args = []
書式 = ''

_dict_ = {'A': '1'}

__文字列または書式__.format(*_list_)
'''
@alt(フォーマットする|[文字列|]整形する)
@alt(パラメータ|引数)
{__文字列または書式__を|[リスト|タプル]_list_[で|をパラメータとして]}フォーマットする
'''

__文字列または書式__.format_map(_dict_)
'''
{__文字列または書式__を|_dict_[で|をパラメータにして]}フォーマットする
'''

len(_str_)
'''
文字列長[|が知りたい]
_str_の[長さ|文字数|大きさ][|が知りたい]
'''

_str_[0]
'''
_str_の[先頭|最初][|の文字][|が知りたい]
'''

_str_[-1]
'''
_str_の[末尾|最後][|の文字][|が知りたい]
'''

_str_[n]
'''
_str_のn番目[|の文字][|が知りたい]
'''

_str_ == _str_
'''
_str_と_str_[は|が][同じ|等しい]かどうか
'''

_str_ != _str_
'''
_str_と_str_[は|が][等しく|同じで]ないかどうか
'''

_str_ < _str_
'''
{_str_と_str_を|辞書順で}比較する
{_str_[が|は]_str_より|辞書順で}[前|小さい]かどうか
'''

_str_ > _str_
'''
{_str_[が|は]_str_より|辞書順で}[後ろ|大きい]かどうか
'''

_str_.casefold() == _str_.casefold()
'''
@alt(ケースを無視して|大文字小文字を無視して)
{_str_と_str_[が|は]|ケースを無視して}[同じ|等しい]かどうか
'''

_str_.casefold() < _str_.casefold()
'''
_str_と_str_をケースを無視して比較する
'''

# Tips
('ァ' <= _文字_ <= 'ン')
'''
@alt(片仮名|カタカナ)
@alt(平仮名|ひらがな)
文字[が|は]片仮名かどうか
'''

('ぁ' <= _文字_ <= 'ん')
'''
_文字_[が|は]平仮名かどうか
'''

('\u4E00' <= _文字_ <= '\u9FD0')
'''
_文字_[が|は]漢字かどうか
'''

re.search('[\u4E00-\u9FD0]', _str_)
'''
{_str_中に|漢字が}[含まれる|使われている]かどうか
'''

re.search('[あ-んア-ン\u4E00-\u9FD0]', _str_)
'''
{_str_[中|]に|日本語が}[含まれる|使われている]かどうか
'''

''.join([chr(ord(ch) - 96) if ('ァ' <= ch <= 'ン') else ch for ch in _str_])
'''
[_str_[中|]の|]片仮名を平仮名に変換する
'''

''.join([chr(ord(ch) + 96) if ('ぁ' <= ch <= 'ん') else ch for ch in _str_])
'''
[_str_[中|]の|]平仮名を片仮名に変換する
'''

_str_.translate(str.maketrans('０１２３４５６７８９', '0123456789'))
'''
[_str_[中|]の|]全角数字を半角[数字|]に変換する
'''
import os
import sys

__オブジェクト__ = 1.0
'''
@poly(__オブジェクト__;オブジェクト;[結果]_str_)
'''
n = 1

sys.byteorder
'''
@alt(プラットホーム|環境|[実行|動作]環境|OS)
@alt(ランタイム|実行環境|インタプリタ)
@alt(が知りたい|を[調べたい|確認する|確めたい]|)
@alt(バイトオーダ|エンディアン)

[|プラットホームの]バイトオーダが知りたい
'''

sys.getdefaultencoding()
'''
[|デフォルトの|プラットホームの]エンコーディングが知りたい
'''

sys.getrefcount(__オブジェクト__)
'''
@alt(ガベージコレクション|ゴミ集め|GC)
[__オブジェクト__の|ガベージコレクションの]参照カウントが知りたい
'''

sys.getsizeof(__オブジェクト__)
'''
@alt(バイトサイズ|メモリ[使用|消費]量)

__オブジェクト__のバイトサイズが知りたい
'''

sys.getrecursionlimit()
'''
@alt(最大の再帰数|スタックの最大[長|の深さ])

[現在の|ランタイムの|]再帰の[最大回数|上限]が知りたい
{何回[まで|、]|再帰が}できるか[を|、][|知りたい]
'''

sys.setrecursionlimit(1000000)
'''
再帰エラーを[未然に|]防ぎたい
再帰の[上限|最大回数]を[上げたい|増やする]
'''

文字列 = 'A'

sys.intern(文字列)
'''
文字列を[隔離する|インターンする]
'''

sys.maxsize
'''
[プラットフォームの|][符号付き|]整数の[最大値]_int_が知りたい
'''

sys.maxunicode
'''
@alt(コードポイント|文字コード)

[プラットフォームの|]コードポイントの[最大値]_int_が知りたい
'''

sys.platform
'''
@alt(の名前|名)

プラットホームの名前が知りたい
'''

__X__ = 'darwin'
'''
@X('darwin';'linux';'win32')
@Y([MacOS|マック];[Linux|リナックス];[Windows|ウィンドウズ])
'''

sys.platform.startswith(__X__)
'''
プラットホーム[が|は]__Y__かどうか
'''

sys.argv
'''
@alt(コマンド引数|コマンドライン)

コマンド引数[|を列挙する]
コマンド引数のリスト
'''

sys.argv[0]
'''
@alt(スクリプト名|[スクリプト|プログラム]ファイル名|プログラム名)

スクリプトの名前が知りたい
[プログラム|スクリプト]のファイルの名前が知りたい
'''

sys.argv[1]
'''
[最初の|第一]コマンド引数が知りたい
コマンドの第一引数[]
第一引数[で指定された|の]ファイルの名前
'''

sys.argv[1:]
'''
コマンド引数の一覧[|]
コマンド引数を[列挙する|一覧として得る]
'''

if len(sys.argv) > 1:
    print(sys.argv[1])  # 具体的な処理にする
'''
もしコマンド引数が[与えられた|指定された]なら、処理する
'''


for file in sys.argv[1:]:
    print(file)  # 具体的な処理にする
'''
コマンド引数で[与えられた|指定された]ファイル[名|]を一つずつ処理する
'''

sys.flags
'''
コマンド[ライン|]フラグの状態が知りたい
'''

sys.path
'''
モジュールを検索するパス[|を列挙する]
Pythonパス[の一覧]が知りたい
'''

ディレクトリ名 = '.'

sys.path.append(ディレクトリ名)
'''
{モジュール[を検索する|の検索]パスに|ディレクトリを}追加する
{Pythonパスに|ディレクトリを}追加する
'''

sys.path.append(os.path.join(os.path.dirname(__file__), ディレクトリ名))
'''
{スクリプトのサブディレクトリを|Pythonパスに}加えたい
'''

sys.modules
'''
[|既に]ロードされたモジュール[の一覧が知りたい|を列挙する]
モジュールを列挙する
'''

sys.modules[__name__]
'''
現在のモジュール[|]
{自分自身を|モジュールとして}[|]
'''

etype, evalue, traceback = sys.exc_info()
'''
[現在|][処理|実行]中の[例外|エラー]情報が知りたい
[例外|エラー]の[種類|メッセージ|トレースバック][|を|]
'''

sys.executable
'''
[Python|]インタプリタの実行ファイルの絶対パスが知りたい
'''

sys.stdin
'''
標準入力
標準入力[を使用する|]
'''

file = sys.__X__
'''
@X(stdout;stderr;open('file.txt', 'w'))
@Y(標準出力;標準エラー;ファイル)

ただし、出力先を__Y__に設定する
ただし、__Y__に出力する
ただし、__Y__を使用する
ただし、__Y__を出力[|先]にする
'''

sys.stdout
'''
標準出力
標準出力[を使用する|]
'''

sys.stderr
'''
標準エラー
標準エラー[を使用する|]
エラーを出力する
'''

sys.stdin.read(1)
'''
@alt(読む|読み込む)
{標準入力から|1文字[だけ|分|]}読む
'''

sys.stdin.readline()
'''
{標準入力から|1行[だけ|分|]}読む
'''

sys.stdin.readline().rstrip()
'''
{標準入力から|1行[だけ|分|]|改行[なし[で|に]|を[取り|]除いて]}読む
{標準入力から|1行[だけ|分|]}読み込んで、改行を取り除く
'''

sys.stdout.flush()
'''
@alt(フラッシュする|強制表示する|即時表示する)
標準出力[のバッファ|]をフラッシュする
'''

sys.stdout.isatty()
'''
[実行時の|]標準出力[の出力先|先|]がターミナルかどうか
標準出力がターミナル出力かどうか
'''

not sys.stdout.isatty()
'''
[実行時に|]標準出力がパイプかどうか
'''

os.isatty(sys.stdin.fileno())
'''
[実行時の|]標準入力[の入力元|のソース]がターミナルかどうか
'''

# sys.path.insert(1, os.path.dirname(os.path.realpath(__file__)))
# sys.path.insert(0, '..')
# sys.path.insert(0, os.path.abspath('/my/source/lives/here'))
# os.path.dirname(sys.modules['__main__'].__file__)
# sys.path.append(os.path.join(os.environ['SPARK_HOME'], 'bin'))
# os.path.realpath(os.path.dirname(sys.argv[0]))
# sys.stdout.isatty()
# os.path.dirname(sys.executable)
# getattr(sys.modules[__name__], 'A')
# os.isatty(sys.stdin.fileno())
# sys.stdout = sys.stdout.detach()
# caller = sys._getframe(1)
# calling_frame = sys._getframe().f_back
# current_frame = sys._getframe(0)
# cur_version = sys.version_info
# f = sys.exc_info()[2].tb_frame
# sys.stdin.fileno()
# inspect.getmembers()
# func_name = sys._getframe().f_code.co_name
# if not sys.stdin.isatty():
# sys._getframe().f_code.co_name

if sys.version_info >= (3, 4):
    print(sys.version_info)
'''
Pythonのバージョン[を確認する|]
'''


sys.exit()
'''
@alt(終了する|停止する|止めたい|終えたい)
@alt(プログラムの実行|プログラム|実行)

プログラムの実行を[強制的に|ここで|即座に]終了する
'''

sys.exit(0)
'''
プログラムの実行を[正しく|正常[に|]|適切に]終了する
'''

sys.exit(1)
'''
プログラムの実行を[異常|エラーとして]終了する
'''
import matplotlib
import matplotlib.pyplot as plt
'''
@poly(__色名__;青 "blue";緑 "green";赤 "red";シアン "cyan";マゼンタ "magenta";黄 "yellow";黒 "black";白 "white")
'''

__色名__ = 'r'

color = __色名__
'''
ただし、__色名__[色|]を使う
'''

plt.barh([データ列]_DataFrame_[_ColumnName_]], [データ列]_DataFrame_[_ColumnName_]], color=__色名__)
'''
横棒グラフの色を__色名__にする
__色名__色の横棒グラフを描画する
{横棒グラフを|__色名__色で_}描画する
'''
[整数]_int_ = 1
変数 = x

変数 += _int_
'''
@alt(変数|変数の値)

変数を[|_int_だけ][増加させたい|大きくする|増やする]
'''

変数 -= _int_
'''
変数を[|_int_だけ][減少させたい|小さくする|減らする]
'''

変数 *= _int_
'''
変数を_int_倍にする
'''

変数 **= _int_
'''
変数を[_int_|累]乗に増やする
'''

変数 /= _int_
'''
変数を_int_分の１にする
'''

変数 /= 2
'''
変数を半分にする
'''

変数 //= _int_
'''
{変数を|切り捨てながら}_int_分の[一|1]にする
変数を_int_分の[一|1]にする
'''

変数 //= 2
'''
{変数を|切り捨てながら}半分にする
変数を半分にする
'''

変数 %= _int_
'''
変数を_int_で割った余りにする
'''
