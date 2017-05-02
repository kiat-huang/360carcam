# my first sensor program
# intention: to test the stepper motor
# Kiat Huang <kiat.huang@gmail.com>
# Created: 20070430
# License: https://choosealicense.com/licenses/apache-2.0/
#
# Based on
# https://www.raspberrypi.org/learning/parent-detector/worksheet/
#
# My hardware
# 1. RCWL-5016 motion detector
#    Bought here: http://www.ebay.fr/itm/172620108071
# 2. Raspberry Pi B+ v1.2 with 40 pins

# Usage
#
# $0
#
#

# Features
#
# 1.
#

# Notes
# 1. Code working with python3.4 on Rasbian
#    pi@raspberrypi:~ $ uname -a && cat /etc/debian_version
#    Linux raspberrypi 4.4.50+ #970 Mon Feb 20 19:12:50 GMT 2017 armv6l GNU/Linux
#    8.0
# 2. Adapt to your own GPIO pins

# Import required libraries
from gpiozero import MotionSensor
import time
import RPi.GPIO as GPIO

delay = 1000/float(1000)
pir = MotionSensor(4,queue_len=4,sample_rate=100,threshold=0.5)
# pir = MotionSensor(4)
count = 0

led = 24
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(led,GPIO.OUT)
# print ("LED on")
# print ("LED off")

try:
    while True:
        if pir.motion_detected:
            print ("Motion detected!", count)
            GPIO.output(led,GPIO.HIGH)
            time.sleep(0.1)
            GPIO.output(led,GPIO.LOW)
            count += 1
            time.sleep(delay)
        GPIO.output(led,GPIO.LOW)

except KeyboardInterrupt:
    GPIO.output(led,GPIO.LOW)
