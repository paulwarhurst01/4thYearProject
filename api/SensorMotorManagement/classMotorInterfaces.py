from .classI2CInterface import I2CInterface

class MotorSensorInterface(I2CInterface):
    def __init__(self, addr):
        I2CInterface.__init__(addr)
        self.status = self.get_motor_status()

    def get_motor_status():
        self.write_byte(0x03)           # write diagnostic register address
        status = self.read_byte()       # Read diagnostic registers
        return status

    def get_formatted_data(self):
        if self.data != 0:
            return "Motor Stalled"
        else:
            return "Motors Operating"

    def update():
        self.status = self.get_motor_status()
        self.formatted_data = self.get_formatted_data()

class MotorControlInterface(I2CInterface):
    def __init__():
        """ Run once on instantiation """
        self.write_byte(0x01)           # write Speed register address
        self.write_byte(0x90)           # Set default speed

    def control_movement(self, direction: int):
        self.write_byte(0x2)            # Write direction register address
        self.write_byte(direction)      # write direction
        self.write_byte(0x00)           # Write enable register address
        self.write_byte(0xFF)           # enable enable registers for all motors

    def move_forward(self):
        self.control_movement(1)

    def move_backward(self):
        self.control_movement(2)

    def turn_left(self):
        self.control_movement(3)

    def turn_right(self):
        self.control_movement(4)

    def reset_move(self):
        self.write_byte(0x00)           # Write enable register address
        self.write_byte(0x00)           # disable enable registers for all motors

        
        

