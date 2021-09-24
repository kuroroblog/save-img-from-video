# save-img-from-video
動画から設定される時間間隔ごとに、静止画像を生成する

# 各種サービスのversion

| サービス | version |
| ------------- | ------------- |
| Python  | 3.8.8  |

# zipをダウンロードしてから動作確認する
1. https://github.com/kuroroblog/save-img-from-video へアクセスする。
2. 緑色の「Code」と書かれたボタンを選択
3. 「Download ZIP」を選択
4. ダウンロードされたzipファイルをデスクトップへ移動
5. zipファイルをダブルクリック
6. ターミナルを開く。
7. ターミナルを活用して、zipを展開して生成されたフォルダへ移動する。(`$ cd Desktop/save-img-from-video-master`)
8. `$ pip install -r requirements.txt`を実行する。
9. `$ python main.py`を実行する。
10. test.mp4からimgディレクトリ以下へ静止画像ファイルが生成されているのか、確認する。

# 参考文献
- https://note.nkmk.me/python-opencv-video-to-still-image/
- https://note.nkmk.me/python-pip-install-requirements/
