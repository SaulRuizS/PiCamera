from picamera import PiCamera
from time import sleep

camera = PiCamera()
camera.vflip = True
camera.resolution = (1920, 1080)
camera.start_preview()
sleep(2)
camera.capture('ex_img_1.jpg')

#Toma una foto con imagen volteada a un a resolucion determinada