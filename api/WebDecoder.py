from GPIOManagement import MoveForward, MoveBackward, MoveLeft, MoveRight, ResetMove

def WebDecoder(keyValue):
    if keyValue == b'W':
        print("Key pressed: W")
        MoveForward()
    if keyValue == b'A':
        print("Key pressed: A")
        MoveLeft()
    if keyValue == b'S':
        print("Key pressed: S")
        MoveBackward()
    if keyValue == b'D':
       print("Key pressed: D")
       MoveRight()
    if keyValue == b'X':
        print("Key released")
        ResetMove()
    