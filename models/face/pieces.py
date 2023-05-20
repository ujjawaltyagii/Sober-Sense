import shutil
import os
from __paths import TMP_PIECES, PIECES_DRUNK, PIECES_SOBER


def pieces():
    os.makedirs(TMP_PIECES, exist_ok=True)
    os.makedirs(PIECES_DRUNK, exist_ok=True)
    os.makedirs(PIECES_SOBER, exist_ok=True)

    for filename in os.listdir(TMP_PIECES):
        if filename.endswith('.jpg'):
            number = int(filename.replace('piece', '').replace('.jpg', ''))

            if number % 2 == 0:
                shutil.move(os.path.join(TMP_PIECES, filename),
                            os.path.join(PIECES_SOBER, filename))
            else:
                shutil.move(os.path.join(TMP_PIECES, filename),
                            os.path.join(PIECES_DRUNK, filename))
