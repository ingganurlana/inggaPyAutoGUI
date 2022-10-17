from unicodedata import name
import pyautogui
import time
nama = ["Object.013",
"Object.014",
"Object.017",
"Object.018",
"Object.019",
"Object.020",
"Object.021",
"Object.022",
"Object.023",
"Object.024",
"Object.025",
"Object.026",
"Object.027",
"Object.028",
"Object.029",
"Object.030",
"Object.032",
"Object.033",
"Object.045",
"Object.051",
"Object.052",
"Object.053",
"Object.079"]

time.sleep(2)

print(pyautogui.position())

#nambah folder
for i, nama in reversed(list(enumerate(nama))):
    pyautogui.moveTo(x=1457, y=172)
    pyautogui.click()
    pyautogui.moveTo(x=1230, y=221)
    pyautogui.doubleClick()
    pyautogui.typewrite(str(i))
    pyautogui.press('enter')
    pyautogui.rightClick()
    pyautogui.moveTo(x=1320, y=38)
    pyautogui.click()
    time.sleep(0.5)