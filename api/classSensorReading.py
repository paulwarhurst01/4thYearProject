class SensorReading(object):
    """
    Two Strings: Name of the sensor
                 Unit used by sensor
    Integer Value: Value
    Boolean Value: Information is complete
    """
    def __init__(self, sensor: str, value: int, unit: str):
        self.sensor = sensor
        self.unit = unit
        self.value = value
        self.complete = False

    def set_complete(self):
        self.complete = True
        print(self.sensor + " reading complete.")