# 設定

import operator

def predicate(a): return a > 0

__結果__=1
'''
@poly(__結果__;_結果_;_整数_;_文字列_)
@poly(__イテラブル__;_リスト_;_タプル_;_イテラブル_)
'''

##


x = 0
y = 0
z = 0

# プリント

print()
'''
@alt(プリントしたい|表示したい|出力したい)

[空行を|改行[だけ|のみ]]プリントしたい
改行したい
'''

print(__結果__)
'''
__結果__をプリントしたい
'''

print(__結果__, __結果__)
'''
２つの__結果__を[順に|]プリントしたい
'''

print(__結果__, __結果__, __結果__)
'''
[３つ|複数]の__結果__を[順に|]プリントしたい
'''

end = _文字列_
'''
option: {改行[|したい]の代わりに|_文字列_を}用いる
option: {[プリント|出力]の終端に|_文字列_を}用いる
'''

end = ''
'''
option: 改行しない[|ように設定したい]
option: 改行なし
'''

print(__結果__, end='')
'''
@alt(改行なしに|改行せず[|に]|改行しな[いで|くて])

{改行なしに|__結果__を}プリントしたい
{__結果__の出力を|改行なしに}行う
'''

print(__結果__, __結果__, end='')
'''
{改行なしに|[２つの|複数の]__結果__を}プリントしたい
'''

print(x, end='')
'''
{改行なしに|xを}プリントしたい
{xの出力を|改行なしに}行う
'''

print(x, y, end='')
'''
{改行なしに|xとyを|[|順に]}プリントしたい
'''

print(*__イテラブル__)
'''
__イテラブル__[[の要素|]を展開して|の[値|要素]のみ]プリントしたい
'''


sep = __結果__
'''
@X(','|'\t'|':'|'/'|'\n'|s)
@Y(カンマ|タブ|コロン|スラッシュ|改行|文字列)
@alt(セパレータ|区切り[|記号]|分割記号)

option: セパレータを__結果__にしたい
option: __結果__をセパレータで使いたい
'''

sep = ''
'''
option: セパレータを使わない
'''

print(x, y, sep=__結果__)
'''
{xとyを|__結果__で区切って}プリントしたい
'''

print('Hello World')
'''
[ハローワールド|こんにちは世界][と|を]プリントしたい
{試しに|何か}動か[す|してみたい]
[最初の|初めての]プログラムを書きたい
'''

__色__ = 30
'''
@poly(__色__;黒色 30;赤色 31;緑色 32;黄色 33;青色 34;[マゼンタ|紫色] 35;[シアン|水色] 36;白色 37;太[|文]字 1;[下線|アンダーライン]付き 2)
'''

print(f'\033[__色__m{x}\033[0m')
'''
{xを|__色__で}プリントしたい
'''

f'\033[__色__m{__結果__}\033[0m'
'''
[__結果__を|]__色__で[プリント|表示]できる文字列に変換したい
[__結果__を|]__色__[に|化]したい
'''

x = 0.11

__結果__ = ':.3f'
print(__結果__.format(x))
'''
@X(':.1f'|':.2f'|':.3f'|':.4f'|':.5f')
@Y('1'|'2'|'3'|'4'|'5')
[xの|]小数点以下__結果__桁まで[を|]プリントしたい
'''

__結果__.format(x)
'''
[xの|]小数点以下__結果__桁[まで|]の文字列に変換したい
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
ユーザが整数を入力したい
ユーザから入力される
'''


##

x = n
'''
変数を定義したい
'''

x, y = y, x
'''
@alt(スワップしたい|入れ替える)

変数[|の値]をスワップしたい
'''

リスト[x], リスト[y] = リスト[y], リスト[x]
'''
リストの要素をスワップしたい
'''

# 組み込み関数（計算）

abs(x)
'''
xの絶対値[|を求める]
'''

bool(x)
'''
@alt(論理値|ブール値)

xを論理値に変換したい
xが真かどうか
'''

complex(x, y)
'''
[x, yの|]複素数[|を求める]
'''

divmod(x, y)
'''
[xとyの|]商と余りを同時に求める
'''

float(x)
'''
[xを|]浮動小数点数に変換したい
'''

int(x)
'''
[xを|]整数に変換したい
'''

# 組み込み関数（文字列）

ascii(x)
'''
[xを|]印字できる文字列にしたい
[xの|]印字可能な文字列
'''

hash(x)
'''
[xの|]ハッシュ値[|を求める]
'''

max(x, y)
'''
@alt(最大値|[最も大きい値|最大の値|一番小さい値])
２[変数|数|つ]の最大値[|を求める]
'''

min(x, y)
'''
@alt(最小値|[最も小さい値|最小の値|一番小さい値])
２[変数|数|つ]の最小値[|を求める]
'''

max(x, y, z)
'''
３[変数|数|つ]の最大値[|を求める]
'''

min(x, y, z)
'''
３[変数|数|つ]の最小値[|を求める]
'''

float(x)
'''
xを[浮動小数点数型|浮動小数点数|実数]に変換したい
'''

int(x)
'''
xを整数に変換したい
'''

str(x)
'''
xを文字列に変換したい
'''

