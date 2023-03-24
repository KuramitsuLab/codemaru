import matplotlib
import matplotlib.pyplot as plt
'''
@poly(__色名__;青 "blue";緑 "green";赤 "red";シアン "cyan";マゼンタ "magenta";黄 "yellow";黒 "black";白 "white")
'''

__色名__ = 'r'

color = __色名__
'''
option: __色名__[色|]を使う
'''

plt.barh(__データ列__, __データ列2__, color=__色名__)
'''
横棒グラフの色を__色名__にする
__色名__色の横棒グラフを描画する
{横棒グラフを|__色名__色で_}描画する
'''
