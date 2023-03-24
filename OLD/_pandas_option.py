import pandas as pd

# 設定

print(pd.__version__)
'''
@alt(確認したい|プリントし[|ておき]たい)
Pandasのバージョンを確認したい
'''

pd.set_option('display.max_columns', n)
'''
@alt(表示可能な|表示できる|表示したい|表示される)
@alt(変更したい|設置したい|増やしたい|表示される)

{データフレームの|[表示可能な|]}[最大|]列数を変更したい
'''

pd.set_option('display.max_rows', n)
'''
{データフレームの|[表示可能な|]}[最大|]行数を変更したい
'''

pd.set_option('precision', n)
'''
{データフレームの|[表示可能な|]}[|表示]精度を変更したい
'''

pd.set_option('expand_frame_repr', False)
'''
[データフレームを表示したいとき、|]折り返しをしない[|ようにしたい]
[データフレームを表示したいとき、|]折り返しを[オフ|無効]に設定したい
'''

pd.set_option('max_colwidth', n)
'''
[データフレームを表示したいとき、|]カラムの最大幅をnに設定したい
'''

pd.set_option('colheader_justify', 'right')
'''
[データフレームを表示したいとき、|]ヘッダー行を右寄せに設定したい
'''

pd.set_option('colheader_justify', 'left')
'''
[データフレームを表示したいとき、|]ヘッダー行を左寄せに設定したい
'''

# 読み込み系

index_col = n
'''
option: n番目のカラムをインデックスに設定したい
'''

index_col = None
'''
option: インデックスを[自動的な|]連番に設定したい
option: どのカラムもインデックスに[設定|]しない
'''

header = 0
'''
@alt(ヘッダ|カラムの名前)
option: [先頭の|最初の]行をヘッダに設定したい
'''

header = None
'''
option: ヘッダを[自動的な|]連番に設定したい
option: どの行もヘッダに[|設定]しない
'''

列名リスト = ['列A', '列B']

names = 列名リスト
'''
option: カラムの名前をリストで設定したい
'''

usecols = names
'''
option: 読みたい行番号をnamesで指定したい
'''

skiprows = names
'''
option: [読み込まない|スキップしたい|無視したい]列番号をnamesで指定したい
'''

skipfooter = n
'''
option: [読み込まない|スキップしたい|無視したい]フッタをnに設定したい
'''
