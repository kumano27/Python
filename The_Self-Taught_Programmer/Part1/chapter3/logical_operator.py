# -*- coding: utf-8 -*-

"""
    論理演算子
    
    比較演算子同様True、Falseのどちらかを返す
"""


"""
    and
    
    Pythonのキーワードで、andの左右に与えられた式が
    True と評価される場合はTrueを返し、どちらかがFalseと評価された場合、Falseを返す
"""
1 == 1 and 2 == 2
# >> True
1 == 2 and 2 == 2
# >> False
1 == 2 and 2 == 1
# >> False
2 == 1 and 1 == 1
# >> False
# and キーワードは1つの文に複数回使える
1 == 1 and 10 != 2 and 2 < 10
# >> True

"""
    or
    
    orの左右に与えられた式どちらかがTrueと評価されればTrueを返す
"""
1 == 1 or 1 == 2
# >> True
1 == 1 or 2 == 2
# >> True
1 == 2 or 2 == 1
# >> False
2 == 1 or 1 == 2
# >> False
# and キーワードと同様1つの文に複数回使える
1 == 1 or 1 == 2 or 1 == 3
# >> True
# 1 == 1がTrueなので、残りの他の式がFalseと評価されたとしても、最終的な評価はTrueになる

"""
    not
    
    notキーワードは式の前に書いて、その式の評価結果を逆転させる。
"""
# Trueと評価される式の前に not を書く
not 1 == 1
# >> False
not 1 == 2
# >> True