# my first stepper program
# intention: to test the stepper motor
# Kiat Huang <kiat.huang@gmail.com>
# Created: 20070427
# License: https://choosealicense.com/licenses/apache-2.0/
#
# Based on
# http://www.raspberrypi-spy.co.uk/2012/07/stepper-motor-control-in-python/
#
# My hardware:
# Stepper Motor: 28BJY-48
# Stepper Motor Driver Board:ULN2003
# Raspberry Pi B

# Import required libraries
import sys
import time
import RPi.GPIO as GPIO

# Define GPIO signals to use
# Physical pins 35, 36, 37, 38
# GPIO19,GPIO16,GPIO26,GPIO20
StepPins = [19,16,26,20]

# Define simple sequence
Seq1 = [[1,0,0,0],
        [0,1,0,0],
        [0,0,1,0],
        [0,0,0,1]]


# Define advanced sequence
Seq2 = [[1, 0, 0, 0],
       [1, 1, 0, 0],
       [0, 1, 0, 0],
       [0, 1, 1, 0],
       [0, 0, 1, 0],
       [0, 0, 1, 1],
       [0, 0, 0, 1],
       [1, 0, 0, 1]]


Seq = Seq2
StepCount = len(Seq)
StepDir = 1 # Set to 1 or 2 for clockwise
            # Set to -1 or -2 for anti-clockwise

# Read wait time from the command line
if len(sys.argv)>1:
    WaitTime = int(sys.argv[1])/float(1000)
else:
    WaitTime = 10/float(1000)

# Initialize variables
StepCounter = 0

# Start main loop
try:
    while True:

        print (StepCounter, Seq[StepCounter])

        # Use BCM GPIO references
        # instead of physical pin numbers
        GPIO.setmode(GPIO.BCM)

        for pin in StepPins:
            print ("Setup Pins")
            GPIO.setup(pin, GPIO.OUT)
            # GPIO.output(pin, False)

        for pin in range(0,4):
            xpin = StepPins[pin] # get GPIO
            if Seq[StepCounter][pin]!=0:
                print ("Enable GPIO ", xpin)
                GPIO.output(xpin, True)
            else:
                GPIO.output(xpin, False)

        StepCounter += StepDir

        # If we reach the end of the sequence, start again
        if (StepCounter >= StepCount):
            StepCounter = 0
        if (StepCounter < 0):
            StepCounter = StepCount + StepDir

        # Wait before moving on
        time.sleep(WaitTime)

except KeyboardInterrupt:
    GPIO.cleanup()

except:
    GPIO.cleanup()
    if sys.version_info[0] < 3:
        print ("Must be using Python 3")
        raise
