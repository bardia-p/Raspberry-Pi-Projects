'''
A simple of example using servo motors and LCDs
'''

import RPi.GPIO as GPIO
import lcd_i2c
import time
import numpy

#Setup and initialization functions of the LCD
def setupLCD():
    lcd_i2c.lcd_init()

def printLCD(string1, string2):
    lcd_i2c.printer(string1,string2)

#General GPIO Pin Setup
GPIO.setmode(GPIO.BCM)
servoPIN = 25 #selects the pin for the servo motor
GPIO.setup(servoPIN, GPIO.OUT) #set the servoPIN to an output
speed = 0.025
setupLCD()

#PWM Pin Setup
p = GPIO.PWM(servoPIN, 50) # GPIO 22 is set for PWM with 50Hz
p.start(2.5) # Initialization of the PWM pin and duty cycle
#use of try/except to get out of loop when needed (ctrl + c)

try:
    printLCD("Servo will now ", "begin") #prints to LCD
    while True: #starts main loop
        time.sleep(1)
        printLCD("Going,", "Counterclockwise")
        for dutyCycle in numpy.arange (2.5,12,0.25): #gives evenly space non-integer values within the range
            p.ChangeDutyCycle(dutyCycle) #changes duty cycle incrementally to rotate the servo
            time.sleep( speed ) #timestep between each change in duty cycle

        time.sleep(1)
        printLCD("Going,","Clockwise")
        for dutyCycle in numpy.arange (12,2.5,-0.25):
            p.ChangeDutyCycle(dutyCycle)
            time.sleep( speed )
except KeyboardInterrupt:
    # Cleanup after (ctrl + c) is pressed
    print("Cleaning up!") #tells the user cleanup is occuring
    p.stop() #stops PWM pin

lcd_i2c.cleanup() #cleans up the LCD
GPIO.cleanup() #cleanup GPIO pins used in the script