# Write your code here :-)

import board
import time
import pulseio
import servo
import touchio

pwm = pulseio.PWMOut(board.A3, duty_cycle=2 ** 15, frequency=50)

my_servo = servo.ContinuousServo(pwm)

touch_A1 = touchio.TouchIn(board.A1)
touch_A2 = touchio.TouchIn(board.A2)


while True:

    if touch_A1.value:
        print("touched a1")
        my_servo.throttle = 1

    if touch_A2.value:
        print("touched a2")
        my_servo.throttle = -1

    time.sleep(0.01)