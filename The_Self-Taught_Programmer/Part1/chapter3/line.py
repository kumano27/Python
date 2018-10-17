# -*- coding: utf-8 -*-

"""
    行
    
    Pythonのプログラムは行単位で解釈される
"""

# line1
# line2
# line3

"""
    上記は実質3行のコード(line1,line2,line3)
    各行には行番号があり、エディタを利用する時に行番号を活用できる
    
    IDLE(Python用統合開発環境)では、
    メニュー>Edit>Go to Line を選び表示したい行番号を入力するとその行にカーソルが移動する
    
    IDLEの対話シェルには一度に1行ずつプログラムを入力する事。
    ペースト機能で一度に複数行を貼り付けても、2行目以降は無視されてしまい、
    期待した動作にならない
    
    コードが長くなって複数行になってしまったら、
    三重クォート(”””)で囲んだり、丸括弧(())、波括弧({})、角括弧([])、で囲めば、
    改行して複数行で書くことも出来る
"""

print("""これは、とても、とても、
      とても、とても長い複数行の
      コードです。""")
# 以下の例のように、行末にバックスラッシュ(\)を使うことで、次の行に続きを書くこともできます。
print\
("""これは、とても、とても、とても、とても
長い複数行のコードです。""")