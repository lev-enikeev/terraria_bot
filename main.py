from mss import mss
from time import sleep
import numpy as np
from image_seg import is_right
import cv2

i = 0 
with mss() as sct:
    while i < 20:
        monitor = sct.monitors[1]
        img = np.asarray(sct.grab(monitor))
        if is_right(img):
            print('СПРАВА')
        else:
            print('СЛЕВА')
        i += 1       