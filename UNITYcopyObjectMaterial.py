import pyautogui, time

namamaterial = ["Object.001",
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
"Object.013",
"Object.014",
"Object.015",
"Object.016",
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
"Object.031",
"Object",
"Object.032",
"Object.033",
"Object.034",
"Object.035",
"Object.036",
"Object.037",
"Object.038",
"Object.039",
"Object.040",
"Object.041",
"Object.042",
"Object.043",
"Object.044",
"Object.045",
"Object.046",
"Object.047",
"Object.048",
"Object.049",
"Object.050",
"Object.051",
"Object.052",
"Object.053",
"Object.054",
"Object.055",
"Object.056",
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
"Object.078",
"Object.079",
"Object.080",
"Object.081"]

time.sleep(5)
namamaterial = sorted(namamaterial)

namamaterial.reverse()
for i in namamaterial:
    
    pyautogui.moveTo(x=288, y=694)
    pyautogui.click()
    pyautogui.hotkey('ctrl', 'c')
    pyautogui.hotkey('ctrl', 'v')
    pyautogui.click()
    pyautogui.press('f2')
    pyautogui.typewrite(i)
    time.sleep(1)
    pyautogui.press('\nObject.080')


    pyautogui.moveTo(x=1888, y=461)
    pyautogui.click()
    pyautogui.typewrite(i)
    time.sleep(3)

    pyautogui.moveTo(x=1395, y=398)
    pyautogui.doubleClick()

    pyautogui.moveTo(x=1856, y=176)
    pyautogui.click()

    time.sleep(2)

