import pandas as pd
'''
@test($$;type(pd))
@alt(全ての|すべての|全)
@alt(の名前|名)
@alt(見る|知る|調べる)

@prefix(value;[文字列|日付|])
'''

dateList = [pd.to_datetime('12-12-12'), pd.to_datetime('12-12-12')]
_データフレーム_ = pd.DataFrame(data={'列A': dateList, '列B': [1, 2]})
_列名_ = '列A'


日付を表現した文字列 = '11-01-01'  # 例
pd.to_datetime(日付を表現した文字列)
'''
@alt(日付データ|タイムスタンプ[型|]|Pandasの日付[型|データ]|datetime64型)
[日付を表現した|]文字列を日付データに変換したい
'''

__データ列__ = _データフレーム_[_列名_]
__データシリーズ__ = __データ列__
'''
@poly(__データ列__;_列名_ _データフレーム_[_列名_];_リスト_)
@poly(__データシリーズ__;_列名_ _データフレーム_[_列名_];_データ列_)
'''

pd.to_datetime(__データ列__)
'''
__データ列__を[全て|]日付データに変換したい
'''

pd.to_datetime(__データ列__, format='%Y-%m-%d')
'''
@alt(フォーマット|書式)

{__データ列__を|フォーマット[にしたがって|を指定して]}[全て|]日付データに変換したい
'''

# エポック秒

pd.to_datetime(__データ列__, unit='s', utc=True)
'''
@alt(エポック秒|UNIX秒|UNIX時間)

エポック秒から日付データに変換したい
__データ列__のエポック秒を[全て|]日付データに変換したい
'''

_データフレーム_.set_index(_列名_, inplace=True)
'''
_データフレーム_のあるカラムをインデックスにしたい
'''

_データフレーム_.index = pd.DatetimeIndex(_データフレーム_[_列名_])
'''
_列名_の日付を[_データフレーム_の|]インデックスにしたい
'''

_データフレーム_.index = pd.DatetimeIndex(pd.to_datetime(_データフレーム_[_列名_]))
'''
_列名_を日付データに変換し、[_データフレーム_の|]インデックスにしたい
'''

__データシリーズ__.tz_convert('Asia/Tokyo')
'''
__データシリーズ__のタイムゾーンを[日本|東京]に設定したい
__データシリーズ__のタイムゾーンを設定したい
'''

__データシリーズ__.dt.year
'''
__データシリーズ__の年[|度]が欲しい
__データシリーズ__[が|は]何年か調べたい
'''

__データシリーズ__.dt.month
'''
__データシリーズ__の月が欲しい
__データシリーズ__[が|は]何月か調べたい
'''

__データシリーズ__.dt.day
'''
__データシリーズ__の[日|日にち]が欲しい
__データシリーズ__[が|は]何日か調べたい
'''

__データシリーズ__.dt.hour
'''
__データシリーズ__の[時|時刻]が欲しい
__データシリーズ__[が|は]何時か調べたい
'''

__データシリーズ__.dt.minute
'''
__データシリーズ__の分が欲しい
__データシリーズ__[が|は]何分か調べたい
'''

__データシリーズ__.dt.second
'''
__データシリーズ__の秒が欲しい
__データシリーズ__[が|は]何秒か調べたい
'''

__データシリーズ__.dt.weekday_name
'''
__データシリーズ__の曜日[の名前|]が欲しい
__データシリーズ__[が|は]何曜日か調べたい
'''

__データシリーズ__.dt.dayofweek
'''
__データシリーズ__の曜日数が欲しい
__データシリーズ__の曜日[[が|は]何日目か|を]調べたい
'''
