# D2Autofishing
![image](https://github.com/2taken/D2Autofishing/blob/main/banner.png)

## Requirements
```
pip install opencv-python
pip install pyautogui
pip install mss
pip install keyboard
pip install pywin32
```

## How it works:
It takes some screenshots of area that is determined in config, masks out white color, sums the masked image, if sum is higher than 0 there is a text on the screen (it works because pure white color only appears as a text). If there is a text it holds interaction button determined in config. Also listens to toggle hotkey in separate process.

