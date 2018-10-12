# 他ファイルから必要な部分参照の為の宣言
from django.db import models
from django.utils import timezone

# モデルを定義
"""
    class -> オブジェクトを定義するという宣言
    Post -> モデルの名前(特殊文字、空白は避ける)。クラス名は大文字で始まる。
    models.Model -> 渡し先が Django Model であることを意味
    
    author,title,text,created_date,published_date -> プロパティの定義
    
    フィールドタイプ(テキスト?数字?日付?他のオブジェクトとの関係性は?...など)の指定
        models.ForeignKey => 他のモデルへのリンク
        models.CharField => テキスト数を定義
        models.TextField => 制限なしの長いテキスト用
        models.DateTimeField => 日付と時間のフィールド
 
    def publish(self): -> ブログを公開するメソッドそのもの
        def => ファンクション(関数)/メソッド
        publish => このメソッドの名前(英小文字もしくはアンダースコアのみ使用可能)
        
    
    メソッドは通常何かを return する 
    return self.title では表題のテキスト(string)が返ってくる
    
    
    定義等で細かな所が気になったら↓参照(Djangドキュメント)
    https://docs.djangoproject.com/ja/2.1/ref/models/fields/#field-types
    
"""
class Post(models.Model):
    # author = models.ForeignKey('postgres')
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    # __"ダンダー(ダブルアンダースコア)"
    def __str__(self):
        return self.title
