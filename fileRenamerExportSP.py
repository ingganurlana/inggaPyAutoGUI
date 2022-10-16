import pyautogui
import time

myList = ["Cube",
"Light",
"Camera",
"Icosphere",
"Icosphere.001",
"Cone",
"Sphere",
"Cone.001"]

myList = sorted(myList)

time.sleep(5)

pyautogui.press('f2')

try:
    for i in myList:
        pyautogui.typewrite(i+"_B.png")
        pyautogui.press('tab')
except:
    print("ada yg salah mas")

pyautogui.alert('done', 'GOKIL BRO!!!', 'OK')