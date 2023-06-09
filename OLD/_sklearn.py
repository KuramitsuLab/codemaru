import numpy as np
import pandas as pd
import sklearn
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split

_データフレーム_ = pd.DataFrame()
_列名_ = 'A'

目的変数 = _データフレーム_[_列名_]
'''
_データフレーム_の_列名_を目的変数にしたい
_データフレーム_から説明変数を選びたい
'''

説明変数 = _データフレーム_[[_列名_]]
'''
_データフレーム_の__列名_[だけ|のみ|を]説明変数にしたい
'''

説明変数 = _データフレーム_[[_列名_, _列名_]]
'''
_列名_と_列名_を説明変数にしたい
２つの_列名_を説明変数にしたい
_データフレーム_から説明変数を選びたい
'''

説明変数 = _データフレーム_[_データフレーム_.columns[:-1]]
'''
_データフレーム_の最後の[列|カラム]以外を[全て|]説明変数にしたい
'''

説明変数 = _データフレーム_[_データフレーム_.columns[1:]]
'''
_データフレーム_の[先頭|最初]の[列|カラム]以外を[全て|]説明変数にしたい
'''

model = sklearn.linear_model.LinearRegression()
'''
@alt(線形回帰モデル=[線形回帰モデル|[単|重]回帰モデル|[線形|回帰]モデル])
@alt(用意したい|準備したい)
@alt(作りたい|[新規|]作成したい)

[新しい|空の|]線形回帰モデルを[作りたい|用意したい]
[線形|単|重|]回帰分析[の準備をしたい|を行いたい]
'''

normalize = True
'''
option: {説明変数を|事前に}正規化したい
'''

fit_intercept = False
'''
option: [切片|バイアス]を[算出|計算]しない
'''

正則化項 = 0.1

model = sklearn.linear_model.Ridge(alpha=0.1)  # alphaは正則化項
'''
[新しい|空の|]リッジ回帰モデルを[作りたい|用意したい]
リッジ回帰分析[の準備をしたい|を行いたい]
'''

model = sklearn.linear_model.Rosso(alpha=0.1)  # alphaは正則化項
'''
[新しい|空の|]ロッソ回帰モデルを[作りたい|用意したい]
ロッソ回帰分析[の準備をしたい|を行いたい]
'''

model = sklearn.linear_model.ElasticNet()
'''
@alt(ハイブリッド|組み合わせた)

[新しい|空の|]リッジ回帰とロッソ回帰のハイブリットモデルを[作りたい|用意したい]
リッジ回帰とロッソ回帰のハイブリッド分析[の準備をしたい|を行いたい]
正則化付き線形回帰モデルを[作りたい|用意したい]
正則化付き[線形|単|重|]回帰分析[の準備をしたい|を行いたい]
'''

model.fit(説明変数, 目的変数)
'''
@alt(予測モデル=[モデル|回帰モデル|分類モデル])
@alt(教師データ|データ|訓練データ)

予測モデルを[学習したい|作りたい|訓練したい]
{教師データで|予測モデル}を学習したい
{説明変数と目的変数で|予測モデルを}学習したい
予測モデルの[当てはめを実行したい|訓練を開始したい]
予測モデルを[当て|あて]はめたい
'''

model = sklearn.linear_model.LinearRegression()
model.fit(説明変数, 目的変数)
'''
[線形|単|重]回帰モデルを[学習したい|作りたい|訓練したい]
'''


model.coef_
'''
@alt(回帰変数|係数)

線形[|回帰]モデルの回帰変数[|を得る]
'''

model.intercept_
'''
@alt(切片|バイアス)

線形[|回帰]モデルの切片[|を得る]
'''

model = sklearn.linear_model.LinearRegression(fit_intercept=False)
'''
切片なしの線形回帰モデルを[作りたい|用意したい]
切片なしの[線形|単|重|]回帰分析[の準備をしたい|を行いたい]
'''

y_pred = model.predict(説明変数)
'''
予測モデルから目的変数を予測したい
'''

pd.DataFrame({'実測': 目的変数, '予測': model.predict(説明変数)})
'''
@alt(実測値|目的変数)
{予測モデルの予測値と|実測値を}[比較したい|対比させる]
'''

plt.scatter(目的変数, model.predict(説明変数))
'''
{予測モデルの予測値と|実測値を}散布図に描く
'''

目的変数 - model.predict(説明変数)
'''
予測モデルの残差を求めたい
'''

plt.hist(目的変数 - model.predict(説明変数))
'''
予測モデルの残差をヒストグラムにしたい
'''

sklearn.metrics.mean_absolute_error(データ列, データ列)
'''
[データ列[間|]の|][平均絶対誤差|MAE]を求めたい
'''

np.sqrt(sklearn.metrics.mean_squared_error(データ列, データ列))
'''
[データ列[間|]の|][平方根平均二乗誤差|RMSE]を求めたい
'''

sklearn.metrics.mean_squared_error(データ列, データ列)
'''
[データ列[間|]の|]平均[二|２]乗誤差を求めたい
[MSE|Mean Squared Error]を求めたい 
'''

sklearn.metrics.mean_squared_error(目的変数, model.predict(説明変数))
'''
予測モデルの[平均[二|２]乗誤差|精度|正確さ]を求めたい
'''

sklearn.metrics.r2_score(データ列, データ列)
'''
@alt(決定係数|R2|[当て|あて]はまりの良さ|寄与率)
[データ列[間|]の|]決定係数を求めたい
'''

sklearn.metrics.r2_score(目的変数, model.predict(説明変数))
'''
予測モデルの[当てはまりの良さ|決定係数]を求めたい
'''

X_train, X_test, y_train, y_test = train_test_split(説明変数, 目的変数, test_size=0.3)
'''
ホールドアウト[法|]を使う
訓練データとテストデータに分割したい
'''


sklearn.model_selection.cross_val_score(model, 説明変数, 目的変数, cv=5, scoring='r2')
'''
@alt(交差検証|クロスバリデーション)
回帰モデルを交差検証したい
'''


model = sklearn.tree.DecisionTreeRegressor()
'''
[新しい|空の|]回帰木モデルを[作りたい|用意したい]
回帰木分析[の準備をしたい|を行いたい]
'''

sklearn.tree.plot_tree(model, feature_names=X.columns, filled=True)
'''
@alt(決定木|回帰木|分類木)

決定木を表示したい
決定木を[可視化|グラフ[化|に]]したい
'''

plt.barh(X.columns, model.feature_importances_)
'''
@alt(決定木|回帰木|分類木)

決定木の重要度を表示したい
決定木の重要度を[可視化|グラフ[化|に]]したい
'''

n = 2

maxdepth = n
'''
option: [決定木の|][深さを制限したい|最大深さを設定したい]
'''

# クラス分類

model = sklearn.linear_model.LogisticRegression()
'''
[新しい|空の|]ロジスティック回帰モデルを[作りたい|用意したい]
線形のクラス分類[をしたい|を行いたい]
'''

混同行列 = sklearn.metrics.confusion_matrix(正解データ列, 予測データ列)
'''
@alt(クラス分類結果=[クラス分類|[分類|予測]結果|分類モデル])

クラス分類結果の[予測精度|偽陽性|偽陰性|真陽性|真陰性]を見る
[予測データの|][混同行列|コンフュージョン・マトリックス]を[求めたい|算出したい]
'''

sns.heatmap(混同行列, annot=True, cmap='Reds')
'''
{混同行列を|ヒートマップで}確認したい
'''

sns.heatmap(confusion_matrix(正解データ列, 予測データ列), annot=True, cmap='Reds')
'''
{クラス分類の[予測精度|偽陽性|偽陰性]を|ヒートマップで}見る
'''

sklearn.metrics.accuracy_score(正解データ列, 予測データ列)
'''
クラス分類結果の[正解率|正確さ|アキュレシー|分類精度]を求めたい 
'''

sklearn.metrics.precision_score(正解データ列, 予測データ列)
'''
クラス分類結果の[適合率|PPV]を求めたい 
偽陽性を[避けたい|抑えたい]指標を使う
'''

sklearn.metrics.recall_score(正解データ列, 予測データ列)
'''
クラス分類結果の[再現率|リコール|真陽性率|感度]を求めたい 
偽陰性を[避けたい|抑えたい]指標を使う
'''

sklearn.metrics.f1_score(正解データ列, 予測データ列)
'''
クラス分類結果の[F値|適合率と再現率の調和平均]を求めたい 
'''


# 回帰

model = sklearn.ensemble.RandomForestRegressor(n_estimators=10)  # ランダム性
model.fit(説明変数, 目的変数)
'''
@alt(を使って|を用いて|で)
{ランダムフォレストを使って|回帰分析を}[行いたい|したい]
'''


model = sklearn.svm.SVR(kernel='rbf', C=1e3, gamma=0.1, epsilon=0.1)
model.fit(説明変数, 目的変数)
'''
{サポートベクターマシンを使って|回帰分析を}[行いたい|したい]
'''

model = sklearn.gaussian_process.GaussianProcessRegressor()
model.fit(説明変数, 目的変数)
'''
{ガウス過程を使って|回帰分析を}[行いたい|したい]
'''

model = sklearn.neighbors.KNeighborsRegressor(n_neighbors=5)
model.fit(説明変数, 目的変数)
'''
{[K最近傍法|KNN]で|回帰分析を}[行いたい|したい]
'''

model = sklearn.linear_model.SGDRegressor()
model.fit(説明変数, 目的変数)
'''
{[確率的勾配降下|SDG]で|回帰分析を}[行いたい|したい]
'''

model = sklearn.neural_network.MLPRegressor(hidden_layer_sizes=(10, 10))
model.fit(説明変数, 目的変数)
'''
{[パーセプトロン|ニューラルネット|多層パーセプトロン|MLP]で|回帰分析を}[行いたい|したい]
'''

model = sklearn.cross_decomposition.PLSRegression(n_components=10)
model.fit(説明変数, 目的変数)
'''
[|新しい|空の]部分的最小二乗回帰モデルを[作りたい|用意したい]
{[部分的最小二乗法|PLS]で|回帰分析を}[行いたい|したい]
'''

model = sklearn.linear_model.RANSACRegressor(random_state=0)
model.fit(説明変数, 目的変数)
'''
[|新しい|空の]ロバスト回帰モデルを[作りたい|用意したい]
{[ロバスト推定|RANSAC]で|回帰分析を}[行いたい|したい]
'''

model = sklearn.linear_model.HuberRegressor()
model.fit(説明変数, 目的変数)
'''
[ロバストな|外れ値に強い]線形回帰モデルを[作りたい|用意したい]
[ロバストな|外れ値に強い][線形|単|重|]回帰分析[の準備をしたい|を行いたい]
'''

model = sklearn.ensemble.GradientBoostingRegressor()
model.fit(説明変数, 目的変数)
'''
[|新しい|空の]勾配ブースティング回帰木を[作りたい|用意したい]
{勾配ブースティングで|回帰分析を}[行いたい|したい]
'''

model = sklearn.ensemble.HistGradientBoostingRegressor()
model.fit(説明変数, 目的変数)
'''
[|新しい|空の]ヒストグラムベースの勾配ブースティング回帰木を[作りたい|用意したい]
{ヒストグラムと勾配ブースティングで|回帰分析を}[行いたい|したい]
'''

model = sklearn.ensemble.AdaBoostRegressor(random_state=0, n_estimators=100)
model.fit(説明変数, 目的変数)
'''
{ブースティングで|回帰分析を}[行いたい|したい]
'''

model = sklearn.ensemble.BaggingRegressor(n_estimators=10)
model.fit(説明変数, 目的変数)
'''
{バギングで|回帰分析を}[行いたい|したい]
'''

sklearn.ensemble.VotingRegressor()
model.fit(説明変数, 目的変数)
'''
{アンサンブル学習で|回帰分析を}[行いたい|したい]
'''

sklearn.ensemble.StackingRegressor()
model.fit(説明変数, 目的変数)
'''
{スタッキングで|回帰分析を}[行いたい|したい]
'''

# 分類器

model = sklearn.ensemble.RandomForestClassifier()
model.fit(説明変数, 目的変数)
'''
{ランダムフォレストで|クラス分類を}[行いたい|したい]
'''

model = sklearn.ensemble.ExtraTreeClassifier(n_estimators=10)
model.fit(説明変数, 目的変数)
'''
{[ランダム性を強化した|よりランダムな]ランダムフォレストで|クラス分類を}[行いたい|したい]
'''

model = sklearn.svm.SVR(kernel='rbf', C=1e3, gamma=0.1, epsilon=0.1)
model.fit(説明変数, 目的変数)
'''
@alt(分類モデル|分類器)

[|新しい]サポート[ベクター|ベクトル]分類モデルを[作りたい|用意したい]
{サポートベクターマシンで|クラス分類を}[行いたい|したい]
'''

model = sklearn.gaussian_process.GaussianProcessClassifier()
model.fit(説明変数, 目的変数)
'''
[|新しい|空の]ガウス過程分類モデルを[作りたい|用意したい]
{ガウス過程で|クラス分類を}[行いたい|したい]
'''

model = sklearn.neighbors.KNeighborsClassifier(n_neighbors=5)
model.fit(説明変数, 目的変数)
'''
{[K最近傍法|KNN]で|クラス分類を}[行いたい|したい]
'''

model = sklearn.linear_model.SGDClassifier()
model.fit(説明変数, 目的変数)
'''
{[確率的勾配降下|SDG]で|クラス分類を}[行いたい|したい]
'''

model = sklearn.neural_network.MLPClassifier(hidden_layer_sizes=(10, 10))
model.fit(説明変数, 目的変数)
'''
{[パーセプトロン|ニューラルネット|多層パーセプトロン|MLP]で|クラス分類を}[行いたい|したい]
'''

model = sklearn.linear_model.RANSACClassifier(random_state=0)
model.fit(説明変数, 目的変数)
'''
[|新しい|空の]ロバスト分類モデルを[作りたい|用意したい]
{[ロバスト推定|RANSAC]で|クラス分類を}[行いたい|したい]
'''

model = sklearn.linear_model.HuberClassifier()
model.fit(説明変数, 目的変数)
'''
[ロバストな|外れ値に強い]線形分類モデルを[作りたい|用意したい]
[ロバストな|外れ値に強い][線形|単|重|]クラス分類[の準備をしたい|を行いたい]
'''

model = sklearn.ensemble.GradientBoostingClassifier()
model.fit(説明変数, 目的変数)
'''
[|新しい|空の]勾配ブースティング分類木を[作りたい|用意したい]
{勾配ブースティングで|クラス分類を}[行いたい|したい]
'''

model = sklearn.ensemble.HistGradientBoostingClassifier()
model.fit(説明変数, 目的変数)
'''
[|新しい|空の]ヒストグラムベースの勾配ブースティング分類木を[作りたい|用意したい]
{ヒストグラムと勾配ブースティングで|クラス分類を}[行いたい|したい]
'''

model = sklearn.ensemble.AdaBoostClassifier(random_state=0, n_estimators=100)
model.fit(説明変数, 目的変数)
'''
{ブースティングで|クラス分類を}[行いたい|したい]
'''

model = sklearn.ensemble.BaggingClassifier(n_estimators=10)
model.fit(説明変数, 目的変数)
'''
{バギングで|クラス分類を}[行いたい|したい]
'''

sklearn.ensemble.VotingClassifier()
model.fit(説明変数, 目的変数)
'''
{アンサンブル学習で|クラス分類を}[行いたい|したい]
'''

sklearn.ensemble.StackingClassifier()
model.fit(説明変数, 目的変数)
'''
{スタッキングで|クラス分類を}[行いたい|したい]
'''


# 教師なし

model = sklearn.decomposition.PCA(n_components=n)
'''
[主成分分析|固有値分解|因子分析|スペクトル分解][を行いたい|の準備をしたい]
'''

sklearn.decomposition.PCA(n_components=_整数_).fit_transform(多次元データ)
'''
{[多次元データを|]|主成分分析で}_整数_次元に[次元|]削減したい
'''

model = sklearn.decomposition.TruncatedSVD(n_components=n)
'''
[特異値分解|SVD][を行いたい|の準備をしたい]
'''

sklearn.decomposition.TruncatedSVD(n_components=_整数_).fit_transform(多次元データ)
'''
{[多次元データを|]|[特異値分解|SVD]で}_整数_次元に[次元|]削減したい
'''

model = sklearn.manifold.MSD(n_components=n)
'''
[多次元尺度構成法|MSD][を行いたい|の準備をしたい]
'''

sklearn.manifold.MSD(n_components=_整数_).fit_transform(多次元データ)
'''
{[多次元データを|]|[多次元尺度構成法|MSD]で}_整数_次元に[次元|]削減したい
'''

model = sklearn.manifold.TSNE(n_components=n)
'''
[[フィッシャーの|]線形判別分類|t-SNE|t分布型確率的近傍埋め込み法][を行いたい|の準備をしたい]
'''

sklearn.manifold.TSNE(n_components=_整数_).fit_transform(多次元データ)
'''
{[多次元データを|]|[t-SNE|t分布型確率的近傍埋め込み法]で}_整数_次元に[次元|]削減したい
'''

sklearn.preprocessing.StandardScaler().fit_transform(データ)
'''
@alt(スケール変換|スケーリング)

[データを|][標準化|スケール変換]したい
{[データを|]|平均と分散で}標準化を行いたい
'''

sklearn.preprocessing.RobustScaler().fit_transform(データ)
'''
[データを|]外れ値に[頑健な|ロバストな]標準化を行いたい
{[データを|]|四分位点で}[標準化|スケール変換]したい
'''

sklearn.preprocessing.MaxAbsScaler().fit_transform(データ)
'''
{[データを|]|最大値で}正規化[したい|を行いたい]
'''

sklearn.preprocessing.MinMaxScaler().fit_transform(データ)
'''
{[データを|]|[最大値と最小値|最大最小]で}正規化[したい|を行いたい]
{[データを|]|[最大最小値|最大最小]で}[標準化|スケール変換]したい
'''

sklearn.preprocessing.MinMaxScaler(feature_range=(0, 1)).fit_transform(データ)
'''
{[データを|]|[最大値と最小値|最大最小]で}[正規化したい|揃える]
'''

np.log(データ列)
'''
データ列[の偏り|]を対数変換したい
'''

np.sqrt(データ列)
'''
データ列[の偏り|]を平方根変換したい
'''

sklearn.preprocessing.Normalizer(norm="l1").fit_transform(データ列)
'''
{[データを|]|L1ノルムで}正則化[したい|を行いたい]
'''

sklearn.preprocessing.Normalizer(norm="l2").fit_transform(データ列)
'''
{[データを|]|L2ノルムで}正規化[したい|を行いたい]
データ列のノルムを[揃える|そろえたい]
'''

sklearn.preprocessing.Binarizer(threshold=閾値).fit_transform(データ列)
'''
{[データ列を|]|[閾値|指定した値]で}[二値化|バイナリ化]したい
'''

sklearn.preprocessing.LabelEncoder().fit_transform(データ列)
'''
[カテゴリ|非数値]データ[列|]を[数値|連番]化したい
[カテゴリ|非数値]データ[列|]を連番に変換したい
'''

sklearn.preprocessing.OneHotEncoder(sparse=False).fit_transform(データ列)
'''
[カテゴリ|非数値]データ[列|]を[ワン・ホット|]ベクトル化したい
'''
