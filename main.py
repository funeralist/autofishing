import cv2 as cv
import mss
import pyautogui
import time
import numpy
import keyboard

def hold_e():
    pyautogui.keyDown('e')
    time.sleep(0.6)
    pyautogui.keyUp('e')

def press_e():
    pyautogui.keyDown('e')
    time.sleep(0.03)
    pyautogui.keyUp('e')

image = None
activity_state = False
capture = {"top": 710, "left": 805, "width": 335, "height": 55}

with mss.mss() as sct:
    while True:
        if keyboard.is_pressed('ctrl') and keyboard.is_pressed('shift') and keyboard.is_pressed('l'):
            activity_state ^= True
            time.sleep(0.7)
            print('state changed to ' + str(activity_state))

        if activity_state:
            image = numpy.asarray(sct.grab(capture))
            hsv_image = cv.cvtColor(image, cv.COLOR_BGR2HSV)

            lower_color = numpy.array([0, 0, 255])
            upper_color = numpy.array([255, 0, 255])
            mask = cv.inRange(hsv_image, lower_color, upper_color)

            has_color = numpy.sum(mask)

            if has_color > 0:
                print('color detected')
                hold_e()
            else:
                print('color NOT detected')
