from SensorMotorManagement.classMotorInterfaces import MotorControlInterface
#from PanAndTilt.classServoController import ServoController

class WebDecoder():
    def __init__(self, motor_addr):
        self.MCI = MotorControlInterface(motor_addr)
        #self.pan = ServoController(18)
        #self.tilt = ServoController(19)
        self.invert = False

    #def toggle_inverted(self):
     #   self.invert = !(invert)

    def decode(self, keyValue):
        if keyValue == b'W':
            self.MCI.move_forward()
        if keyValue == b'A':
            self.MCI.turn_left()
        if keyValue == b'S':
            self.MCI.move_backward()
        if keyValue == b'D':
            self.MCI.turn_right()
        if keyValue == b'X':
            self.MCI.reset_move()
        if keyValue == b'I':
            if invert:
                tilt.rotate_cw()
            else:
                tilt.rotate_ccw()
        if keyValue == b'J':
            pan.rotate_ccw()
        if keyValue == b'K':
            if invert:
                tilt.rotate_ccw
            else:
                rotate_cw
        if keyValue == b'L':
            pan.rotate_cw()
        if keyValue == b'M':
            tilt.stop_rotating()
            pan.stop_rotating()
