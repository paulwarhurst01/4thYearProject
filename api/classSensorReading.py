from .I2CInterface import ping_sensor

sensor_names = [
    "O2",
    "CO",
    "LPG",
    "Current"
]

sensor_unit = [
    "ppm",
    "ppm",
    "ppm",
    "mA"
]

class SensorReading(object):
    """
    Two Strings: Name of the sensor
                 Unit used by sensor
    Integer Value: Value
    """
    def __init__(self, id: int):
        self.id = id
        self.sensor = get_sensor_name(id)
        self.unit = get_sensor_unit(id)
        self.value = 0.00

    def get_sensor_name(id: int) -> str:
        """
        Returns the string name of the sensor represented by id
        """
        return sensor_names[id]

    def get_sensor_unit(id: int) -> str:
        """
        Returns the string unit for the sensor represented by id
        """
        return sensor_unit[id]

    def update_reading(self):
        self.value = ping_sensor(self.id)
