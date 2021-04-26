from picamera import PiCamera
from time import sleep
from fractions import Fraction

camera = PiCamera(
    resolution=(1280, 720),
    framerate=Fraction(1, 6),
    sensor_mode=3)
camera.shutter_speed = 6000000
camera.iso = 800

sleep(30)
camera.exposure_mode = 'off'

camera.capture('dark.jpg')

#Toma fotos con poca luz presente