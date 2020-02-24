import pyautogui, sys

print("Ctrl-C")
try:
    while True:
        x, y = pyautogui.position()
        positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
        print(positionStr, end='')
        print('\b' * len(positionStr), end='', flush=True)
except KeyboardInterrupt:
    print('\n')
#################################################################
import pyautogui, time 

try:
    while True:
        if pyautogui.mouseDown:
            pyautogui.doubleClick()
            pyautogui.move(960, 0)
            pyautogui.doubleClick()
except KeyboardInterrupt:
    print('\n')
