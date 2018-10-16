# -*- coding: utf-8 -*-

"""
    文
    
    Pyhonには2種類の文がある。単純文と複合文の2つ。
    単純文は1行のコードで表現される。
    複合分は通常複数の行で表現される。
"""

# 単純文
print("Helo,World!")

"""
    if文、if-else文、100times_display.pyは全て複合文
    
    複合文は1つ以上の節で構成される。
    1つの節は2行以上のコードで、1行のヘッダー部分と、それに続くスイート部分で構成される
    
    ヘッダーはキーワードが含まれる1行のコード。
    行の最後にコロンがありインデントされた1行以上のコードが次の行に続く。
    インデントの後には1つ以上のスイートが続く。1つのスイートは1行のコードだけで構成される。
    ヘッダーがスイートを制御する。
    
    以下のコードは「Hello,World!」 を100回表示する1つの複合文。
    
    プログラムの最初の行はヘッダー。
    ヘッダーにはforキーワードが福間得ている。そして、ヘッダー行の最後はコロンで終わる。
    ヘッダーの次の行以降にインデントされているブロックがスイート。ここでは print("Hello,World!") がスイート。
    この例では、ヘッダー部分はスイート部分にあるprintを100回実行するように制御している。
    この例のようなコードをループというが、ループは後程説明を行う。
    このコードには1つの節だけ含まれている。

"""
for i in range(100):
    print("Hello,World!")
    
"""
    複合文は複数の節を持つこともある。すでに紹介したif-else文は、if文にelse文を続けられるので、
    複数の節を持つ複合文に分類される。複合文に複数の節を持つとき、ヘッダー節はほかの節とセットで動作する
    
    if-else文の例では、if文がTrueに評価された場合、if文のスイート部分が実行され、
    else文のスイートは実行されない。if文がFalseに評価された場合、if文のスイートは実行されず、
    代わりにelse文のスイートが実行される。
    conditional_statement.py の最後に紹介したコードを再確認する。
    これは3つの複合文をもつコード
    
    最初の複合文は3つの節を持っている。
    2つ目の複合文は1つの節、3つ目の複合文は2つの節を持っている。
    
    コード例では、文と文の間に空行を置いている。
    この空行は、コードを見やすくする為に使用している。
"""
x = 100
if x == 10:
    print("10!")
elif x == 20:
    print("20!")
else:
    print("分かりません!")
    
if x == 100:
    print("xは100!")

if x % 2 == 0:
    print("xは偶数!")
else:
    print("xは奇数!")