import matplotlib
import matplotlib.pyplot as plt

__データ列__ = [1, 2, 3]
__データ列2__ = [2, 3, 4]
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
matplotlibで[使える|利用可能な]色の名前の一覧が欲しい
色の名前とカラーコード[の[対応表|一覧]]が欲しい
'''

色名 = 'red'

matplotlib.colors.cnames[色名]
'''
色の名前からカラーコードを知りたい
色の名前からコードに変換したい
'''

# アルファ値

alpha = 0.5
'''
@alt(透明度|アルファ[|値])

<option>[色を|表示を|]半透明にしたい
<option>色の透明度を設定したい
'''

color = __色名__
'''
<option>色は__色名__
<option>__色名__[色|]を使いたい
'''

color = __色名2__
'''
<option>色は__色名2__
<option>__色名2__色を使いたい
'''

color = __色名3__
'''
<option>色は__色名3__
<option>__色名3__色を使いたい
'''

color = __和色名__
'''
<option>色は__和色名__[色|]
<option>__和色名__色を使いたい
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

plt.plot(__データ列__, __データ列__, alpha=0.5)
'''
折れ線グラフの透明度を設定したい
折れ線グラフを半透明にしたい
'''

plt.hist(__データ列__, alpha=0.5)
'''
ヒストグラムを半透明[に|化]したい
ヒストグラムを描画して、半透明[に|化]にしたい
'''

plt.plot(__データ列__, __データ列2__, color=__色名__)
'''
[折れ|]線グラフの色を__色名__に設定したい
__色名__色の[|折れ]線グラフを描画したい
{[折れ|]線グラフを|__色名__色で_}描画したい
'''

plt.hist(__データ列__, color=__色名__)
'''
{ヒストグラムの色を|__色名__に}設定したい
__色名__色のヒストグラムを描画したい
{ヒストグラムを|__色名__色で_}描画したい
'''

plt.scatter(__データ列__, __データ列2__, color=__色名__)
'''
散布図の色を__色名__にしたい
__色名__色の散布図を描画したい
{散布図を|__色名__色で_}描画したい
'''

plt.scatter(__データ列__, __データ列2__, color=__和色名__)
'''
散布図を__和色名__[|色]にしたい
'''

plt.bar(__データ列__, __データ列2__, color=__色名__)
'''
[|縦]棒グラフの色を__色名__にしたい
__色名__色の[|縦]棒グラフを描画したい
{[|縦]棒グラフを|__色名__色で_}描画したい
'''

plt.bar(__データ列__, __データ列2__, color=__色名2__)
'''
[|縦]棒グラフを__色名2__[|色]にしたい
'''

plt.barh(__データ列__, __データ列2__, color=__色名__)
'''
横棒グラフの色を__色名__にしたい
__色名__色の横棒グラフを描画したい
{横棒グラフを|__色名__色で_}描画したい
'''

plt.bar(__データ列__, __データ列2__, color=__色名3__)
'''
横棒グラフを__色名3__[|色]にしたい
'''

_ = None


plt.hist(__データ列__, alpha=_, color=_)
'''
ヒストグラムを描画したい
'''
