from .classI2CInterface import I2CInterface

class MotorSensorInterface(I2CInterface):
    def __init__(self, addr):
        I2CInterface.__init__(addr)
        self.status = self.get_motor_status()

    def get_motor_status():
        status = self.read_byte()
        return status

    def get_formatted_data():
        return "Motor Data"

    def update():
        self.status = self.get_motor_status()
        self.formatted_data = self.get_formatted_data()

class MotorControlInterface(I2CInterface):
    def control_movement(self, direction: int):
        self.write_byte(direction)

    def move_forward(self):
        self.control_movement(1)

    def move_backward(self):
        self.control_movement(2)

    def turn_left(self):
        self.control_movement(3)

    def turn_right(self):
        self.control_movement(4)

    def reset_move(self):
        self.control_movement(0)

