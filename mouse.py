

import webbrowser
import pyautogui as gui
from time import sleep

URL_AUTH = 'https://login.mos.ru/sps/oauth/ae?scope=openid+profile+blitz_user_rights+snils+contacts+blitz_change_password&access_type=offline&response_type=code&redirect_uri=https://dnevnik.mos.ru/sudir&state=6b0506f5-43fd-41ac-9a43-088375815733&client_id=dnevnik.mos.ru'
lessons = [[1550, 590], [1600, 715], [1550, 715], [1550, 965], [1550, 1090], [1550, 1145]]
size = gui.size()
teams_btn = [1315, 465]
teams_cancel_btn = [1145, 340]
teams_continue_btn = [1295, 725]
mic_btn = [990, 930]
webcam_btn = [890, 930]
name_textfield = [900, 875]
teams_join_btn = [1125, 875]


def open_chrome():
    chrome_path = '/usr/bin/google-chrome %s'
    webbrowser.get(chrome_path).open(URL_AUTH)


def get_click():
    print(gui.position())


def auth():
    sleep(7)
    gui.click([990, 630])


def enter_lesson():
    sleep(1)
    gui.leftClick(teams_btn)
    sleep(1)
    gui.leftClick(teams_cancel_btn)
    sleep(1)
    gui.leftClick(teams_continue_btn)
    sleep(7)

    # camera off
    gui.leftClick(webcam_btn)
    sleep(0.6)
    # mic off
    gui.leftClick(mic_btn)
    sleep(0.6)

    # entering name
    '''
    gui.doubleClick(name_textfield)
    gui.hotkey('control', 'a')
    gui.press('backspace')
    gui.hotkey('win', 'space')
    gui.write('Name Surname', interval=0.1)
    '''

    # entering meeting
    gui.leftClick(teams_join_btn)


def main():
    # TODO: Поздороваться и вырубить микро
    # TODO: Сервер с записями голосов
    # TODO:
    get_click()
    open_chrome()
    sleep(7)

    '''Accesing first lesson'''
    gui.leftClick(lessons[0])
    enter_lesson()


if __name__ == '__main__':
    #gui.moveTo(teams_btn)
    main()
    #get_click()
