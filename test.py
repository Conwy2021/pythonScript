import pyautogui
try:# 记录位置
    while True:
        x, y = pyautogui.position()
        print(x,y)
except KeyboardInterrupt:
    print('\nExit.')