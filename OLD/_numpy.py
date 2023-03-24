import numpy as np
'''
@alt(配列|行列|ベクトル)
@alt(作りたい=[作りたい|作成したい|初期化したい])
@alt(求める=[求める|[計算|算出]したい|[得る|調べる]])

@alt(要素ごと|各要素)

ベクトル[の|][演算|計算]を[したい|行う]
行列[の|][演算|計算]を[したい|行う]
numpyを[使う|入れる|インポートしたい]
'''

_配列_ = np.array([1, 2, 3, 4])
_行列_ = np.array([[1, 2], [3, 4]])
_配列_ = __イテラブル__
_リスト_ = [1, 2]
n = 3

要素数 = 3
行数 = 2
列数 = 2
初期値 = 0
行番号 = 0
列番号 = 0

N = 10
開始値 = 0
終了値 = 10
等差 = 2

__行列__ = _配列_
'''
@poly(__行列__;_配列_;_行列_)
'''

__D型__ = np.int

dtype = __D型__
'''
@poly(__D型__;整数 np.int;８ビット整数 np.int8;符号なし８ビット整数 np.uint8;３２ビット整数 np.int32;[ブール|論理値] bool;複素数 complex)

<option>データ型は__D型__
<option>[|データ型として]__D型__を使う
'''

np.array(_リスト_)
'''
_リスト_を配列に変換したい
{_リスト_から|配列を}作りたい
'''

np.array(__イテラブル__)
'''
__イテラブル__を配列に変換したい
{__イテラブル__から|配列を}作りたい
'''

np.zeros(要素数)
'''
{全要素が|0で}初期化した配列[|を作りたい]
ゼロ埋めされた配列[|を作りたい]
'''

np.zeros(要素数, dtype=__D型__)
'''
{ゼロ埋めされた|__D型__型の}配列[|を作りたい]
'''

np.zeros(行数, 列数)
'''
{全要素を|０で}初期化した行列[|を作りたい]
ゼロ埋めされた行列[|を作りたい]
'''

np.zeros(行数, 列数, dtype=__D型__)
'''
{{全要素を|０で}初期化した|__D型__型の}行列[|を作りたい]
'''

np.ones(要素数, dtype=np.int)
'''
{全要素を|1で}初期化した配列[|を作りたい]
要素が全て1の配列[|を作りたい]
'''

np.ones(行数, 列数, dtype=np.int)
'''
{全要素を|1で}初期化した行列[|を作りたい]
全要素が1の行列[|を作りたい]
'''

np.full(要素数, 初期値, dtype=np.int)
'''
{全要素を|初期値で}初期化した配列[|を作りたい]
要素が全て初期値の配列[|を作りたい]
'''

np.full((行数, 列数), 初期値, dtype=np.int)
'''
{全要素を|初期値で}初期化した行列[|を作りたい]
全要素が初期値の行列[|を作りたい]
'''

np.eye(行数, 列数)
'''
単位行列[|を作りたい]
'''

np.identity(n)
'''
[単位正方行列|正方単位行列][|を作りたい]
'''

np.empty(要素数, dtype=np.int)
'''
未初期化の配列[|を作りたい]
'''

np.empty((行数, 列数), dtype=np.int)
'''
未初期化の行列[|を作りたい]
'''

np.empty_like(_配列_)
'''
_配列_と同じ大きさの[空配列|空の配列]を作りたい
'''

np.arange(_整数_)
'''
[0から|]_整数_未満までの配列[|を作りたい]
'''

np.arange(1, _整数_+1)
'''
1から_整数_までの配列[|を作りたい]
'''

np.arange(開始値, 終了値, 等差)
'''
[連続した|連番の]配列の[自動|]作成したい
等間隔の配列[を作りたい＼]
等差数列を配列に変換したい
'''

np.linspace(最小値, 最大値, 要素数)
'''
[最大最小|範囲|区間]から配列[|を作りたい]
'''

np.random.random(N)
'''
乱数[で要素を埋めた|の]配列[|を作りたい]
'''

np.random.random((行数, 列数))
'''
乱数[の|で要素を埋めた]行列[|を作りたい]
'''

np.random.randint(開始値, 終了値, N)
'''
整数乱数[で要素を埋めた|の]配列[|を作りたい]
'''

np.random.randint(開始値, 終了値, (行数, 列数))
'''
整数乱数[で要素を埋めた|の]行列[|を作りたい]
'''


_配列_.reshape(行数, 列数)
'''
_配列_[の[次元|形状]|]を変形したい
'''

_配列_.reshape(-1, 1)
'''
_配列_を[2次元1列|縦ベクトル]に変形したい
'''

_配列_.reshape(1, -1)
'''
_配列_を[2次元1行|横ベクトル]に変形したい
'''

np.zeros_like(_配列_)
'''
@alt(ベースに=[元に|ベースに][|して])

[既存の|]_配列_をベースに全要素が0の配列[|を作りたい]
'''

np.ones_like(_配列_)
'''
[既存の|]_配列_をベースに全要素が1の配列[|を作りたい]
'''

np.full_like(_配列_, 初期値)
'''
[既存の|]_配列_をベースに全要素が初期値の配列[|を作りたい]
'''

指定の値 = 0

_配列_[:, :] = 指定の値
'''
_配列_の全要素の値を変更したい
_配列_の全要素を指定の値にしたい
'''

_配列_[行番号, 列番号]
'''
__行列__の値[|を得る]
'''

_配列_[行番号, 列番号] = 指定の値
'''
__行列__の値を変更したい
'''

_配列_[行番号]
'''
__行列__の行[|を選択したい]
'''

_配列_[:, 列番号]
'''
__行列__の列[|を選択したい]
'''

# ユニーク

np.unique(_配列_)
'''
[|_配列_の]ユニークな値を要素としたい配列[|を得る]
'''

np.unique(_配列_, return_counts=True)
'''
[|_配列_の]ユニークな要素ごとの[頻度|出現回数][|を得る]
'''


# 転置行列

[list(x) for x in list(zip(*_リスト_))]
'''
２次元リストを転置したい
２次元リストの転置行列を求めたい
'''

_配列_.T
'''
_配列_を転置したい
__行列__の転置行列を求めたい
'''

_配列_ + _配列_
'''
_配列_の和を求めたい
_配列_の要素ごとに加算したい
'''

_配列_ - _配列_
'''
_配列_の差を求めたい
'''

_配列_ * n
'''
_配列_のスカラー[倍|積]を求めたい
'''

np.multiply(_配列_, _配列_)
'''
_配列_の要素ごとの[積|アダマール積]を求めたい
'''

np.dot(_配列_, _配列_)
'''
_配列_の内積を求めたい
'''

np.matmul(_行列_, _行列_)
'''
[[_行列_と|]_行列_の|]行列積を求めたい
'''

np.linalg.inv(_行列_)
'''
[_行列_の|]逆行列を求めたい
'''

np.linalg.pinv(_行列_)
'''
[_行列_の|]ムーア・ペンローズの擬似逆行列を求めたい
'''


np.linalg.det(_行列_)
'''
[_行列_の|]行列式を求めたい
'''

np.linalg.eig(_配列_)
'''
FIXME
'''

# ユニバーサル関数

np.gcd(_配列_, _配列_)
'''
_配列_[間|]の要素ごとの最大公約数を求めたい
'''

np.lcm(_配列_, _配列_)
'''
_配列_[間|]の要素ごとの最小公倍数を求めたい
'''

__行列__.shape
'''
__行列__の[形状|形|シェイプ]を求めたい
'''

__行列__.dtype()
'''
__行列__の[データ型|型]を求めたい
__行列__[が|は]何のデータ型か調べる
'''

__行列__.ndim
'''
__行列__の[次元数|次元の数]を求めたい
__行列__[は|が]何次元か調べる
'''

_配列_.size
'''
_配列_の[要素数|個数]を求めたい
_配列_にはいくつ要素が[ある|含まれる|存在したい]か調べる
'''


np.concatenate([__行列__, __行列__], axis=0)
'''
{[２つの|__行列__と]__行列__を|[列方向|縦方向]に}連結したい
'''

np.concatenate([__行列__, __行列__], axis=1)
'''
{[２つの|__行列__と]__行列__を|[行方向|横方向]に}連結したい
'''

np.sum(_配列_)
'''
_配列_の[合計値|合計]を求めたい
'''

np.sum(__行列__, axis=0)
'''
__行列__の列ごとの[合計値|合計]を求めたい
'''

np.sum(__行列__, axis=1)
'''
__行列__の行ごとの[合計値|合計]を求めたい
'''

np.mean(_配列_)
'''
_配列_の[平均値|平均]を求めたい
'''

np.mean(__行列__, axis=0)
'''
__行列__の列ごとの[平均値|平均]を求めたい
'''

np.mean(__行列__, axis=1)
'''
__行列__の行ごとの[平均値|平均]を求めたい
'''

np.min(_配列_)
'''
_配列_の[最小値|最小]を求めたい
'''

np.min(__行列__, axis=0)
'''
__行列__の列ごとの[最小値|最小]を求めたい
'''

np.min(__行列__, axis=1)
'''
__行列__の行ごとの[最小値|最小]を求めたい
'''

np.max(_配列_)
'''
_配列_の[最大値|最大]を求めたい
'''

np.max(__行列__, axis=0)
'''
__行列__の列ごとの[最大値|最大]を求めたい
'''

np.max(__行列__, axis=1)
'''
__行列__の行ごとの[最大値|最大]を求めたい
'''

np.std(_配列_)
'''
_配列_の標準偏差を求めたい
'''

np.std(__行列__, axis=0)
'''
__行列__の列ごとの標準偏差を求めたい
'''

np.std(__行列__, axis=1)
'''
__行列__の行ごとの標準偏差を求めたい
'''

np.var(_配列_)
'''
_配列_の分散を求めたい
'''

np.var(__行列__, axis=0)
'''
__行列__の列ごとの分散を求めたい
'''

np.var(__行列__, axis=1)
'''
__行列__の行ごとの分散を求めたい
'''

np.cumsum(_配列_)
'''
_配列_の累積和を求めたい
'''

np.cumprod(_配列_)
'''
_配列_の累積積を求めたい
'''

np.unique(_配列_)
'''
_配列_から重複を除きたい
_配列_から重複を除いた配列を作りたい
_配列_のユニークな要素を求めたい
'''

u, counts = np.unique(_配列_, return_counts=True)
'''
_配列_のユニークな要素とその個数を求めたい
'''

u, indices = np.unique(_配列_, return_index=True)
'''
_配列_のユニークな要素とその[位置|インデックス]を求めたい
'''

_配列_.flatten()
'''
_配列_を[平坦化|フラット化|一次元化]したい
_配列_を[平坦|フラット|一次元]にしたい
'''
