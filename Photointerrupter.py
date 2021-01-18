from digitalio import DigitalInOut, Direction, Pull
import time
import board

from lcd.lcd import LCD
from lcd.i2c_pcf8574_interface import I2CPCF8574Interface
lcd = LCD(I2CPCF8574Interface(0x3f), num_rows=2, num_cols=16)

interrupter = DigitalInOut(board.D3)
interrupter.direction = Direction.INPUT
interrupter.pull = Pull.UP #makes the photointerrupter an input

lcd.set_cursor_pos(0,0)
time.sleep(2)
counter = 0


max = 4#delay time
start = time.time()
while True:
    lcd.set_cursor_pos(0,0)
    if interrupter.value: #if an object passes through, the counter increases by one
     counter += 1
     time.sleep(.20) # this allows it to count individual passes
    else:
        counter = counter

    remaining = max - time.time()
    if remaining <= 0:
        lcdmessage = "Interruptions: "
        lcdmessage += str(counter)
        lcd.print(lcdmessage)
        print(lcdmessage)

        max = time.time() + 4
        counter = counter