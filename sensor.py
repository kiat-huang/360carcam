# sensor
from gpiozero import MotionSensor
import time
import RPi.GPIO as GPIO

delay = 1000/float(1000)
pir = MotionSensor(4,queue_len=10,sample_rate=100,threshold=0.20)
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
            time.sleep(0.2)
            GPIO.output(led,GPIO.LOW)
            count += 1
            time.sleep(delay)
        GPIO.output(led,GPIO.LOW)

except KeyboardInterrupt:
    GPIO.output(led,GPIO.LOW)


