#!/usr/bin/env python


# import
from time import sleep
import RPi.GPIO as GPIO
import move
import array

# configuration
GPIO.setmode(GPIO.BOARD)
m = move.Motor([35,36,37,38])
m.rpm = 5
print ("Pause in seconds: ", m._T)

def findtarget(results):
    radar = results
    print(radar)
    rMax = max(radar)
    rMaxIndex = radar.index(rMax)
    rValueL = radar[(rMaxIndex - 1)%4]
    rValueR = radar[(rMaxIndex + 1)%4]

    targetAngle = round(90 * (rMaxIndex + (rValueR - rValueL)/(rValueR + rValueL)))
    print("Target angle is", targetAngle)
    return targetAngle

try:
    m.mode = 3
    rcwl=([800,400,100,300],
          [800,600,100,200],
          [400,400,200,500],
          [900,100,300,600],
          [700,600,200,300],
          [000,400,500,600],
          [000,700,100,300],
          [800,400,300,200],
          [500,600,400,300],
          [200,700,100,0],
          [400,600,900,300])

    for a in rcwl:
        angle = findtarget(a)
        m.move_to(angle)
        sleep(1)

    """
    # move
    m.mode = 3
    m.move_to(135)
    sleep(1)
    m.move_to(90)
    sleep(1)
    m.mode = 2
    m.move_to(-90)
    sleep(1)
    m.move_to(0)
    """

# cleanup
except KeyboardInterrupt:
        GPIO.cleanup()

except :
        GPIO.cleanup()

GPIO.cleanup()

