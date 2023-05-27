import cv2 as cv
import mss
import pyautogui
import time
import numpy
import keyboard
import config


def hold_e():
    pyautogui.keyDown(config.interaction_key)
    time.sleep(0.6)
    pyautogui.keyUp(config.interaction_key)


image = None
activity_state = False

print('Macro launched!')

with mss.mss() as sct:
    while True:
        # check for the hotkey
        if keyboard.is_pressed(config.hotkey):
            activity_state ^= True
            print('Macro is ' + (not activity_state) * 'not ' + 'working!')
            time.sleep(0.7)

        # if hotkey was pressed
        if activity_state:
            # get screenshot and convert to HSV color format
            image = numpy.asarray(sct.grab(config.capture))
            hsv_image = cv.cvtColor(image, cv.COLOR_BGR2HSV)

            # get white pixels
            lower_white = numpy.array([0, 0, 255])
            upper_white = numpy.array([255, 0, 255])
            mask = cv.inRange(hsv_image, lower_white, upper_white)

            # check for white pixels
            has_color = numpy.sum(mask)
            if has_color > 0:
                hold_e()
