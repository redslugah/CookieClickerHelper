import pyautogui
import keyboard


def do_quick_save():
    mousestart = pyautogui.position()
    pyautogui.click(x=640, y=50)
    pyautogui.click(x=700, y=370)
    keyboard.press_and_release('ctrl+c')
    pyautogui.click(x=960, y=630)
    pyautogui.click(x=1550, y=150)
    pyautogui.moveTo(mousestart)


def quick_save_start():
    pyautogui.PAUSE = 0.01
    while True:
        keyboard.add_hotkey('F5', do_quick_save)
        keyboard.wait()