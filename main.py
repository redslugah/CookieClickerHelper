import PySimpleGUI as Sg
import pyautogui
import threading
import keyboard


def main_window():
    layout = [
        [Sg.Text("Cookie Clicker Helper")],
        [Sg.Button("Ascend", size=(20, 0), key="ascend"),
         Sg.Button("Fast clicking", size=(20, 0), key="fast"),
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



if __name__ == '__main__':
    main_window()
