from mss import mss
from time import sleep
import numpy as np
from image_seg import is_right
import cv2
from controlls import start_fishing
sleep(1)
with mss() as sct:

    monitor = sct.monitors[1]
    img = np.asarray(sct.grab(monitor))
    start_fishing(is_right(img))
       