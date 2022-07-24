import pyautogui
import keyboard
import time


def rest(x, y):
    pyautogui.click(x=x, y=y)
    time.sleep(0.1)


def auto_ascend():
    while True:
        rest(x=960, y=130)
        rest(x=940, y=560)
        time.sleep(2)
        rest(x=1810, y=270)
        rest(x=1750, y=170)
        pyautogui.moveTo(x=1420, y=270)
        rest(x=1750, y=320)
        rest(x=1750, y=380)
        rest(x=1750, y=450)
        rest(x=1750, y=510)
        rest(x=1750, y=580)
        rest(x=1750, y=640)
        time.sleep(1)
        rest(x=1750, y=170)
        pyautogui.moveTo(x=1420, y=270)
        rest(x=1750, y=710)
        rest(x=1750, y=770)
        rest(x=1750, y=840)
        rest(x=1750, y=890)
        rest(x=1750, y=950)
        rest(x=1750, y=1020)
        time.sleep(1)
        rest(x=1750, y=170)
        time.sleep(2.5)
        rest(x=1750, y=170)
        pyautogui.moveTo(x=1420, y=270)
        time.sleep(0.2)
        pyautogui.moveTo(x=1750, y=560)
        pyautogui.scroll(-2000)
        time.sleep(0.2)
        rest(x=1750, y=560)
        rest(x=1750, y=620)
        rest(x=1750, y=690)
        rest(x=1750, y=750)
        rest(x=1750, y=820)
        rest(x=1750, y=880)
        pyautogui.scroll(2000)
        time.sleep(2)
        rest(x=1750, y=170)
        pyautogui.moveTo(x=1420, y=270)
        time.sleep(0.2)
        pyautogui.moveTo(x=1750, y=560)
        pyautogui.scroll(-2000)
        time.sleep(0.2)
        rest(x=1750, y=940)
        pyautogui.scroll(2000)
        time.sleep(2)
        rest(x=1750, y=170)
        time.sleep(3)
        rest(x=1750, y=170)
        time.sleep(1)
        rest(x=1540, y=90)
        rest(x=960, y=600)
        time.sleep(0.5)
        keyboard.press_and_release('Escape')
        time.sleep(2)
        if keyboard.is_pressed('F3'):
            time.sleep(0.2)
            break


def ascend():
    while True:
        keyboard.add_hotkey('F4', auto_ascend)
        keyboard.wait()