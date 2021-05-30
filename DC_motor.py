'''
A program simulating how to use a DC motor
'''

import RPi.GPIO as GPIO
import time
import lcd_i2c

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

#A list of the commands (delay and frequency)
commands = [[0.1, e] for e in range(0, 36, 1)]

GPIO.setup(20, GPIO.OUT) #clockwise pin for motor
pin20 = GPIO.PWM(20, 50)
GPIO.setup(21, GPIO.OUT) #counterclockwise pin for the motor
pin21 = GPIO.PWM(21, 50)
GPIO.setup(25, GPIO.OUT) #an LED connected to pin 25
GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) #a button
GPIO.setup(24, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) #a button

lcd_i2c.lcd_init()

try:
    while True:
        print("Press the button")
        lcd_i2c.printer("Press a button", "")
        while True: #Waits for the user to press a button
            user_input = GPIO.input(23), GPIO.input(24)
            clock_pin, count_pin = user_input
            if clock_pin == 1: #Finds out which buttons was pressed
                is_clockwise = 1
                break
            elif count_pin == 1:
                is_clockwise = 0
                break

        print(f"Running {'clockwise' if not is_clockwise else 'counter-clockwise'}")

        lcd_i2c.printer("Press a button", f"{'clockwise' if not is_clockwise else 'counter-clockwise'}")
        GPIO.output(25, 1) #the lED is turned on

        # Buzzer is turned on when the motor is about to start
        print("Buzzer")
        GPIO.setup(13, GPIO.OUT)
        buz = GPIO.PWM(13, 100)
        buz.start(0)
        buz.ChangeDutyCycle(50)
        time.sleep(1)
        buz.stop()
        print("Stopped buzzing")

        if is_clockwise==0:
            pin20.start(0)
            for delay, duty_cycle in commands: #the motor starts turning
                print(f"Delay {delay} at {duty_cycle} clockwise")
                pin20.ChangeDutyCycle(duty_cycle)
                time.sleep(delay)

            pin20.stop() #the motor stops
            is_clockwise=2
            
        elif is_clockwise==1:
            pin21.start(0)

            for delay, duty_cycle in commands: #the motor starts turning
                print(f"Delay {delay} at {duty_cycle} counter-clockwise")
                pin21.ChangeDutyCycle(duty_cycle)
                time.sleep(delay)

            pin21.stop() #the motor stops
            is_clockwise=2

        GPIO.output(25, 0) #The LED is turned off
        print("Delaying")
        time.sleep(0.1)
except KeyboardInterrupt: #the program quits when a key is pressed
    pass

lcd_i2c.printer("Quitting", "")
time.sleep(1)
lcd_i2c.printer("", "")

GPIO.cleanup()
lcd_i2c.cleanup()