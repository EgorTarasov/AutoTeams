

import webbrowser
import pyautogui as gui
from time import sleep

URL_AUTH = 'https://login.mos.ru/sps/oauth/ae?scope=openid+profile+blitz_user_rights+snils+contacts+blitz_change_password&access_type=offline&response_type=code&redirect_uri=https://dnevnik.mos.ru/sudir&state=6b0506f5-43fd-41ac-9a43-088375815733&client_id=dnevnik.mos.ru'
lessons = [[1600, 520], [1600, 645], [1600, 770], [1600, 895], [1600, 1020], [1600, 1145]]
size = gui.size()
teams_btn = [1345, 385]


def open_chrome():
    chrome_path = 'open -a /Applications/Google\ Chrome.app %s'
    webbrowser.get(chrome_path).open(URL_AUTH)


def get_click():
    print(gui.position())


def auth():
    sleep(2)
    gui.click([1030, 560])


def enter_lesson():
    sleep(3)
    gui.leftClick(teams_btn)
    sleep(5)
    gui.leftClick(1055, 260)
    sleep(3)
    gui.leftClick(1220, 560)
    sleep(7)

    # camera off
    gui.leftClick(920, 620)
    sleep(0.6)
    # mic off
    gui.leftClick(1015, 620)
    sleep(0.6)

    # entering name
    gui.doubleClick(900, 575)
    gui.write('Tujh Nfhfcjd', interval=0.1)

    # entering meeting
    gui.leftClick(1175, 575)


def main():
    get_click()
    open_chrome()
    #gui.hotkey('control', 'command', 'f')
    sleep(5)
    auth()
    sleep(7)

    '''Accesing first lesson'''
    gui.leftClick(lessons[0])
    enter_lesson()


if __name__ == '__main__':
    main()
