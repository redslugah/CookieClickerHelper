import pyautogui
import keyboard


def scum():
    pyautogui.click(x=640, y=50)
    pyautogui.click(x=850, y=370)
    keyboard.press_and_release('ctrl+v')
    pyautogui.click(x=920, y=630)


def start_save_scum():
    while True:
        keyboard.add_hotkey('F6', scum)
        keyboard.wait()

