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

