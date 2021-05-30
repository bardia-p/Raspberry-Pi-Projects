'''
Testing the effects of PWM on a buzzer
'''

import RPi.GPIO as GPIO #Library for the GPIO Pins
import time
import lcd_i2c

#Setup and initialization functions of the LCD
def printLCD(string1, string2):
    lcd_i2c.printer(string1, string2)
def setup():
    lcd_i2c.lcd_init()

setup() #calls setup function of the LCD
GPIO.setmode(GPIO.BCM) #Sets the way we reference the GPIO Pins
GPIO.setup(13,GPIO.OUT) #Sets GPIO Pin 25 to an output pin

pin=GPIO.PWM (13,50)
pin.start(20)

try:
    for dc in [200, 400, 600] * 2:
        printLCD("Duty Cycle:",f"{dc}") #prints to LCD
        pin.ChangeFrequency(dc)
        print(dc)
        time.sleep(1)
        
except KeyboardInterrupt:
    print("Stopped")
    pin.stop()

GPIO.cleanup() #Resets the GPIO Pins that we used
lcd_i2c.cleanup()#LCD cleanup