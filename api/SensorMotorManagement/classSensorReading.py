from .I2CInterface import ping_sensor
import datetime

sensor_names = [
    "O2",
    "CO",
    "LPG",
    "Current",
    "Sensor5",
    "Sensor6",
    "Sensor7",
    "Sensor8",
    "Sensor9",
    "Sensor10",
    "Sensor11",
    "Sensor12",
    "Sensor13",
    "Sensor14",
    "Sensor15",
    "Motor Status"
]

sensor_unit = [
    "ppm",
    "ppm",
    "ppm",
    "mA",
    "TBA",
    "TBA",
    "TBA",
    "TBA",
    "TBA",
    "TBA",
    "TBA",
    "TBA",
    "TBA",
    "TBA",
    "TBA",
    "-",
]

class SensorReading(object):
    """
    Two Strings: Name of the sensor
                 Unit used by sensor
    Integer Value: Value
    """
    def __init__(self, id: int):
        self.id = id
        self.sensor = self.get_sensor_name(id)
        self.unit = self.get_sensor_unit(id)
        self.value = 0.00
        self.time = self.get_time()

    def get_sensor_name(self, id: int) -> str:
        """
        Returns the string name of the sensor represented by id
        """
        return sensor_names[self.id]

    def get_sensor_unit(self, id: int) -> str:
        """
        Returns the string unit for the sensor represented by id
        """
        return sensor_unit[self.id]

    def update(self):
        sensorid = int(self.id)
        self.time = self.get_time()
        if self.id == 16:
            self.value = read_motor_status()
        else:
            self.value = ping_sensor(sensorid)

    def get_time(self) -> str:
        dateTime = datetime.datetime.now()
        time = str(dateTime.hour) + "h" + str(dateTime.minute) + "m" + str(dateTime.second) + "s"
        return time