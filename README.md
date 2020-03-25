# AtCoder
AtCoderの問題で書いたコードをあげていきます。

言語はPython。


2020/02/23
ファイルの命名規則を変更。

フォルダ名：コンテスト名

ファイル名：問題のタイトルではなく問題難易度にする。

        　例：ABC156\Rally.py → ABC156\C.py

2020/03/25
AtCoder Unit Test導入に伴いテストコードファイルも用意する。

例：
ABC156\C.py のテストファイル
ABC156\test_C.py

いちいち手動でファイルを作るのがめんどくさくなったので
コードファイルとテストコードファイルを自動作成する
directory_skeleton_generator.pyを作成した
