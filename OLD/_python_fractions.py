import math
import numbers

import fractions
'''
@alt(有理数|分数)

有理数が使いたい
'''

_整数_ = 1
_文字列_ = "1/2"
_数値_ = 0.5
_結果_ = 1
_有理数_ = fractions.Fraction(1, 2)

分子, 分母 = 1, 2
fractions.Fraction(分子, 分母)
'''
有理数が欲しい
'''

fractions.Fraction(numerator=_整数_, denominator=_整数_)
'''
分子_整数_、分母_整数_の有理数が欲しい
'''

fractions.Fraction(_文字列_)
'''
_文字列_を有理数に変換したい
'''

fractions.Fraction(_数値_)
'''
_数値_を有理数に変換したい
'''

_有理数_.numerator
'''
_有理数_の分子が欲しい
'''

_有理数_.denominator
'''
_有理数_の分母が欲しい
'''

float(_有理数_)
'''
_有理数_を浮動小数点数に変換したい
'''

math.ceil(_有理数_)
'''
_有理数_を切り上げたい
_有理数_の天井数が欲しい
'''

math.floar(_有理数_)
'''
_有理数_を切り下げたい
_有理数_の床数が欲しい
'''

fractions.Fraction(_数値_).limit_denominator()
'''
_数値_の{有理数|近似}が欲しい
'''

fractions.Fraction(_数値_).limit_denominator(max_denominator=_整数_)
'''
_数値_の{有理数|近似}が欲しい。分母の最大値は_整数_
'''


isinstance(_結果_, numbers.Number)
'''
_結果_が数かどうか
'''
