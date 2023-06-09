# 整数

n = 2
_文字列_ = '1101'
_整数_ = 2
_整数2_ = 2

int(_文字列_, 10)
'''
@alt(に変換したい|[化|に]したい)
_文字列_を整数に変換したい
'''

int(_文字列_, 2)
'''
{_文字列_を|[２|二]進数として}整数に変換したい
'''

int(_文字列_, 8)
'''
{_文字列_を|[８|八]進数として}整数に変換したい
'''

int(_文字列_, 16)
'''
{_文字列_を|[１６|十六]進数として}整数に変換したい
'''

int(_文字列_, n)
'''
{_文字列_を|n進数として}整数に変換したい
'''

バイト数 = 8

int(_文字列_, 16).to_bytes(length=バイト数, byteorder='big')
'''
@alt(バイト列|バイナリ)
@alt(進数表現|進数表記)

[１６|十六]進数表現[の_文字列_|]をバイト列に変換したい
'''

int(_文字列_, 2).to_bytes(length=バイト数, byteorder='big')
'''
@alt(バイト列|バイナリ)

[２|二]進数表現[の_文字列_|]をバイト列に変換したい
'''

bin(_整数_)
'''
_整数_を[２|二]進数表現[|の文字列]に変換したい
'''

oct(_整数_)
'''
_整数_を[８|八]進数表現[|の文字列]に変換したい
'''

hex(_整数_)
'''
_整数_を[１６|十六]進数表現[|の文字列]に変換したい
'''

_整数_.bit_length()
'''
@alt(を知りたい|を調べたい|が欲しい)

_整数_のビット長[|を知りたい]
'''

(_整数_.bit_length() + 7) // 8
'''
@alt(を知りたい|を調べたい|が欲しい)

_整数_のビット長[|を知りたい]
'''

_整数_.to_bytes((_整数_.bit_length() + 7) // 8, byteorder='big')
'''
_整数_をバイト列に変換したい
'''

_整数_.to_bytes((_整数_.bit_length() + 7) // 8, byteorder='big', signed=True)
'''
{_整数_を|符号付きで}バイト列に変換したい
'''

_整数_.to_bytes(length=バイト数, byteorder='big')
'''
{_整数_を|[|符号なしで]}バイト列に変換したい
'''

_整数_.to_bytes(length=バイト数, byteorder='big', signed=True)
'''
{_整数_を|符号付きで}バイト列に変換したい
'''

_整数_ + _整数2_
'''
@alt(求めたい|計算したい)

[足し算したい|加算したい]
_整数_に_整数2_を[加えたい|加算したい]
_整数_[プラス|足す|＋]_整数2_を求めたい
[二つの|]整数の和を求めたい
'''

_整数_ - _整数2_
'''
[引き算したい|減算したい]
_整数_から_整数2_を[引きたい|減算したい]
_整数_[マイナス|引く|ー]_整数2_を求めたい
[二つの|]整数の差を求めたい
'''

_整数_ * _整数2_
'''
[掛け算したい|掛算したい|乗算したい]
_整数_に_整数2_を[かけたい|掛けたい]
_整数_[かける|掛ける|×]_整数2_を求めたい
[二つの|]整数の積を求めたい
'''

_整数_ / _整数2_
'''
[割り算|徐算|割算]したい
_整数_を_整数2_で[割りたい|わりたい]
_整数_[わる|割る|÷]_整数2_を求めたい
[二つの|]整数の商を求めたい
'''

_整数_ // _整数2_
'''
整数で[割り算|徐算|割算]したい
_整数_を_整数2_で割って[小数点以下|その結果]を切り捨てたい
_整数_を[|_整数2_で]整数除算したい
'''

_整数_ % _整数2_
'''
_整数_を_整数_で割った[余り|モジュロ|剰余|mod]を求めたい
[整数の|][割り算の余り|モジュロ]を求めたい
'''

(_整数_ + _整数2_ - 1) // _整数2_
'''
_整数_を_整数2_で割って[小数点以下|その結果]を切り上げたい
整数[除算|割り算]の切り上げを求めたい
'''


__X__ = 2
'''
@X(2;3;4;5;8;n)
@Y([二|2];[三|3];[四|4];[五|5];[八|8];n)
'''

_整数_ ** __X__
'''
整数の__Y__乗を求めたい
'''

_整数_ / __X__
'''
整数の__Y__分の[一|1]を求めたい
'''

# ビット演算

_整数_ & _整数2_
'''
@alt(整数同士の||２つの整数の|_整数_と_整数2_の)
整数同士の[論理|ビット]積を求めたい
'''

_整数_ | _整数2_
'''
整数同士の[論理|ビット]和を求めたい
'''

_整数_ ^ _整数2_
'''
整数同士の[排他的論理和|XOR]を求めたい
'''

_整数_ << n
'''
整数を[nだけ|]左シフトしたい
整数の左シフトを求めたい
'''

_整数_ >> n
'''
整数を[nだけ|]右シフトしたい
整数の右シフトを求めたい
'''

# 比較演算子

_整数_ == _整数2_
'''
@alt(かどうか|か知りたい|か[調べたい|判定したい])
@alt(整数同士が|２つの整数が|_整数_と_整数2_が)

整数同士が[等しい|同じ値]かどうか
_整数_[が|は]_整数2_と等しいかどうか
_整数_[が|は]_整数2_かどうか
'''

_整数_ > _整数2_
'''
_整数_[が|は]_整数2_より大きいかどうか
_整数_[が|は]_整数2_よりも大きいかどうか
'''

_整数_ < _整数2_
'''
_整数_[が|は]_整数2_より小さいかどうか
_整数_[が|は]_整数2_よりも小さいかどうか
'''

_整数_ >= _整数2_
'''
_整数_[が|は]_整数2_以上かどうか
'''

_整数_ <= _整数2_
'''
_整数_[が|は]_整数2_以下かどうか
'''

_整数_ < _整数2_ or _整数_ >= n3
'''
_整数_[が|は]_整数2_未満、[または|もしくは|それか]n3以上かどうか
'''

_整数_ <= _整数2_ or _整数2_ >= n3
'''
_整数_[が|は]_整数2_以下、[または|もしくは|それか]、n3以上かどうか
'''

_整数_ <= _整数2_ and _整数2_ <= n3
'''
_整数2_がn以上、かつ、n3以下かどうか
'''

_整数_ < _整数2_ and _整数2_ < n3
'''
_整数2_がnより大きく、かつ、n3[未満|より小さい]かどうか
'''

_整数_ % 2 == 0
'''
_整数_[が|は]偶数かどうか
_整数_[が|は]2で割り切れるかどうか
'''

_整数_ % 2 == 1
'''
_整数_[が|は]奇数かどうか
_整数_[が|は]2で割り切れないかどうか
'''

_整数_ % 3 == 0
'''
_整数_[が|は]3の倍数かどうか
_整数_[が|は]3で割り切れるかどうか
'''

_整数_ % 5 == 0
'''
_整数_[が|は]5の倍数かどうか
_整数_[が|は]5で割り切れるかどうか
'''

_整数_ % _整数2_ == 0
'''
_整数_[が|は]_整数2_の倍数かどうか
_整数_[が|は]_整数2_で割り切れるかどうか
'''

_整数_ % _整数2_ != 0
'''
_整数_[が|は]_整数2_の倍数でないかどうか
_整数_[が|は]_整数2_で割り切れないかどうか
'''

_整数_ > 0
'''
_整数_[が|は]正の[数|整数]かどうか
'''

_整数_ >= 0
'''
_整数_[が|は]非負数でないかどうか
'''

_整数_ < 0
'''
_整数_[が|は]負の[数|整数]かどうか
'''

-9 <= _整数_ <= 9
'''
_整数_[が|は]一桁の[数|整数]かどうか
_整数_[が|は]-9以上、9以下かどうか
'''

0 <= _整数_ <= 9
'''
_整数_[が|は]一桁の[数|整数]かどうか
'''

_整数_ in __リストまたはタプル__
'''
_整数_[が|は]__リストまたはタプル__の[どれか|いづれか|一つ[|である]]かどうか
'''

_整数_ == 1 or _整数_ == 2
'''
_整数_[が|は]1、もしくは2かどうか
'''

_整数_ == 1 or _整数_ == 2 or _整数_ == 3
'''
_整数_[が|は]1、もしくは2、もしくは3に等しいかどうか
'''

len(str(_整数_))
'''
_整数_の桁数を求めたい
整数[が|は]何桁[|になる]か知りたい
'''

sum(map(int, str(_整数_)))
'''
@alt(総和|和)

_整数_の[各|それぞれの]桁の総和[を求めたい||が欲しい]
'''
