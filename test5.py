import time

#回收
import pyautogui
try:
    while True:
        time.sleep(2)
        pyautogui.moveTo(1026, 456, duration=1)
        pyautogui.click()
        pyautogui.moveTo(938, 803, duration=1)
        pyautogui.click()
        pyautogui.moveTo(721, 709, duration=1)
        pyautogui.click()
        pyautogui.moveTo(523, 373, duration=1)
        pyautogui.click()

        time_left = 7200
        while time_left >= 0:
            #print("\r ",'倒计时(s): ', time_left,end="",flush=True)
            print("\r 回收倒计时(s): %d " % (time_left),end="",flush=True)#显示不会有留影
           # print("\r", "倒计时{}秒！".format(time_left), end="", flush=True)
            time.sleep(1)
            time_left = time_left - 1
        # time.sleep(7200)

except KeyboardInterrupt:
    print('\nExit.')
