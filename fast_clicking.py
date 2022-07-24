import pyautogui
import keyboard
import time


def clicky():
    while True:
        pyautogui.click()
        if keyboard.is_pressed('F3'):
            time.sleep(0.2)
            break


def fast_click():
    pyautogui.PAUSE = 0.01
    while True:
        keyboard.add_hotkey('F4', clicky)
        keyboard.wait()


if __name__ == '__main__':
    fast_click()