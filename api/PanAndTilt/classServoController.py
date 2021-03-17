import RPi.GPIO as GPIO
from time import sleep

# running at 50Hz - Period = 20ms
# 1.5 ms - Returns servo to centre - Duty cycle = 7.5%
# 2.0 ms - Turns servo CCW - Duty cycle = 10%
# 1.0 ms - Turns servo CW - Duty cycle = 5%

class ServoController():
    def __init__(self, pin):
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(pin, GPIO.OUT)
        self.pin = pin
        self.pwm = GPIO.PWM(pin, 50)
        self.pwm.start(0)
        self.sensitivity_setting = 4    # Initialised at maximum sensitivity setting
        self.sensitivity = [0.04, 0.03, 0.02, 0.01, 0] # Five sensitivity settings 0 -> 4 inclusive
        # Need to rethink sensitivities - 0.075 is centre!

    
    def turn_ccw(self):
        duty_cycle = 0.1 - self.sensitivity[self.sensitivity_setting]
        GPIO.output(self.pin, True)
        self.pwm.ChangeDutyCycle(duty_cycle)

    def turn_cw(self):
        duty_cycle = 0.05 + self.sensitivity[self.sensitivity_setting]
        GPIO.output(self.pin, True)
        self.pwm.ChangeDutyCycle(duty_cycle)

    def stop_turning(self)
        duty_cycle = 0
        GPIO.output(self.pin, False)
        self.pwm.ChangeDutyCycle(duty_cycle)
