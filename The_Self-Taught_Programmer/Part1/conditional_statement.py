# -*- coding: utf-8 -*-

"""
    条件文
    
    if、elif、そしてesleのキーワードは条件文に使用する。
    条件文は制御構造の1つで、与えられた変数の値で実行を判断するコードの塊(ブロック)
    条件文は与えられた条件によって追加の処理を実行する。
    以下に条件文がどのように動作するかを表した擬似コードで表す
    
    もし(式)なら
        (コード群1)
    そうでなければ
        (コード群2)
        
    この擬似コードは、2つの実行コードを条件によって切り替えられることを表す。
    最初の式がTrueに評価される場合、コード群1に書かれたコードがすべて実行される。
    反対に、最初の式がFalseに評価されれば、コード群2に書かれたコードがすべて実行される。
    
    この式が書かれている「もし」の行をif文と言う。「そうでなければ」の部分はelse文。
    両方合わせてif-else文と呼ぶこともある。
    
    以下にPythonでif-else文を使ったコード例を書く。
    
"""
home = 'アメリカ'
if home == 'アメリカ':
    print("Hello,America!")
else:
    print("Hello,World!")
    
"""
    27-28行目がif文の使い方
    if文はifキーワードで始まって、直後に書く式の最後に:(コロン)を書き、
    その式がTrueだった場合に実行したい1行以上のコードブロックをインデントして書く
    
    29-30行目がelse文の使い方
    else文はelseキーワードで始まって、直後にコロン(:)を書き、
    if文の式がFalseだった場合に実行したい1行以上のコードブロックをインデントして書く
    
    この例では Hello,America! と出力されているが、これはif文にある式がTrueｔ評価されているから。
    もし、homeに日本という文字列を代入していれば式はFalseに評価されるので、
    else文のこーどが実行され、画面にはHello,World!と表示される。
"""
home = '日本'
if home == 'アメリカ':
    print("Hello,America!")
else:
    print("Hello,World!")
    
# if文だけでも使用可
home = "アメリカ"
if home == "アメリカ":
    print("Hello,America!")

# 複数のif文を書いてみる
x = 2
if x == 2:
    print("数値は2です。")
if x % 2 == 0:
    print("数値は偶数です。")
if x % 2 != 0:
    print("数値は奇数です。")

"""
    上記の例では、
    最初のif文2つがTrueに評価されるので、そこにあるコードが実行される
    しかし3つ目はFalseと評価されるので、その中のコードは実行されない
"""

# if文のブロック内にif文を書く(「ネストした」、「入れ子の...」)
x = 10
y = 11

if x == 10:
    if y == 11:
        print(x + y)
        
"""
    以下の例では、x + yの結果が画面に出力されるのは2つのif文が両方ともTrueに評価された時
    else文は単独では使えない。else文はif-else文の最後に一度だけ使える決まり。
    
    if-else文に使えるキーワードがもう1つある。
    elif というキーワードを使ってelif文を書くと、「あるいはもし...」という意味になる。
    これはif-else文に別の条件分岐を追加したいときに使う。
    
    if-else文にelif文を含めた場合、最初にif文が評価される。
    もしif文の式がTrueに評価されたら、そのブロックだけ実行する。
    しかしもし、Falseに評価されたら、次に書かれたelif文が順番に評価される。
    elif文に書かれた式がTrueだったら、そのelif文のコードブロックが実行され、それ以降のelif文は評価されない
    もしどのelif文もTrueでなかった場合、else文のコードブロックが実行される。
    
    次のコードは、elif文があるif-else文例です
"""
home = "タイ"
if home == "日本":
    print("Hello,Japan!")
elif home == "タイ":
    print("Hello,Thailand!")
elif home == "インド":
    print("Hello,India!")
elif home == "中国":
    print("Hello,China!")
else:
    print("Hello,World!")
    
# 以下はどの elif文も True に評価されなかった場合の例
home = "火星"
if home == "アメリカ":
    print("Hello,America!")
elif home == "カナダ":
    print("Hello,Canada!")
elif home == "タイ":
    print("Hello,Thailand!")
elif home == "メキシコ":
    print("Hello,Mexico!")
else:
    print("Hello,World!")
    
# 複数のif文、elif文をコードに記述した例
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
