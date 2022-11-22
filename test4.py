import time


import pyautogui
try:
    while True:
        time.sleep(2)
        pyautogui.click(896, 586, duration=1)  # interval 点击间隔
        pyautogui.click(889, 491, duration=1)
        pyautogui.click(694, 390, duration=1)
        pyautogui.click(712, 749, duration=1)
        pyautogui.click(888, 353, duration=1)
        time.sleep(7200)
except KeyboardInterrupt:
    print('\nExit.')
