import pyautogui
import time

myList = [
"Object.073",
"Object.074",
"Object.075",
"Object.076",
"Object.077",
"Object.078"]

myList = sorted(myList)

time.sleep(5)

pyautogui.press('f2')

for i in myList:
    print(i)
    pyautogui.typewrite(i+"_R")
    pyautogui.press('tab')
    pyautogui.typewrite(i+"_N")
    pyautogui.press('tab')
    pyautogui.typewrite(i+"_B")
    pyautogui.press('tab')

    time.sleep(1)

pyautogui.alert('done', 'GOKIL BRO!!!', 'OK')