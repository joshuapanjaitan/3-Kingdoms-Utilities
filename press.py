from pynput.keyboard import Key, Controller
import time

keyboard = Controller()
i = 3000
for _ in range(i):
    time.sleep(800)
    keyboard.press('a')
    keyboard.release('a')
