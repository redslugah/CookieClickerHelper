import PySimpleGUI as Sg
import pyautogui
import threading
import keyboard


def fast_click():
    t = threading.current_thread()
    pyautogui.PAUSE = 0.01
    while getattr(t, "do_run", True):
        def clicky():
            while True:
                pyautogui.click()
                if keyboard.is_pressed('F3'):
                    break
        keyboard.add_hotkey('F4', clicky)
        keyboard.wait()


def main_window():
    layout = [
        [Sg.Text("Cookie Clicker Helper")],
        [Sg.Button("Ascend", size=(20, 0), key="ascend"),
         Sg.Button("Fast click [OFF]", size=(20, 0), key="fastclick"),
         Sg.Button("Savescum", size=(20, 0), key="savescum")],
        [Sg.Button("Sell click combo", size=(20, 0), key="clickcombo"),
         Sg.Button("Stock market bot", size=(20, 0), key="stockBot"),
         Sg.Button("EXIT", size=(20, 0), key="exit")],
        [Sg.Output(size=(75, 15), key='-OUTPUT-')]]
    window = Sg.Window("Cookie Clicker Helper", layout, element_justification='c')

    while True:
        event, values = window.read()
        if event in (Sg.WIN_CLOSED, "exit"):
            break
        elif event == 'fastclick':
            if window[event].get_text() == 'Fast click [OFF]':
                window[event].Update("Fast click [ON]", button_color=('white', 'green'))
                t = threading.Thread(target=fast_click)
                t.start()
            else:
                t.do_run = False
                t.join()
                window[event].Update("Fast click [OFF]", button_color=('white', 'blue'))


if __name__ == '__main__':
    main_window()
