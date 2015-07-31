BrowserPrinter
=========

description
---------------------------
任意のページからリンクをたどって、すべてのページのスクリーンショットを取得します。



依存パッケージ
---------
以下の3つのライブラリを使用しているのでインストール
```
pip install beautifulsoup4
pip install selenium
pip install requests
```

conf.py
--------------------
top_page  
リンクをたどるトップページ。このページからリンクをたどれるページのスクリーンショットを取得します。

includes  
スクリーンショットを取るページ  
http://www.yahoo.co.jp とした場合、http://www.yahoo.co.jp で始まるURLをすべてスクリーンショットを取る。

excludes  
スクリーンショットの対象外にするページ  
http://docs.yahoo.co.jp/info とした場合、 http://docs.yahoo.co.jp/info から始まるURLのページのスクリーンショットは取得しない。

dest_dir  
スクリーンショットを保存するディレクトリ名

driver  
スクリーンショットを取るのに使用するブラウザ。Firefox、Chrome、Ie、Operaが使用できる。

