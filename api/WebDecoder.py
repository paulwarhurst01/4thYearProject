from SensorMotorManagement.classMotorInterfaces import MotorControlInterface
import logging

motor_addr = 9
MCI = MotorControlInterface(motor_addr)

def WebDecoder(keyValue):
    if keyValue == b'W':
        logging.debug("Key pressed: W")
        MCI.move_forward()
    if keyValue == b'A':
        logging.debug("Key pressed: A")
        MCI.turn_left()
    if keyValue == b'S':
        logging.debug("Key pressed: S")
        MCI.move_backward()
    if keyValue == b'D':
       logging.debug("Key pressed: D")
       MCI.turn_right()
    if keyValue == b'X':
        logging.debug("Key pressed: X")
        MCI.reset_move()