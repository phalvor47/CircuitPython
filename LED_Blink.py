# Write your code here :-)
import time
import board
import digitalio
led = digitalio.DigitalInOut(board.A1)
led.direction = digitalio.Direction.OUTPUT

While True:
    led.value = True
    time.sleep(.5)
    led.value = False
    time.sleep(.5)