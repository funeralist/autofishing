import multiprocessing
import pyautogui
import keyboard
import numpy
import time
import mss
import cv2

import config

is_start_of_fishing = False
image = None
macro_state = False


def hold_button():
    pyautogui.keyDown(config.interaction_key)
    time.sleep(config)
    pyautogui.keyUp(config.interaction_key)


def hotkey_check():
    global macro_state
    global is_start_of_fishing

    while True:
        if keyboard.is_pressed(config.hotkey):
            macro_state ^= True
            if macro_state:
                is_start_of_fishing = True
            print('Macro is ' + (not macro_state) * 'not ' + 'working.')
            time.sleep(0.7)


def color_check():
    global image

    with mss.mss() as sct:
        while True:
            if macro_state:
                image = numpy.asarray(sct.grab(config.capture))
                hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

                lower_white = numpy.array([0, 0, 255])
                upper_white = numpy.array([255, 0, 255])
                mask = cv2.inRange(hsv_image, lower_white, upper_white)

                has_color = numpy.sum(mask)
                if has_color > 0:
                    if not is_start_of_fishing:
                        time.sleep(config.catch_delay)
                    hold_button()
                    is_start_of_fishing ^= True


def main():
    hotkey_checker = multiprocessing.Process(name='hotkey_checker', target=hotkey_check)
    color_checker = multiprocessing.Process(name='color_checker', target=color_check)
    
    color_checker.start()
    hotkey_checker.start()


if __name__ == "__main__":
    main()
