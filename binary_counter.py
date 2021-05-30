'''
This program simulates a binary counter using LEDs
'''

import RPi.GPIO as GPIO #Library for the GPIO Pins
import time #Library for time-related tasks

def set_LED (n):
    #This function takes a number and turns the LEDs on in its binary pattern
    for i in range (8): #Runs through all the pins
        GPIO.output (pins[len(pins) - 1 - i], n >> i & 1)
    '''This line shifts the binary number by a certain number of
    spaces and sets that value for the voltage of that pin. This
    allows the program to read every digit of the binary number and
    turn on the pins that need to be turned on.'''


GPIO.setmode(GPIO.BCM) #Sets the way we reference the GPIO Pins

pins = [25,8,7,1,12,16,20,21] #A list of the pins

for i in pins: #Runs through all the pins
    GPIO.setup (i, GPIO.OUT) #Setting all the pins to an output pin

for i in range (250): #The loop goes from 0 to 249
    set_LED (i) #Converts the number to binary and turns the LEDs on
    
time.sleep (0.5) #Pauses the program for 0.5 second
GPIO.cleanup() #Resets the GPIO Pins that we used