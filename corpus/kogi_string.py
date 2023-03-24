import keyword
import re
import string

_int_ = 10
_str_ = 'A'
_list_ = ['A']

n = 0

""
'''
[空文字|空文字列]
'''

"\n"
'''
[改行文字]
'''

"\t"
'''
[タブ文字]
'''

" "
'''
[空白文字|スペース文字]
'''


len(_str_)
'''
_str_の[長さ|文字数|大きさ]
'''

_str_[0]
'''
_str_の[先頭|最初]の[文字]
'''

_str_[-1]
'''
_str_の[末尾|最後]の[文字]
'''

_str_[n]
'''
_str_のn番目の[文字]
'''

_str_ == _str_
'''
_str_と_str_[は|が]等しいかどうか
'''

_str_ != _str_
'''
_str_と_str_[は|が]等しくないかどうか
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
{_str_と_str_[が|は]|ケースを無視して}等しいかどうか
'''

_str_.casefold() < _str_.casefold()
'''
{_str_と_str_を|ケースを無視して}比較する
'''

chr(_int_)
'''
[文字コード]_int_[から|を]文字[へ|に]変換する
[文字コード]_int_から変換された文字列
'''

ord(_str_)
'''
[文字]_str_を文字コードに変換する
[文字]_str_の文字コード
'''

ord(_str_[n])
'''
_str_のn番目の文字コード
'''

[ord(ch) for ch in _str_]
'''
_str_を文字コードのリストに変換する
_str_のそれぞれの文字を文字コードに変換した[リスト]
'''

_str_.upper()
'''
_str_を大文字に変換した[文字列]
_str_中の小文字を大文字に変換した[文字列]
'''

_str_.lower()
'''
_str_を小文字に変換した[文字列]
_str_中の大文字を小文字に変換した[文字列]
'''

_str_.casefold()
'''
_str_を[積極的に|特殊文字も含め]小文字に変換する
'''

list(_str_)
'''
_str_の文字リスト
_str_を文字リストに変換する
_str_中の文字を列挙する
'''

_str_.split()
'''
{_str_を|空白で}分割した[文字列リスト]
'''

_str_.split(_str_)
'''
{_str_を|[セパレータ]_str_で}分割した[リスト]
'''

_str_.splitlines()
'''
{_str_を|改行で}分割した[文字列リスト]
'''

_str_.splitlines(keepends=True)
'''
{_str_を|改行で}改行を残したまま分割した[文字列リスト]
'''


left, sep, right = _str_.partition()
'''
{_str_を|[最初の|]空白で}二分する
'''

left, sep, right = _str_.partition(_str_)
'''
{_str_を|[最初の|][セパレータ]_str_で}二分する
'''

left, sep, right = _str_.rpartition()
'''
{_str_を|最後の空白で}二分する
'''

left, sep, right = _str_.rpartition(_str_)
'''
{_str_を|最後の[セパレータ]_str_で}二分する
'''

_str_.partition(_str_)[0]
'''
_str_中の[最初の]_str_より前の文字列
_str_から[最初の]_str_より後の[余分な|]文字を除去した[文字列]
'''

_str_.partition(_str_)[-1]
'''
_str_中の[最初の]_str_より後の文字列
_str_から[最初の]_str_より前の[余分な|]文字を除去した[文字列]
'''

_str_.rpartition(_str_)[0]
'''
_str_中の[最後の]_str_より前の文字列
_str_から[最後の]_str_より後の[余分な|]文字を除去した[文字列]
'''

_str_.rpartition(_str_)[-1]
'''
_str_中の[最後の]_str_より後の文字列
_str_から[最後の]_str_より前の[余分な|]文字を除去した[文字列]
'''

# 置換

_str_.replace(_str_, _str_)
'''
_str_中の[部分文字列]_str_を[別の]_str_に[全て|]置換した[文字列]
'''

_str_.replace(_str_, _str_, 1)  # 回数制限
'''
文字列置換の回数制限をする
_str_中の[部分文字列]_str_を[別の]_str_に[一度|一回]だけ置換した[文字列]
'''

_str_.replace(_str_, "")
'''
_str_中の[部分文字列]_str_を[全て|]除去した[文字列]
'''

_str_.expandtabs(tabsize=n)
'''
_str_中のタブ[文字|]を[|n個の]空白に置換した[文字列]
'''

# トリム

_str_.strip()
'''
_str_[|の両端]から[不要な|余分な]空白や改行を除去した[文字列]
_str_をトリムした[文字列]
'''

_str_.lstrip()
'''
_str_の先頭から[不要な|]空白や改行を除去した[文字列]
_str_を左トリムした[文字列]
'''

_str_.rstrip()
'''
_str_の末尾から[不要な|]空白や改行を除去した[文字列]
_str_を右トリムした[文字列]
'''

_str_.strip(_str_)
'''
_str_の両端から[余分な]_str_を除去した[文字列]
'''

_str_.lstrip(_str_)
'''
_str_の先頭から[余分な]_str_を除去した[文字列]
'''

_str_.rstrip(_str_)
'''
_str_の末尾から[余分な]_str_を除去した[文字列]
'''

_str_.zfill(8)  # 文字列幅
'''
_str_をゼロ埋めした[文字列]
'''

str(_int_).zfill(8)  # 文字列幅
'''
_int_をゼロ埋めした[文字列]
'''

_str_.center(8)  # 文字列幅
'''
_str_を[センタリング|中央寄せ]した[文字列]
'''

_str_.ljust(40)  # 文字列幅
'''
_str_を左寄せした[文字列]
'''

_str_.rjust(40)  # 文字列幅
'''
_str_を右寄せした[文字列]
'''

_str_.capitalize()
'''
_str_をキャピタライズした[文字列]
'''

_str_.swapcase()
'''
_str_の大文字と小文字を[相互に|]交換した[文字列]
'''

# 包含

_str_ in _str_
'''
[文字|]_str_[が|は]_str_に存在するかどうか
'''

_str_ in _list_
'''
[文字|]_str_[が|は]_list_に存在するかどうか
[文字|]_str_が_list_のいずれかどうか
'''

_str_ not in _str_
'''
[文字|]_str_[が|は]_str_に存在しないかどうか
'''

_str_ not in _list_
'''
[文字|]_str_[が|は]_list_に存在しないかどうか
[文字|]_str_が_list_のいずれでもないかどうか
'''

_str_.find(_str_)
'''
_str_中の[部分文字列|文字]_str_の[位置]
{_str_[中|]から|[部分文字列|文字]_str_[の位置|]を}探索する
'''

_str_.find(_str_, 0, -1)  # 開始位置と終了位置
'''
{_str_中の範囲を指定して|[部分文字列|文字]_str_[の位置|]を}探索する
'''

_str_.rfind(_str_)
'''
_str_の末尾から探索した[部分文字列|文字]_str_の[位置]
{_str_の末尾から|[部分文字列|文字]_str_[の位置|]を}探索する
'''

_str_.rfind(_str_, 0, -1)  # 開始位置と終了位置
'''
{_str_中の末尾から範囲を指定して|[部分文字列|文字]_str_[の位置|]を}探索する
'''

_list_ = ['A', 'B', 'C']

''.join(map(str, _list_))
'''
_list_を[|文字列化して]連結した[文字列]
'''


_str_.join(map(str, _list_))
'''
{_list_を|[セパレータ]_str_[を挟んで|を使って]}連結した[文字列]
'''

_str_.count(_str_)
'''
_str_中の[文字|部分文字列]_str_の出現数
_str_中の[文字|部分文字列]_str_[を|がいくつ存在するか]カウントする
'''

_str_.startswith(_str_)
'''
{_str_が|[文字|部分文字列]_str_で}開始するかどうか
_str_の接頭辞[が|は]_str_と等しいかどうか
'''

_str_.startswith(_str_, _int_)
'''
{_str_の_int_番目以降が|[文字|部分文字列]_str_で}開始するかどうか
'''

_str_.endswith(_str_)
'''
{_str_が|[文字|部分文字列]_str_で}終端するかどうか
_str_の接尾辞[が|は][文字|部分文字列]_str_と等しいかどうか
'''

_str_.removeprefix(_str_)
'''
_str_から[接尾辞]_str_を除去した[文字列]
'''

_str_.removesuffix(_str_)
'''
_str_から[接尾辞]_str_を除去した[文字列]
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

any(c.islower() for c in _str_)
'''
{_str_中に|[ひとつでも|]小文字が}存在するかどうか
'''

any(c.isupper() for c in _str_)
'''
{_str_中に|[ひとつでも|]大文字が}存在するかどうか
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


_str_ = '1 2'

list(map(int, _str_.split()))
'''
_str_を空白ごとに整数化した[リスト]
'''
