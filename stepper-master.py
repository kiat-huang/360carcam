#!/usr/bin/env python


from time import sleep
import RPi.GPIO as GPIO
import move

GPIO.setmode(GPIO.BOARD)
m = move.Motor([35,36,37,38])
m.rpm = 5
print "Pause in seconds: " + `m._T`
m.mode = 3
m.move_to(135)
sleep(1)
m.move_to(90)
sleep(1)
m.mode = 2
m.move_to(-90)
sleep(1)
m.move_to(0)
GPIO.cleanup()
