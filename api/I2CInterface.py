from smbus import SMBus

bus = SMBus(1)      # indicates /dev/i2c-1

motor_addr = 0x8
sensors_addr = 0x9          # Bus address

# Define 15 availiable sensors
sensorLPG = 1


def ping_sensor(sensor: int) -> float:
    """
    Writes sensor value to sensor arduino
    Returns value for selected value as float
    """
    try:
        bus.write_byte(sensors_addr, sensor)
        data = bus.read_i2c_block_data(sensors_addr, 0, 4)   # Read 4 bytes from sensor addr, offset: 0
        return format_data(data)

    except OSError as e:
        print(e)
        print("Sensor device offline or incorrect address set")

def read_motor_status() -> int:
    """Reads status of motors"""
    # Write Decoder for status
    status = bus.read_byte(motor_addr)
    return status

def format_data(data=[])->float: 
    """
    Converts ASCII characters received to a float
        Creates a string from ASCII characters received in data chunk
        Converts this string to a float and returns float
    """
    formatted = chr(data[0])
    for i in range(1, len(data)):
        formatted = formatted + (chr(data[i]))      
    return float(formatted)

def test_sensor_I2C(sensor: int) -> float:
    number = ping_sensor(sensor)
    print("Sensor pinged: " + str(sensor) + ", value returned:" + str(number))