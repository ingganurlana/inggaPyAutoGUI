import time
from urllib.request import ProxyDigestAuthHandler

import pyautogui

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
"Object.046",
"Object.051",
"Object.052",
"Object.053",
"Object.079"]

time.sleep(2)

print(pyautogui.position())

# pyautogui.moveTo(x=1767, y=499) #ke height
 #ke height
# pyautogui.moveTo(x=1767, y=499) #ke normal
# pyautogui.moveTo(x=1767, y=499) #ke metallic

nama.sort(reverse=True)

for i in nama:
    pyautogui.moveTo(1399, 175)
    pyautogui.click()

    pyautogui.moveTo(1208, 216)
    pyautogui.doubleClick()
    pyautogui.typewrite(i)
    pyautogui.press('enter')

    #nambah mask
    pyautogui.rightClick()
    pyautogui.moveTo(x=1320, y=38)
    pyautogui.click()

    #pindah mouse kesini biar muncul slot basecolor dll
    pyautogui.moveTo(x=1114, y=216)
    pyautogui.click()

    pyautogui.moveTo(x=1771, y=310)
    pyautogui.click()

    #import texturenya
    pyautogui.moveTo(x=1697, y=417) #ke basecolor 
    pyautogui.click()
    pyautogui.hotkey('ctrl', 'a')
    pyautogui.press('delete')
    pyautogui.typewrite(i+"_B")
    pyautogui.moveRel(-53, 87, 0.1)
    pyautogui.click()
    pyautogui.moveTo(x=1697, y=882)
    pyautogui.click()

    pyautogui.moveTo(x=1697, y=464) #height
    pyautogui.click()
    pyautogui.hotkey('ctrl', 'a')
    pyautogui.press('delete')
    pyautogui.typewrite(i+"_N")
    pyautogui.moveRel(-53, 87, 0.1)
    pyautogui.click()
    pyautogui.moveTo(x=1575, y=882)
    pyautogui.click()

    pyautogui.moveTo(x=1697, y=525) #roughness
    pyautogui.click()
    pyautogui.hotkey('ctrl', 'a')
    pyautogui.press('delete')

    pyautogui.typewrite(i+"_R")
    pyautogui.moveRel(-53, 87, 0.1)
    pyautogui.click()
    pyautogui.moveTo(x=1575, y=882)
    pyautogui.click()

    pyautogui.moveTo(x=1697, y=569) #normal
    pyautogui.click()
    pyautogui.hotkey('ctrl', 'a')
    pyautogui.press('delete')
    pyautogui.typewrite(i+"_N")
    pyautogui.moveRel(-53, 87, 0.1)
    pyautogui.click()
    pyautogui.moveTo(x=1575, y=882)
    pyautogui.click()

    time.sleep(1)
