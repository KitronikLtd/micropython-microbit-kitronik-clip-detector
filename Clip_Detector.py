from microbit import display
from microbit import Image
from KitronikClipDetector import Detector

sensor = Detector()

while True:
    if sensor.readDigitalSensor("P2", "Dark") is True:
        display.show(Image.HAPPY)
    else:
        display.show(Image.SAD)