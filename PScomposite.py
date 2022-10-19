import pyautogui as p
import time

time.sleep(2)


for i in range(1, 4):
    try:
        buttonLayer = p.locateOnScreen('BTN_Group'+str(i)+'.png')
        p.moveTo(buttonLayer)
        p.click()

        p.hotkey('ctrl','.')
        p.press('enter')

        buttonMask = p.locateOnScreen('PSmaskButton.png')
        p.moveTo(buttonMask)
        p.click()
    except:
        print("skipped")

buttonGroupOpen = p.locateOnScreen('BTN_GroupOpen.png')
p.moveTo(buttonGroupOpen)
p.keyDown('ctrl')
p.click()
p.keyUp('ctrl')

namabutton = ["BTN_UVSelect.png","BTN_Roughness.png", "BTN_Normal.png"]


for nomer, namabtn in enumerate(namabutton): 
    for i in range(1, 4+1):
        ButtonIni = p.locateOnScreen(namabtn)
        p.moveTo(ButtonIni)
        p.click()
        p.press('delete')
        p.scroll(-500)

    #saving
    p.press('f1')

    p.moveTo(x=232, y=392)
    p.click()
    p.hotkey('ctrl', 'a')
    p.typewrite(str(nomer))

    p.moveTo(314, 421,)
    p.click()
    p.moveTo(260, 688, 0.5)
    p.click()
    p.press('enter')
    p.moveTo(x=1068, y=312)
    p.click()

    p.moveTo(x=779, y=609)
    p.click()
    p.press('enter')

    p.moveTo(buttonGroupOpen)

    p.scroll(500)
    time.sleep(3)




