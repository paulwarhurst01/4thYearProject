import RPi.GPIO as GPIO
from time import sleep

# running at 50Hz - Period = 20ms
# 1.5 ms - Returns servo to centre - Duty cycle = 7.5%
# 2.0 ms - Turns servo CCW - Duty cycle = 10%
# 1.0 ms - Turns servo CW - Duty cycle = 5%

class ServoController():
    def __init__(self, pin, center_dc = 7, increment = 0.25):
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(pin, GPIO.OUT)
        self.pin = pin                      # GPIO pin for PWM
        self.center_dc = center_dc          # the duty cycle for which the servo is centred
        self.duty_cycle = self.center_dc    # current duty cycle, begins at centre 
        self.increment = increment          # sets the change size of duty_cycle
        self.delay = 0.2                    # default sleep value
        self.turning = False                # control for turning while loop
        self.pwm = GPIO.PWM(pin, 50)        # set PWM signal @ 50Hz
        self.pwm.start(0)                   # Start PWM

    def print_details(self):
        print("centre_dc: " + str(self.center_dc))
        print("increment: " + str(self.increment))

    def change_increment(self, new_increment):
        """
        resets duty cycle to remain in sink
        """
        self.duty_cycle = 7
        self.increment = new_increment

    def change_delay(self, delay):
        self.delay = delay

    def set_pwm(self):
        GPIO.output(self.pin, True)
        self.pwm.ChangeDutyCycle(self.duty_cycle)
    
    def turn_ccw(self):
        """
            decrements the duty cycle
        """
        self.turning = True
        while self.turning:
            if self.duty_cycle > 2:
                self.duty_cycle = self.duty_cycle - self.increment
            self.set_pwm()
            sleep(self.delay)

    def turn_cw(self):
        """
            incrememnts the duty cycle
        """
        self.turning = True
        while self.turning:
            if self.duty_cycle < 12:                # Don't increment past max position
                self.duty_cycle = self.duty_cycle + self.increment
            self.set_pwm()
            sleep(self.delay)

    def center(self):
        """
        Centers the servo
        """
        self.duty_cycle = 7
        set_pwm()

    def stop_turning(self):
        self.turning = False                        # Break turning loop
        duty_cycle = 0
        GPIO.output(self.pin, False)
        self.pwm.ChangeDutyCycle(duty_cycle)