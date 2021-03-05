from .I2CInterface import ping_sensor, read_motor_status
import datetime

motor_id = 14

sensor_names = [
    "LPG",
    "CO",
    "Smoke",
    "Hexane",
    "Propane",
    "CO2",
    "Alcohol",
    "Amonia",
    "Acetone",
    "Tolene",
    "Temperature",
    "Humidity",
    "Current",
    "Motor Status"
]

sensor_unit = [
    "ppm",
    "ppm",
    "ppm",
    "ppm",
    "ppm",
    "ppm",
    "ppm",
    "ppm",
    "ppm",
    "ppm",
    "C",
    "%",
    "mA",
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
        self.value = self.get_value(id)
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

    def get_value(self, id: int) -> float:
        if id == 16:
            return read_motor_status()
        else:
            return ping_sensor(id)

    def update(self):
        sensorid = int(self.id)
        self.time = self.get_time()
        if self.id == motor_id:
            self.value = read_motor_status()
        else:
            self.value = ping_sensor(sensorid)

    def get_time(self) -> str:
        dateTime = datetime.datetime.now()
        time = str(dateTime.hour) + "h" + str(dateTime.minute) + "m" + str(dateTime.second) + "s"
        return time