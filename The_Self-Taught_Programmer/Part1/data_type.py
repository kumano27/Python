# -*- coding: utf-8 -*-

"""
    データ型
    
    データを性質でグループ分けしたものをデータ型と呼ぶ。
    Pythonのデータ(例:Hello,World!)はオブジェクトと呼ぶ。
    Pyhtonにおけるオブジェクトは同一性、データ型、値の3つの要素
    
    ・オブジェクトの同一性
    コンピュータのメモリーのどこに格納されているかで決まる。
    変化しない
    
    ・オブジェクトのデータ型
    データがどんな性質を持っているかでグループ分けしたもの
    データ型が持つ性質も変化することはない
    
    ・オブジェクトの値
    表すデータ
    2という数値が表すオブジェクトの値は2
    
"""

"""
    "Hello,World!"はstr(string:文字列の省略形)というデータ型のオブジェクト
    値はHello,World!。このstrデータ型のオブジェクトのことを「文字列」と呼ぶ。
    文字列は1つ以上の文字の羅列で、クォートで囲まれる。
    クォートとしてシングルｋォート(')かダブルクォート(")が使用できるが、
    開始時、終了時のクォートを揃える必要がある。
"""
"Hello,World!"
'Hello,World!'

"""
    文字列は文章を表現するのに使わる
    
    数値もまたオブジェクトです。
    文字列とは異なる種類のオブジェクト。
    全ての整数(1,2,3,4...)はintデータ型(integer: 整数の省略型)です。
    2つの整数は掛け算可能だが、2つの文字列は掛け算可
    
    小数(小数点を含む数値)はfloatデータ型で、2.1,8.2,9.999はすべてfloatデータ型のオブジェクト
    これは浮動小数点数という。
"""
2 + 2
2.2 + 2.2


"""
    ブール値のオブジェクトはboolデータ型で、
    値はTrueかFalseのみです
"""
True
False

"""
    NoneTypeデータ型のオブジェクトは常に1つの値しかない
    それがNone。
    値が存在しないことを表現する為に使われる
"""
None