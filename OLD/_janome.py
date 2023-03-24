import janome

from janome.tokenizer import Tokenizer
janome = Tokenizer()
for token in janome.tokenize(_文字列_):
    print(token)
'''
_文字列_を形態素解析したい
'''
