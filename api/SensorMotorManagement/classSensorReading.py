from .classMotorInterfaces import MotorSensorInterface
from .classSensorInterface import SensorInterface
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

class SensorReading():
    """
    -> Contains all information for a sensor reading
    -> Contains interface needed to complete reading
    -> contains functions to update readings
    """
    def __init__(self, id: int):
        self.id = id
        self.sensor = self.get_sensor_name(id)
        self.unit = self.get_sensor_unit(id)
        if(id == motor_id):
            motor_addr = 9
            self.interface = MotorSensorInterface(motor_addr)
        else:
            sensor_addr = 8
            self.interface = SensorInterface(sensor_addr, id)
        self.value = self.get_value()
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

    def get_value(self):
        """
        Retrieves formatted data from interface
        """
        return self.interface.formatted_data

    def update(self):
        """
        updates sensor instance values
        updates sensor reading
        """
        self.interface.update()
        self.time = self.get_time()
        self.value = self.get_value()

    def get_time(self) -> str:
        """
        Returns time as a string
        """
        dateTime = datetime.datetime.now()
        time = str(dateTime.hour) + "h" + str(dateTime.minute) + "m" + str(dateTime.second) + "s"
        return time