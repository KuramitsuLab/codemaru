import io

import json
'''
@alt(形式|フォーマット)
JSONを使う
'''

_文字列_ = "{'A':1}"
_JSONLファイル_ = 'file.jsonl'
_バイト列_ = b"{'A':1}"
_辞書_ = {'A': 0}
_リスト_ = [1, 2, 3]

# ファイル入力 = io.StringIO(_文字列_)
# ファイル出力 = io.StringIO(mode='w')
# n = 0
# '''
# @alt(ファイル入力|入力ストリーム|入力)
# @alt(ファイル出力|出力ストリーム|出力)
# '''


__ファイル名__ = 'file.json'
__データ__ = _文字列_
'''
@poly(__データ__;_辞書_;_リスト_;_タプル_;_結果_)
@poly(__ファイル名__;_JSONファイル_;ファイル名)
'''

with open(__ファイル名__) as f:
    data = json.load(f)
'''
@alt(読みたい|読み込みたい|ロードしたい)
@alt(構文解析したい|パースしたい|デコードしたい)

__ファイル名__からJSON[形式のデータ|]を読みたい
JSON[形式の|]ファイルを構文解析したい
'''

with open(_JSONLファイル_) as f:
    ss = []
    for line in f.readlines():
        data = json.loads(line)
        ss.append(data)
'''
_JSONLファイル_からJSON[形式のデータ|]を読みたい
JSON[形式の|]ファイルを構文解析したい
'''

data = json.loads(_文字列_)
'''
_文字列_からJSON[形式のデータ|]を読みたい
JSON[形式の|]文字列を構文解析したい
JSON[形式の|]文字列を[辞書|オブジェクト|データ]に変換したい
'''

json.loads(_バイト列_.decode('unicode-escape'))
'''
_バイト列_からJSON[形式のデータ|]を読みたい
JSON[形式の|]バイト列を構文解析したい
'''

json.dumps(__データ__, ensure_ascii=False)
'''
__データ__をJSON[形式の|]文字列に変換したい
__データ__をJSON[形式|]にエンコードしたい
'''

json.dumps(__データ__, ensure_ascii=False, indent=4)
'''
{インデント[|幅]を指定して|__データ__を}JSON文字列に変換したい
{__データ__を|インデント[|幅]を指定して}JSON[形式|]にエンコードしたい
'''

json.dumps(__データ__, ensure_ascii=False, sort_keys=True)
'''
{__データ__を|ソートして}JSON[形式|]にエンコードしたい
'''

with open(__ファイル名__, 'w') as f:
    json.dump(__データ__, f, ensure_ascii=False)
'''
{__データ__を|JSON形式で}__ファイル名__に[保存したい|出力したい|ダンプしたい]
'''

with open(_JSONLファイル_, 'w') as f:
    for data in _リスト_:
        s = json.dumps(data, ensure_ascii=False)
        print(s, file=f)
'''
_リスト_の[要素|データ]をJSON形式に[一行|ひとつ]ずつ変換し、[保存したい|出力したい]
{_リスト_を|JSON[L|]形式で}_JSONLファイル_に[保存したい|出力したい]
'''
