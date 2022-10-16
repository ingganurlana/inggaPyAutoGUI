import pyautogui
import time
# print(pyautogui.size())

time.sleep(5)

print(pyautogui.position())

for i in range(1, 6):
    
    pyautogui.doubleClick()
    pyautogui.hotkey('ctrl', 'a')
    pyautogui.typewrite("change names to "+str(i))

    pyautogui.moveRel(0, 94/2)
    pyautogui.click()

    print(i)

