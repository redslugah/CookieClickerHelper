import pyautogui
import keyboard
import time


def do_combo():
    keyboard.press('F3')
    time.sleep(0.3)
    keyboard.release('F3')
    pyautogui.click(x=1630, y=355)
    pyautogui.click(x=1870, y=350)

    pyautogui.click(x=1750, y=400)
    pyautogui.click(x=1750, y=460)
    pyautogui.click(x=1750, y=530)
    pyautogui.click(x=1750, y=590)
    pyautogui.click(x=1750, y=650)
    pyautogui.click(x=1750, y=720)

    pyautogui.click(x=1630, y=340)
    pyautogui.click(x=1810, y=350)

    for i in range(6):
        pyautogui.click(x=1750, y=400)
        pyautogui.click(x=1750, y=460)
        pyautogui.click(x=1750, y=530)
        pyautogui.click(x=1750, y=590)
        pyautogui.click(x=1750, y=650)
        pyautogui.click(x=1750, y=720)

    pyautogui.moveTo(x=290, y=420)
    keyboard.press_and_release('F4')


def do_combo2():
    keyboard.press('F3')
    time.sleep(0.3)
    keyboard.release('F3')
    pyautogui.click(x=1630, y=280)
    pyautogui.click(x=1870, y=273)

    pyautogui.click(x=1750, y=320)
    pyautogui.click(x=1750, y=380)
    pyautogui.click(x=1750, y=440)
    pyautogui.click(x=1750, y=510)
    pyautogui.click(x=1750, y=580)
    pyautogui.click(x=1750, y=640)

    pyautogui.click(x=1630, y=265)
    pyautogui.click(x=1810, y=270)

    for i in range(6):
        pyautogui.click(x=1750, y=320)
        pyautogui.click(x=1750, y=380)
        pyautogui.click(x=1750, y=440)
        pyautogui.click(x=1750, y=510)
        pyautogui.click(x=1750, y=580)
        pyautogui.click(x=1750, y=640)

    pyautogui.moveTo(x=290, y=420)
    keyboard.press_and_release('F4')

def start():
    pyautogui.PAUSE = 0.01
    while True:
        keyboard.add_hotkey('F7', do_combo2)
        keyboard.wait()
