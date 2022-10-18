import pyautogui as p
import time

time.sleep(5)


for i in range(67):
    p.moveTo(x=702, y=636)
    p.click()

    p.press('down')


    p.moveTo(x=1723, y=630)
    p.click()
    p.moveTo(1708, 804, 0.5)
    p.click()
    p.moveTo(x=1892, y=747)
    p.click()

    time.sleep(2)