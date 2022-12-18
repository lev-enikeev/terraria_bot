import pyautogui
import time
W, H = pyautogui.size()
x, y = pyautogui.position()

def start_fishing(right):
    if right:
        pyautogui.moveTo(W//2+100, H//2)
    else:
        pyautogui.moveTo(W//2-100, H//2)
    pyautogui.mouseDown()
    time.sleep(0.2)
    pyautogui.mouseUp()
