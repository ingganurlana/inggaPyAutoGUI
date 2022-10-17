import pyautogui
import time

time.sleep(5)

fase1 = ["Object.035",
"Object.036",
"Object.037",
"Object.038",
"Object.039",
"Object.040",
"Object.041",
"Object.042",
"Object.057",
"Object.058",
"Object.059",
"Object.060",
"Object.061",
"Object.062",
"Object.063",
"Object.064",
"Object.065",
"Object.066",
"Object.067",
"Object.068",
"Object.069",
"Object.070",
"Object.071",
"Object.072",
"Object.073",
"Object.074",
"Object.075",
"Object.076",
"Object.077",
"Object.078"]

fase2 = ["Object.013",
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

fase3 = ["Object",
"Object.001",
"Object.002",
"Object.003",
"Object.004",
"Object.005",
"Object.006",
"Object.007",
"Object.008",
"Object.009",
"Object.010",
"Object.011",
"Object.012",
"Object.015",
"Object.016",
"Object.031",
"Object.034",
"Object.043",
"Object.044",
"Object.047",
"Object.048",
"Object.049",
"Object.050",
"Object.054",
"Object.055",
"Object.056",
"Object.080",
"Object.081"]


fase1.reverse()
fase2.reverse()
fase3.reverse()

for i in fase3:
    pyautogui.moveTo(x=1759, y=801)
    pyautogui.click()
    pyautogui.press('f1')

    pyautogui.moveTo(x=232, y=392)
    pyautogui.click()
    pyautogui.hotkey('ctrl', 'a')
    pyautogui.typewrite(i)

    pyautogui.moveTo(314, 421,)
    pyautogui.click()
    pyautogui.moveTo(260, 688, 0.5)
    pyautogui.click()
    pyautogui.press('enter')
    pyautogui.moveTo(x=1068, y=312)
    pyautogui.click()

    pyautogui.moveTo(x=779, y=609)
    pyautogui.click()
    pyautogui.press('enter')

    time.sleep(4)

    pyautogui.moveTo(x=1887, y=1020)
    pyautogui.click()
    pyautogui.press('enter')






