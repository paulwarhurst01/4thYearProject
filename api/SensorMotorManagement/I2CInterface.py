from smbus import SMBus

bus = SMBus(1)      # indicates /dev/i2c-1

motorAddr = 0x9           # motor aI2C address
sensorAddr = 0x8          # sensor I2C address

def ping_sensor(sensor: int) -> float:
    """
    Writes sensor value to sensor arduino
    Returns value for selected value as float
    """
    try:
        bus.write_byte(sensorAddr, sensor)
        data = bus.read_i2c_block_data(sensorAddr, 0, 4)   # Read 4 bytes from sensor addr, offset: 0
        return format_data(data)

    except OSError as e:
        print(e)
        print("Sensor device offline or incorrect address set")

def read_motor_status() -> int:
    """Reads status of motors"""
    # Write Decoder for status
    try:
        status = bus.read_byte(motorAddr)
        return status
    except OSError as e:
        print(e)
        print("Sensor device offline or incorrect address set")

def format_data(data=[])->float: 
    """
    Converts ASCII characters received to a float
        Creates a string from ASCII characters received in data chunk
        Converts this string to a float and returns float
    """ 
    try:
        formatted = chr(data[0])
        for i in range(1, len(data)):
            formatted = formatted + (chr(data[i])) 
        return float(formatted)
    except ValueError as e:
        print(e)

def test_sensor_I2C(sensor: int) -> float:
    """
    Pings a single sensor printing the returned float
    """
    number = ping_sensor(sensor)
    print("Sensor pinged: " + str(sensor) + ", value returned:" + str(number))

# Motor Controls 
def control_movement(direction: int):
    try:
        bus.write_byte(motorAddr, 0)
    except OSError as e:
        print(e)
        print("Sensor device offline or incorrect address set")

def move_forward():
    control_movement(1)

def move_backward():
    control_movement(2)

def turn_left():
    control_movement(3)

def turn_right():
    control_movement(4)

def reset_move():
    control_movement(0)