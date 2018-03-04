# Pythonチュートリアル  

###### 参考書;Pythonチュートリアル  
###### 発行:オライリージャパン  
###### 第3版  
  
### Python インタープリンタのインストール  
　公式サイト: <https://www.python.org/downloads/> から最新版（Ver.3.6.4[2018/01/21時点]）をダウンロード  
exeファイルを実行し、インストール開始  
#### 1.インストール方法  
　　_Install Now_ では保存場所が分かりづらいので、保存場所を指定できる * Customize installation * を選択  
　　___Add Python 3.6 to PATH___ にチェックを入れる

#### 2.オプション機能
　　_Optional Features_ はとりあえず全てにチェックを入れた。  
　　

#### 3.高度なデバッグ
　　インストール場所は ** C: ** 配下を指定  


インストール終了後 C:** \Python36-32 ** フォルダが作成される。  
C:\Python36-32\python.exeを実行するとPython インタープリンタが起動する  


※PythonのソースファイルはデフォルトでUTF-8でエンコードしてある。  
  
  
  
### 気楽な入門  
#### 1.1Pythonを電卓として利用  
```python
>>> 2 + 2
4
>>> 50 - 5*6
20
>>> (50 - 5*6) / 4
5.0
>>> 8/5
1.6
>>> 2/2
1.0
```
除算(/)は常にfloatを返す。
切り下げ除算を行う場合 //演算子 を使い、剰余のみ得たい場合は %演算子 を使う。  
**演算子を使うことで累乗も可
```python
>>> 17 / 3
5.666666666666667
>>> 17 // 3
5
>>> 17 % 3
2
>>> 5 ** 2
25
```
等号(=)は変数に値を代入するのに使う。  
変数は「定義(値を代入)」されていないまま使おうとするとエラーが出る。  
```python
>>> width = 20
>>> height = 5 * 9
>>> width * height
900

>>> n #未定義の変数
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'n' is not defined
(名前エラー:名前'n'は定義されていない)
```
最後に表示した式は変数「_」で呼び出すことができる
```python
>>> tax = 12.5 / 100
>>> price = 100.80
>>> price * tax
12.6
>>> price + _
113.39999999999999
>>> round(_,2) #四捨五入
113.4
```
[](
複素数もサポート虚部を示す接尾辞「j」または「J」を使用
)

#### 1.2文字列  
引用符にシングルクォート('...')、ダブルクォート("...")使用  
バックスラッシュ(\でも可)でクォート文字のエスケープができる  
```python
>>> 'samp eggs' # シングルクォート
'samp eggs'
>>> 'doesn\'t'
"doesn't"
>>> "doesn't" # ↑のダブルクォート版
"doesn't"
>>> '"Yes," he said.'
'"Yes," he said.'
>>> '\"Yes,\" he said.'
'"Yes," he said.'
```

print関数で出力することも可
```python
>>> '"Isn\'t," she said'
'"Isn\'t," she said'
>>> print('"Isn\'t," she said')
"Isn't," she said
>>> s = 'First line.\nSecond line.' # \nは改行
>>> s # print()を使用しないと\nが出力に含まれる
'First line.\nSecond line.'
>>> print(s) # print()を使うと\nで改行が発生する
First line.
Second line.
```

「\」を設置した文字が特殊文字に解釈されるのが困る場合、  
raw文字列を使う  
[](
raw文字列とは...
)
以下の例は最初の引用符に _r_ を置く
```python
>>> print('C:\some\name')
C:\some
ame
>>> print(r'C:\some\name')
C:\some\name
```

文字列は複数行にわたり書くこともできる。  
その例としてトリプルクォートを使用。
```python
>>> print("""
...     Usage: thingy[OPTIONS]
...      -h             Display this usage message
...      -H             Hostname to connect to
... """)

        Usage: thingy[OPTIONS]
         -h             Display this usage message
         -H             Hostname to connect to

```

文字列は +演算子で連結できるし、*演算子で繰り返すこともできる。  
列挙された文字列リテラル(引用筆囲まれたものたち)は自動的に連結される。  
```python
>>> # unを3回繰り返して最後にiumを付ける
... 3 * 'un' + 'inum'
'unununinum'
>>> 'Py''thon'
'Python'
>>> text = ('カッコの中にながいながい文字列'
...     'これも追加')
>>> text
'カッコの中にながいながい文字列これも追加'
```

但しこれはリテラル同士でのみ有効
```python
>>> prefix = 'Py'
>>> prefix 'thon' # 変数に文字列リテラルを連結
  File "<stdin>", line 1
    prefix 'thon' # 変数に文字列リテラルを連結
                ^
SyntaxError: invalid syntax
(構文エラー:無効な構文)
>>>
>>> # 変数と文字列リテラル連結には + を使う
... prefix + 'thon'
'Python'
```

文字列はインデックス指定(連番による指定)ができる。  
最初のキャラクタのインデックスは0  
```python
>>> word = 'Python'
>>> word = 'Python' # 位置0のキャラクタ
>>> word = 'Python'
>>> word[0] # 位置 0 のキャラクタ
'P'
>>> word[5] # 位置 5 のキャラクタ
'n'
>>> word[-1] # 最後のキャラクタ
'n'
>>> word[-2] # 最後から 2 番目のキャラクタ
'o'
>>> word[6] # 指定文字列オーバー
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: string index out of range
```

スライシング(切取):部分文字列(サブストリング)取得  
始点は常に含まれ、終点は常に除外される  
```python
>>> word[0:2] # 位置 0 から(0含む) 2 まで(2含まず)
'Py'
>>> word[0:] # 位置 0 からすべて表示
'Python'
>>> word[1:] # 位置 1 からすべて表示
'ython'
>>> word[:4] # 最初の文字から位置 4 までの文字
'Pyth'
>>> word[5:2]
''
>>> word[5:-4]
''
>>> word[2:-1]
'tho'
```
  
大きすぎるインデックスを指定するとエラー  
スライシングで指定すると適度に対処  
```python
>>> word[42]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: string index out of range
>>> word[4:42]
'on'
>>> word[42:]
''
```


異なる文字列が必要なときは新しい文字列を生成する必要がある  
ビルドイン関数 len() は文字列の長さを返す  
```python
>>> 'J' +word[1:]
'Jython'
>>> word[:2] + 'py'
'Pypy'
>>> len(word)
6
```



#### 1.3リスト  
文字列同様リストにはインデックスとスライシングが使える  
```python
>>> squares = [1,4,9,16,25]
>>> squares
[1, 4, 9, 16, 25]
>>> squares[0]
1
>>> squares[-1]
25
>>> squares[-3:]
[9, 16, 25]
```

スライシング操作は常に要求された要素を含んだ新たなリストを返す  
[](
変更可能体、変更不可体
)
append()メソッドを使うことでリストの末尾にアイテムを追加できる。  
append()を使用しスライシングへの代入、リストの長さ変更、リストの内容クリアも可能  
```python
>>> # スライシング確認
... squares = [1,4,9,16,25]
>>> squares
[1, 4, 9, 16, 25]
>>> squares[0]
1
>>> squares[-1]
25
>>> squares[-3:]
[9, 16, 25]
>>> squares + [36,49,64,81,100]
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
>>> squares[:] # 元のリスト自体は変更されていない
[1, 4, 9, 16, 25]
>>>
>>> # append()メソッド
... cubes = [1,8,27,65,125] # 1 ～ 5それぞれの3乗
>>> 4 ** 3
64
>>> cubes[3] = 64 # 4 の3乗は64だった、、、入れ替える
>>> cubes
[1, 8, 27, 64, 125]
>>> cubes.append(216) # 6 の3乗追加
>>> cubes.append(7 ** 3) # 7 の3乗追加
>>> cubes
[1, 8, 27, 64, 125, 216, 343]
>>>
>>> letters = ['a','b','c','d','e','f','g']
>>> letters
['a', 'b', 'c', 'd', 'e', 'f', 'g']
>>> # スライシングへの代入
... letters[2:5] = ['C','D','E']
>>> letters
['a', 'b', 'C', 'D', 'E', 'f', 'g']
>>> # 代入された範囲を削除
... letters[2:5] = []
>>> letters
['a', 'b', 'f', 'g']
>>> # リストをクリア。空リストで全部の要素を置換
... letters[:] = []
>>> letters
[]
>>>
>>> letters = ['a','b','c','d']
>>> len(letters) # ビルドイン関数len()
4
```

リストは入れ子にできる(リストを要素とするリストが生成できる)
```python
>>> a = ['a','b','c']
>>> n = [1,2,3]
>>> x = [a,n]
>>> x
[['a', 'b', 'c'], [1, 2, 3]]
>>> x[0]
['a', 'b', 'c']
>>> x[0][1]
'b'
>>> x[1]
[1, 2, 3]
>>> x[1][2]
3
```

#### 2.プログラミング、はじめの一歩
```python
>>> # フィボナッチ級数
... # 2項の和により次項が定まる
... a,b = 0,1
>>> while b < 10:
...     print(b)
...     a,b = b, a+b
...
1
1
2
3
5
8
>>> a,b = 0,1
>>> while b < 10:
... print(b) # 字下げ忘れ
  File "<stdin>", line 2
    print(b)
        ^
IndentationError: expected an indented block
>>> a,b = 0,1
>>> while b < 10:
...     print(b)
... a,b = b, a+b # ブロック内のインデント不揃い
  File "<stdin>", line 3
    a,b = b, a+b
    ^
SyntaxError: invalid syntax
```
a,b = 0,1 多重代入  
変数aとbは、新しい値0と1をそれぞれ得ている。  
a,b = b, a+b も多重代入  
こちらでは代入が行われる前に右辺の式を処理  

whileループは条件(b < 10)が真(true)である限り実行を繰り返す。  
C言語同様0でない整数が真、0が偽となる  
比較演算子も同じ<(小なり)、>(大なり)、==(等しい)、<=(小なりまたは等しい)、>=(大なりまたは等しい)、!=(等しくない)  
条件は文字列やリストでも可  

ループのボディ部分にはインデントがかかっている  
Pythonでは文のグルーピングにインデントを使う  
対話環境ではインデントされた行を入力するにはTabやスペースを入力する必要がある。  
[](
実地ではもっと複雑な入力....実地？
)
また、最後に空白行を加えて文の完了を知らせる必要がある  
ブロック内の行同士はインデントを揃える必要があるのでそこも注意する  

print関数は、与えられた引数(複数可)の値を表示する  
引数(文字列、数値)が複数あるときの扱いは、電卓の例とは異なる  
文字列は引用符なしで表示され、アイテムの間にはスペースが挿入されるため  
キレイにフォーマットされる
```python
>>> i = 256 * 256
>>> print('The value ov i is',i)
The value ov i is 65536
>>> j = 'null'
>>> print('The value ov i is',j)
The value ov i is null
```
キーワード引数endを使えば、出力末尾の改行の抑制や、出力末尾を他の文字列に変更することができる
```python
>>> a,b = 0,1
>>> while b < 1000:
...     print(b,end=',')
...     a,b = b, a+b
...
1,1,2,3,5,8,13,21,34,55,89,144,233,377,610,987,>>>
```



### 制御構造ツール  
#### 1.if文  
```python
>>> x = int(input("整数を入れてください:"))
整数を入れてください:42
>>> if x < 0:
...     x = 0
...     print('負数はゼロとする')
... elif x == 0:
...     print('ゼロ')
... elif x == 1:
...     print('ひとつ')
... else:
...     print('もっと')
...
もっと
```

elifはもっと続けてもよいし、無くてもよい。  
「else if」の短縮で、インデントだらけになるのを防ぐ。  
else部分はオプション  
[](
オプション？
)


#### 2.for文  
Cのfor文とは少し異なる  
反復間隔と停止条件を定義させること無くあらゆるシーケンス(リストや文字列)のアイテムに対し、  
そのシーケンス内の順序で反復をかける  
```python
>>> # 文字列の長さを測る
... words = ['cat','window','defenestrate']
>>> for w in words:
...     print(w,len(w))
...
cat 3
window 6
defenestrate 12
```
反復中のシーケンスを改変する必要があるときは、コピーを取って反復をかけることを推奨  
シーケンスに反復をかけることで暗黙にコピーが取られたりはしない  
```python
>>> for w in words[:]: # リスト全体のスライスコピーにループをかける
...     if len(w) > 6:
...             words.insert(0,w)
...
>>> words
['defenestrate', 'cat', 'window', 'defenestrate']
```
スライスコピー・・・範囲指定後部分リスト取得



#### 3.range()関数  
数字の連なりに反復をかけるときは、ビルドイン関数のrange()が便利  
ビルドイン関数・・・基本的、汎用的な演算処理を行うためにあらかじめ用意されている関数のこと
```python
>>> for i in range(5):
...     print(i)
...
0
1
2
3
4
```

与えられた終端値は入らない、  
range(XX)が生成するXX個の値は、長さXXのシーケンスの各アイテムへのインデックスとなる  
rangeは0以外の数字から始めることも、増分の指定(負数)も可  
```python
>>> for i in range(5,9): #5～9まで
...     print(i)
...
5
6
7
8
>>> for i in range( 0,10, 3): #0～10まで、増分3
...     print(i)
...
0
3
6
9
>>> for i in range(-10,-100, -30): #-10～-100まで、増分-30
...     print(i)
...
-10
-40
```
シーケンスのインデックスで反復をかけたいときは、
range()、len()を組み合わせる
```python
>>> a = ['Mary','had','a','little','lamb']
>>> for i in range(len(a)):
...     print(i,a[i])
...
0 Mary
1 had
2 a
3 little
4 lamb
```


多くの場合enumerate()関数を使用している(6 ループのテクニック参照)  
rangeを単純にprintしてやると、
```python
>>> print(range(10))
range(0, 10)
```
range()関数が返すオブジェクトはリストのように振舞っているが、  
** 実はlistではない **  
反復を掛けることで望みのシーケンスのアイテムを連続的に返すオブジェクトであり、  
本当にはリストを作らず、それにより空間を節約する  
このようなオブジェクトを ** 反復可能体(iterable) ** と呼ぶ  
これは空になるまで連続的にアイテムを供給するもの、そうしたものを期待する関数や構造のターゲットとして適したもの  
反復可能体を期待する関数や構造を ** 反復子(iterator) ** という  
for文は反復子の例である  
反復可能体からリストを生成するlist()関数も反復子  
```python
>>> list(range(5))
[0, 1, 2, 3, 4]
```
反復可能体を返す関数や、引数として取る関数は他にも存在するので後記で触れる  


#### 4.break文とcontinue文、ループにおけるelse節
break文はC同様、forまたはwhileのループを抜けるもの  
ループ文にはelse節を加えられる  
else節は、リストを使い果たしたり(for)、条件式がfalseになること(while)によってループが終了した場合に実行され、  
break文で終了した場合には実行されない  
以下素数探索ループによる例
```python
>>> for n in range(2,10):
...     for x in range(2,n):
...             if n % x == 0:
...                     print(n,'equals',x,'*',n//x)
...                     break
...     else:
...             # ループで約数が見つけられなかった場合
...             print(n,'is a prime number')
...paa
2 is a prime number
3 is a prime number
4 equals 2 * 2
5 is a prime number
6 equals 2 * 3
7 is a prime number
8 equals 2 * 4
9 equals 3 * 3
```
この例で注目すべきは * else節の所属がif文ではなくforループとなっている所 *  
ループでのelse節は、try文に似たものになる  
try文のelse節は例外が起きなかったときに、  
ループのelse節はbreakが起きなかったときに実行される  
try文や例外の詳細は後記の「例外の処理」参照  
continue文もC同様でループの残りを飛ばして次の反復に移る  
```python
>>> for num in range(2,10):
...     if num % 2 == 0:
...             print("Found an even number",num)
...             continue
...     print("Found a number", num)
...
Found an even number 2
Found a number 3
Found an even number 4
Found a number 5
Found an even number 6
Found a number 7
Found an even number 8
Found a number 9
```



#### 5.pass文  
pass文は何もしない  
構文的に文が必要なのに、プログラム的には何もする必要がないときに使う  
```python
>>> while True:
...     pass #キーボード割込(Ctrl+C)を待つ
...
KeyboardInterrupt
```
passの使いどころとしては、新しくコードを書いているとき関数や条件の本体に一時的に保存しておき(プレースホルダ)、  
実装を後回しにするときに使う  
```python
>>> def initlog(*args):
...     pass # 実装を忘れずに！
...
```

