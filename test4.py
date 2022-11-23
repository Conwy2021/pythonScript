import time

#分解
import pyautogui
try:
    while True:
        time.sleep(2)
        # pyautogui.click(896, 586, duration=1)  # interval 点击间隔
        # pyautogui.click(889, 491, duration=1)
        # pyautogui.click(694, 390, duration=1)
        # pyautogui.click(712, 749, duration=1)
        # pyautogui.click(888, 353, duration=1)
        pyautogui.moveTo(896, 586, duration=1)
        pyautogui.click()
        pyautogui.moveTo(889, 491, duration=1)
        pyautogui.click()
        pyautogui.moveTo(694, 390, duration=1)
        pyautogui.click()
        pyautogui.moveTo(712, 749, duration=1)
        pyautogui.click()
        pyautogui.moveTo(888, 353, duration=1)
        pyautogui.click()
        time_left = 7200
        while time_left >= 0:
            #print("\r ",'倒计时(s): ', time_left,end="",flush=True)
            print("\r 倒计时(s): %d " % (time_left),end="",flush=True)#显示不会有留影
           # print("\r", "倒计时{}秒！".format(time_left), end="", flush=True)
            time.sleep(1)
            time_left = time_left - 1
        # time.sleep(7200)

except KeyboardInterrupt:
    print('\nExit.')
