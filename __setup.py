import os
from __paths import USER_DATA, TRAINING_DATA, TMP_PIECES, PIECES_DRUNK, PIECES_SOBER


def setup():
    dirs = [USER_DATA, TRAINING_DATA, TMP_PIECES, PIECES_DRUNK, PIECES_SOBER]

    for dir in dirs:
        if not os.path.exists(dir):
            os.makedirs(dir)
