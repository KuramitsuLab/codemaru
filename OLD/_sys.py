import os
import sys

__オブジェクト__ = 1.0
'''
@poly(__オブジェクト__;オブジェクト;_結果_)
'''
n = 1

sys.byteorder
'''
@alt(プラットホーム|環境|[実行|動作]環境|OS)
@alt(ランタイム|実行環境|インタプリタ)
@alt(が知りたい|を[調べたい|確認したい|確めたい]|が欲しい)
@alt(バイトオーダ|エンディアン)

[|プラットホームの]バイトオーダが知りたい
'''

sys.getdefaultencoding()
'''
[|デフォルトの|プラットホームの]エンコーディングが知りたい
'''

sys.getrefcount(__オブジェクト__)
'''
@alt(ガベージコレクション|ゴミ集め|GC)
[__オブジェクト__の|ガベージコレクションの]参照カウントが知りたい
'''

sys.getsizeof(__オブジェクト__)
'''
@alt(バイトサイズ|メモリ[使用|消費]量)

__オブジェクト__のバイトサイズが知りたい
'''

sys.getrecursionlimit()
'''
@alt(最大の再帰数|スタックの最大[長|の深さ])

[現在の|ランタイムの|]再帰の[最大回数|上限]が知りたい
{何回[まで|、]|再帰が}できるか[を|、][|知りたい]
'''

sys.setrecursionlimit(1000000)
'''
再帰エラーを[未然に|]防ぎたい
再帰の[上限|最大回数]を[上げたい|増やしたい]
'''

文字列 = 'A'

sys.intern(文字列)
'''
文字列を[隔離したい|インターンしたい]
'''

sys.maxsize
'''
[プラットフォームの|][符号付き|]整数の最大値が知りたい
'''

sys.maxunicode
'''
@alt(コードポイント|文字コード)

[プラットフォームの|]コードポイントの最大値が知りたい
'''

sys.platform
'''
@alt(の名前|名)

プラットホームの名前が知りたい
'''

__X__ = 'darwin'
'''
@X('darwin';'linux';'win32')
@Y([MacOS|マック];[Linux|リナックス];[Windows|ウィンドウズ])
'''

sys.platform.startswith(__X__)
'''
プラットホーム[が|は]__Y__かどうか
'''

sys.argv
'''
@alt(コマンド引数|コマンドライン)

コマンド引数[|を列挙したい]
コマンド引数のリスト
'''

sys.argv[0]
'''
@alt(スクリプト名|[スクリプト|プログラム]ファイル名|プログラム名)

スクリプトの名前が知りたい
[プログラム|スクリプト]のファイルの名前が知りたい
'''

sys.argv[1]
'''
[最初の|第一]コマンド引数が知りたい
コマンドの第一引数[を知りたい]
第一引数[で指定された|の]ファイルの名前
'''

sys.argv[1:]
'''
コマンド引数の一覧[|が欲しい]
コマンド引数を[列挙したい|一覧として得る]
'''

if len(sys.argv) > 1:
    print(sys.argv[1])  # 具体的な処理にしたい
'''
もしコマンド引数が[与えられた|指定された]なら、処理したい
'''


for file in sys.argv[1:]:
    print(file)  # 具体的な処理にしたい
'''
コマンド引数で[与えられた|指定された]ファイル[名|]を一つずつ処理したい
'''

sys.flags
'''
コマンド[ライン|]フラグの状態が知りたい
'''

sys.path
'''
モジュールを検索したいパス[|を列挙したい]
Pythonパス[の一覧]が知りたい
'''

ディレクトリ名 = '.'

sys.path.append(ディレクトリ名)
'''
{モジュール[を検索したい|の検索]パスに|ディレクトリを}追加したい
{Pythonパスに|ディレクトリを}追加したい
'''

sys.path.append(os.path.join(os.path.dirname(__file__), ディレクトリ名))
'''
{スクリプトのサブディレクトリを|Pythonパスに}加えたい
'''

sys.modules
'''
[|既に]ロードされたモジュール[の一覧が知りたい|を列挙したい]
モジュールを列挙したい
'''

sys.modules[__name__]
'''
現在のモジュール[|が欲しい]
{自分自身を|モジュールとして}[|が欲しい]
'''

etype, evalue, traceback = sys.exc_info()
'''
[現在|][処理|実行]中の[例外|エラー]情報が知りたい
[例外|エラー]の[種類|メッセージ|トレースバック][|を|を知りたい]
'''

sys.executable
'''
[Python|]インタプリタの実行ファイルの絶対パスが知りたい
'''

sys.stdin
'''
標準入力が欲しい
標準入力[を使いたい|]
'''

file = sys.__X__
'''
@X(stdout;stderr;open('file.txt', 'w'))
@Y(標準出力;標準エラー;ファイル)

option: 出力先を__Y__に設定したい
option: __Y__に出力したい
option: __Y__を使いたい
option: __Y__を出力[|先]にしたい
'''

sys.stdout
'''
標準出力が欲しい
標準出力[を使いたい|]
'''

sys.stderr
'''
標準エラーが欲しい
標準エラー[を使いたい|]
エラーを出力したい
'''

sys.stdin.read(1)
'''
@alt(読む|読み込む)
{標準入力から|1文字[だけ|分|]}読む
'''

sys.stdin.readline()
'''
{標準入力から|1行[だけ|分|]}読む
'''

sys.stdin.readline().rstrip()
'''
{標準入力から|1行[だけ|分|]|改行[なし[で|に]|を[取り|]除いて]}読む
{標準入力から|1行[だけ|分|]}読み込んで、改行を取り除く
'''

sys.stdout.flush()
'''
@alt(フラッシュしたい|強制表示したい|即時表示したい)
標準出力[のバッファ|]をフラッシュしたい
'''

sys.stdout.isatty()
'''
[実行時の|]標準出力[の出力先|先|]がターミナルかどうか
標準出力がターミナル出力かどうか
'''

not sys.stdout.isatty()
'''
[実行時に|]標準出力がパイプかどうか
'''

os.isatty(sys.stdin.fileno())
'''
[実行時の|]標準入力[の入力元|のソース]がターミナルかどうか
'''

# sys.path.insert(1, os.path.dirname(os.path.realpath(__file__)))
# sys.path.insert(0, '..')
# sys.path.insert(0, os.path.abspath('/my/source/lives/here'))
# os.path.dirname(sys.modules['__main__'].__file__)
# sys.path.append(os.path.join(os.environ['SPARK_HOME'], 'bin'))
# os.path.realpath(os.path.dirname(sys.argv[0]))
# sys.stdout.isatty()
# os.path.dirname(sys.executable)
# getattr(sys.modules[__name__], 'A')
# os.isatty(sys.stdin.fileno())
# sys.stdout = sys.stdout.detach()
# caller = sys._getframe(1)
# calling_frame = sys._getframe().f_back
# current_frame = sys._getframe(0)
# cur_version = sys.version_info
# f = sys.exc_info()[2].tb_frame
# sys.stdin.fileno()
# inspect.getmembers()
# func_name = sys._getframe().f_code.co_name
# if not sys.stdin.isatty():
# sys._getframe().f_code.co_name

if sys.version_info >= (3, 4):
    print(sys.version_info)
'''
Pythonのバージョン[を確認したい|を知りたい]
'''


sys.exit()
'''
@alt(終了したい|停止したい|止めたい|終えたい)
@alt(プログラムの実行|プログラム|実行)

プログラムの実行を[強制的に|ここで|即座に]終了したい
'''

sys.exit(0)
'''
プログラムの実行を[正しく|正常[に|]|適切に]終了したい
'''

sys.exit(1)
'''
プログラムの実行を[異常|エラーとして]終了したい
'''
