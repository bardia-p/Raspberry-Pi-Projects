'''
A simple program to simulate an automated drink server using stepper motors
'''

import RPi.GPIO as GPIO
import time
import lcd_i2c

GPIO.setwarnings(False)
lcd_i2c.lcd_init()
GPIO.setmode(GPIO.BCM)

control_pins = [21, 20, 12, 16]
for pin in control_pins:
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, 0)

# Following matrix should contain the coil energizing sequence for coils A, B, A', and B'
halfstep_seq = [
    [1,0,0,0],
    [1,1,0,0],
    [0,1,0,0],
    [0,1,1,0],
    [0,0,1,0],
    [0,0,1,1],
    [0,0,0,1],
    [1,0,0,1],
]

try:
    for i in range(50): 
        if i%10==0:
            time.sleep(3)
        for halfstep in range(8):
            for pin in range(4):
                GPIO.output(control_pins[pin], halfstep_seq[halfstep][pin])
                time.sleep(0.005)
    lcd_i2c.printer("Your drink is","ready. Enjoy")
except:
    pass

GPIO.cleanup()
lcd_i2c.cleanup()