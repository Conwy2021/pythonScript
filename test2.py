import time

import pyautogui
#挂地图
# sizex,sizey=pyautogui.size()
# pyautogui.moveTo(sizex/2,sizey/2,duration=1)#duration 为过渡时间
# pyautogui.click(button='right')
# pyautogui.moveRel(100, -200, duration=0.5) 相对位置移动
try:
    while True:
        time.sleep(2)
        pyautogui.click(1040, 456, duration=1)  # interval 点击间隔
        pyautogui.moveRel(-183, 0, duration=1)
        pyautogui.doubleClick()
        pyautogui.moveRel(-214, 164, duration=1)
        pyautogui.click()
        pyautogui.moveRel(378, -177, duration=1)
        pyautogui.click()
        pyautogui.click(975, 521, duration=1)
        time_left = 7200
        while time_left >= 0:
            print("\r 挂地图倒计时(s): %d " % (time_left), end="", flush=True)  # 显示不会有留影
            time.sleep(1)
            time_left = time_left - 1
        #time.sleep(7200)
except KeyboardInterrupt:
    print('\nExit.')
