'''
A program demonstrating how to use a button
'''

import RPi.GPIO as GPIO
import time
import lcd_i2c 

PIN = 25
#Setup and initialization functions of the LCD
def printLCD(string1, string2):
    lcd_i2c.printer(string1, string2)

def setup():
    lcd_i2c.lcd_init()

#General GPIO Setup
GPIO.setmode(GPIO.BCM) #sets how we reference GPIO pins
GPIO.setup( PIN ,GPIO.IN, pull_up_down=GPIO.PUD_DOWN) #sets pin 17 to a pull-down pin, pulls the voltage of the pin to 0V when nothing is connected
setup() #calls setup function of the LCD

try:
    while True:
        printLCD("Press the button!!"," ") #prints to LCD
        if(GPIO.input( PIN ) == GPIO.HIGH): #Checks if input is high (3.3V), if so the button is pressed (connects 3.3V rail to pin)
            printLCD("Button Pressed!!!", "Reset in 2s")
            time.sleep(2)
        time.sleep(0.1)
except KeyboardInterrupt:
    pass

GPIO.cleanup()
lcd_i2c.cleanup()