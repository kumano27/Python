# -*- coding: utf-8 -*-

"""
    比較演算子
    
    比較演算子は算術演算子と同様に、2つの被演算子と1つの演算子で1つの式を表す。
    Pythonでは、比較演算子は算術演算子とは別のカテゴリ。
    比較演算子を使った式はTrueかFalseのどちらかしか返さない
   
"""

# 演算子 > の左側の数値が右側の数値よりも大きければ、この式はTrueを返し、そうでなければFalseを返す
100 > 10
# >> True

# 演算子 < の左側の数値が右側の数値よりも小さければ、この式はTrueを返し、そうでなければFalseを返す
100 < 10
# >> False

# 演算子 >= の左側の数値が右側の数値以上であれば、この式はTrueを返し、そうでなければFalseを返す
2 >= 2
# >> True

# 演算子 <= の左側の数値が右側の数値以下であれば、この式はTrueを返し、そうでなければFalseを返す
2 <= 2
# >> True

# 演算子 == の左側の数値と右側の数値が同じ値であれば、この式はTrueを返し、そうでなければFalseを返す
2 == 2
# >> True

1 == 2
# >> False

# 演算子 != の左側の数値と右側の数値が異なる値であれば、この式はTrueを返し、そうでなければFalseを返す
1 != 2
# >> True

2 != 2
# >> False

"""
    x = 100 のように、=は数値を変数に割り当てる為に使う
    「xは100に等しい」と読みそうになるがそれはNG
    =は値を変数に割り当てる為に使用するが、xが100かのチェックはしない。
    なので「xに100が代入された」と読む。
    
    比較演算子 == は値の検証に使われるので、 x == 100というコードを見たら
    「ｘが100と同じかどうか」と考える。
"""