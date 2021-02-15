from SensorMotorManagement.I2CInterface import move_forward, move_backward, turn_left, turn_right, reset_move

def WebDecoder(keyValue):
    if keyValue == b'W':
        print("Key pressed: W")
        move_forward()
    if keyValue == b'A':
        print("Key pressed: A")
        turn_left()
    if keyValue == b'S':
        print("Key pressed: S")
        move_backward()
    if keyValue == b'D':
       print("Key pressed: D")
       turn_right()
    if keyValue == b'X':
        print("Key released")
        reset_move()
    