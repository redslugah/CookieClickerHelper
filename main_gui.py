import PySimpleGUI as Sg
import fast_clicking
import savescum
from multiprocessing import Process


def fast_click():
    fast_clicking.fast_click()


def save_scum():
    savescum.start_save_scum()


def main_window():
    layout = [
        [Sg.Text("Cookie Clicker Helper")],
        [Sg.Button("Ascend [OFF]", size=(20, 0), key="ascend", button_color=('black', 'grey')),
         Sg.Button("Fast click [OFF]", size=(20, 0), key="fast_click", button_color=('black', 'grey')),
         Sg.Button("Savescum [OFF]", size=(20, 0), key="savescum", button_color=('black', 'grey'))],
        [Sg.Button("Sell click combo [OFF]", size=(20, 0), key="click_combo", button_color=('black', 'grey')),
         Sg.Button("Stock market bot [OFF]", size=(20, 0), key="stock_bot", button_color=('black', 'grey')),
         Sg.Button("EXIT", size=(20, 0), key="exit")],
        [Sg.Output(size=(75, 15), key='-OUTPUT-')],
        [Sg.Button("Clear log", size=(20, 0), key="clear_log", button_color=('black', 'grey')),
         Sg.Button("Hotkeys", size=(20, 0), key="hotkeys", button_color=('black', 'grey')),
         Sg.Button("Something", size=(20, 0), key="aaaaaa", button_color=('black', 'grey'))]]
    window = Sg.Window("Cookie Clicker Helper", layout, element_justification='c')
    while True:
        event, values = window.read()
        if event in (Sg.WIN_CLOSED, "exit"):
            break
        elif event == 'fast_click':
            if window[event].get_text() == 'Fast click [OFF]':
                fc = Process(target=fast_click)
                fc.daemon = True
                window[event].Update("Fast click [ON]", button_color=('white', 'green'))
                fc.start()
                print('Fast clicking enabled, press F4 to start fast clicking and press F3 to stop.')
            else:
                fc.kill()
                window[event].Update("Fast click [OFF]", button_color=('black', 'grey'))
                print('Fast clicking disabled.')
        elif event == 'savescum':
            if window[event].get_text() == 'Savescum [OFF]':
                sc = Process(target=save_scum)
                sc.daemon = True
                window[event].Update("Savescum [ON]", button_color=('white', 'green'))
                sc.start()
                print('Savescum enabled, export your save to clipboard and press F6 on the main game for quick import')
            else:
                sc.kill()
                window[event].Update("Savescum [OFF]", button_color=('black', 'grey'))
                print('Savescum disabled.')


if __name__ == '__main__':
    main_window()