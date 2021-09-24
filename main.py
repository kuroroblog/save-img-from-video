# 参考 : https://note.nkmk.me/python-opencv-video-to-still-image/
import cv2
import os

# 動画ファイルパス
videoPath = "./test.mp4"
# 静止画像を取り込むディレクトリ
resultPath = "./img/"

# 静止画像を切り出す時間間隔を設定。
N = 1

# 動画から設定される時間間隔ごとに、静止画像を生成する関数
def saveImgFromVideo():
    # 動画を読み込む。
    cap = cv2.VideoCapture(videoPath)

    # 動画が存在しない場合、後続処理を行わない。
    if not cap.isOpened():
        print('No such file or directory!!')
        return

    # 静止画像を取り込むディレクトリが存在しない場合に、ディレクトリを自動生成する。
    os.makedirs(os.path.dirname(resultPath), exist_ok=True)

    # 動画からフレーム数を取得する。
    videoFrameCount = cap.get(cv2.CAP_PROP_FRAME_COUNT)
    # 動画からフレームレートを取得する。
    # フレームレート : 1秒間あたりに取得できるフレーム数。
    # フレームレートとは? : https://nvr.bz/topics/knowledge/what-framerate.php
    videoFps = cap.get(cv2.CAP_PROP_FPS)
    # 動画の長さ(秒)を計算する。
    videoLenSec = videoFrameCount / videoFps

    # N秒間隔ごとに静止画像を切り出す処理
    cnt = 0
    while videoLenSec > cnt:
        cap.set(cv2.CAP_PROP_POS_FRAMES, round(videoFps * cnt))

        ret, frame = cap.read()

        if ret:
            # 静止画像を保存する。
            # imwriteについて : https://kuroro.blog/python/i0tNE1Mp8aEz8Z7n6Ggg/
            cv2.imwrite(resultPath + str(cnt) + '.jpg', frame)

        cnt += N

saveImgFromVideo()
