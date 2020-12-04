import RPi.GPIO as GPIO
import atexit
from time import sleep

# 4 bits to be used to control movement
movePins = [29, 31, 32, 33]

GPIO.setmode(GPIO.BOARD)        # Board is more compatable across RPi's than BCM                  
GPIO.setup(movePins, GPIO.OUT, initial=GPIO.HIGH)       # set active low

def MoveForward():
    """Writes the move forward signal to GPIO Pins 31""" 
    GPIO.output(31, 0)

def MoveLeft():
    GPIO.output(33, 0)

def MoveRight():
    GPIO.output(29, 0)

def MoveBackward():
    GPIO.output(32, 0)

def ResetMove():
    GPIO.output(movePins, 1)

def OnExitApp():
    print("Exit GPIO")
    GPIO.cleanup

atexit.register(OnExitApp)