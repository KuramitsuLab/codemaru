# https://knooto.info/python-snippets/#json

import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['font.size'] = 18
plt.tight_layout()
'''
[matplotlibで|]グラフの[文字|フォント]サイズを大きくしたい
グラフの[文字|フォント]サイズを__数値__ptにしたい
'''

x = np.linspace(-3, 3, 20)  # -3～3まで20刻みでxの値を生成
y = x**2 - 1            # 2次関数
plt.plot(x, y, label='$y=x^2+1$')      # 曲線を引く
plt.show()              # グラフ表示
'''
[2次関数|放物線]を[グラフ表示したい|描きたい]
'''

x = np.arange(-np.pi, -np.pi, 0.25)
y = np.sin(x)
plt.plot(x, y, label='$y=\sin{x}$')      # 曲線を引く
plt.show()              # グラフ表示
'''
[サイン|sin][曲線|]をグラフ[描画|表示|化]したい
'''

x = np.arange(-np.pi, -np.pi, 0.25)
y = np.cos(x)
plt.plot(x, y, label='$y=\cos{x}$')      # 曲線を引く
plt.show()              # グラフ表示
'''
[コサイン|cos][|曲線]をグラフ[描画|表示|化]したい
'''

plt.plot(_列名_, _列名2_)
plt.title('(タイトル)')
plt.show()
'''
_列名_と_列名_を[折れ線|]グラフにしたい
'''
