import pyautogui
import time
import PIL
time.sleep(5)

W, H = pyautogui.size()
x, y = pyautogui.position()
pyautogui.moveTo(W/2-100, H/2)
pyautogui.click()
pyautogui.click()
pyautogui.click()