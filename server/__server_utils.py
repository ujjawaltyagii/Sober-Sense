import os
import datetime
from __paths import USER_DATA


def save_video(video):
    name = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    video_path = os.path.join(os.getcwd(), USER_DATA, name + '.mp4')
    video.save(video_path)
