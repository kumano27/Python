# -*- coding: utf-8 -*-

"""
    関数を再利用する
    
    関数は、値の計算を行って戻り値を戻すだけではない。
    関数は再利用したい機能をまとめておける
"""

def even_odd(x):
    if x % 2 == 0:
        print("偶数")
    else:
        print("奇数")
even_odd(2)
even_odd(3)

"""
    上記のコード例では、関数の戻り値を定義していないが、機能する。
    x % 2 == 0 でxの値をテストし、xが偶数(even)か奇数(odd)かを出力する
    
    関数を使用すると、より少ないコードを書くだけで済む。
    以下のコードは関数なしで記述されたプログラム例

    このプログラムでは、ユーザーに数値チェックを3回入力するように求めている。
    次に、if-else文で数値が偶数かどうかをチェック、偶数であればn is even.を出力、そうでなければn is odd.を出力する
    
    このプログラムの問題は、同じコードを3回繰り返していること。
"""

n = input("type a number:")
n = int(n)
if n % 2 == 0:
    print("n is even.")
else:
    print("n is odd.")
    
n = input("type a number:")
n = int(n)
if n % 2 == 0:
    print("n is even.")
else:
    print("n is odd.")

n = input("type a number:")
n = int(n)
if n % 2 == 0:
    print("n is even.")
else:
    print("n is odd.")

"""
    上記を機能ごとに関数にまとめ、それを3回呼び出すことで、
    プログラムが短く、かつ読みやすくなるようにする
"""
def even_odd():
    n = input("type a number:")
    n = int(n)
    if n % 2 == 0:
        print("n is even.")
    else:
        print("n is odd.")

even_odd()
even_odd()
even_odd()