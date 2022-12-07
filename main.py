from mss import mss
from time import sleep

# The simplest use, save a screen shot of the 1st monitor
with mss() as sct:
    sleep(4)
    sct.shot(output=f'test.png')