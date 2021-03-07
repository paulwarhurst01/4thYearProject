from SensorMotorManagement.classMotorInterfaces import MotorControlInterface

MCI = MotorControlInterface(addr=9)

def WebDecoder(keyValue):
    if keyValue == b'W':
        print("Key pressed: W")
        MCI.move_forward()
    if keyValue == b'A':
        print("Key pressed: A")
        MCI.turn_left()
    if keyValue == b'S':
        print("Key pressed: S")
        MCI.move_backward()
    if keyValue == b'D':
       print("Key pressed: D")
       MCI.turn_right()
    if keyValue == b'X':
        print("Key released")
        MCI.reset_move()