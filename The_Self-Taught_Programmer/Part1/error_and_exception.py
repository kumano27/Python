# -*- coding: utf-8 -*-

"""
    エラーと例外
    
    Pythonプログラムを書いているときにPython構文に従わないと、
    プログラム実行時にエラーが発生する。
    この時プログラムが動作しなかったことと、どんなエラーが起きたのかを、Pythonのシェルが表示してくれる
    試しに、文字列rテラルのクォートを片方つけ忘れたときにどんなエラーが表示されるか見てみる
"""
my_string = "Hello World.

"""
    表示エラー文 
   
  File "C:/work/Python/The_Self-Taught_Programmer/Part1/error_and_exception.py", line 11
    my_string = "Hello World.
                             ^
  SyntaxError: EOL while scanning string literal
  
  
  このメッセージは、プログラム中に構文エラー(SyntaxError)があることを伝えている
  構文エラーは致命的。構文エラーがあるままではプログラムを実行できない。
  構文エラーがあるプログラムを実行すると、Pythonはエラーがあることを教えてくれる。
  メッセージには、どのファイルのどの行に問題があるか、そしてそれはどんなエラーなのかが書かれている。
  
  プログラムにエラーがあったら、エラーメッセージに表示されたファイルの行番号を確認して、
  そこで何を間違えたのか確認する。
  
  今回の例だと11行目に移動する。
  クォートが片方しかないことに気付く。
  文字列の最後にクォートを追加する。
  再度プログラムを実行し、修正できたかを確認する。
  
"""

"""
    エラーの読み方
    
    SyntaxError: EOL while scanning string literal
    
    上記は分かりやすいようにエラーメッセージの最後の行のみ記述
    
    Pythonには2種類エラーがある。構文エラー(Syntax Error)と例外(Exception)。
    構文エラーでないエラーはすべて例外
    例えばZeroDivisionErrorは、ゼロで割り算したときに発生する例外
    
    構文エラーと違って、例外は致命的ではない。
    例外が起こることを想定してプログラムを書いていれば、例外が起きてもプログラムを実行し続けられる。
    
    例外が発生すると、「Pyhtonが例外を投げた」「プログラムが例外を起こした」などと言う
    以下のコードはゼロで割り算する例
    
"""
10 / 0
# >> ZeroDivisionError: division by zero

# コードのインデントを間違えると、IndentationError が発生する
y = 2
    x = 1
# >> IndentationError: unexpected indent