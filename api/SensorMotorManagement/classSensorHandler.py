from .classSensorReading import SensorReading
from tinydb import TinyDB
from time import sleep
import datetime 

class SensorHandler():
    def __init__(self):
        self.sensorsarray = self.initiate_sensor_array()
        self.jsonreadyarray = []
        self.databasename = self.get_database_name()
        # Initiate tinydb database
        self.db = TinyDB("SensorMotorManagement/SensorMotorLogs/" + self.databasename)


    def get_database_name(self) -> str:
        """
        Creates file name for database
        """
        dateTime = datetime.datetime.now()
        date = str(dateTime.year) + "-" + str(dateTime.month) + "-" + str(dateTime.day)
        time = str(dateTime.hour) + "h" + str(dateTime.minute) 
        databasename = date + "-" + time + ".json"
        return databasename

    def initiate_sensor_array(self):
        sensorsarray = []
        for s in range(0, 13):
            sensorsarray.append(SensorReading(s))
        print("Sensors array initiatied")
        return sensorsarray

    def update(self):
        tempjsonreadyarray = []
        for sensor in self.sensorsarray:
            sensor.update()
            jsonready = {
                'id' : sensor.id,
                'sensorName' : sensor.sensor,
                'sensorUnit' : sensor.unit,
                'sensorValue' : sensor.value,
                'time' : sensor.time
                }
            tempjsonreadyarray.append(jsonready)
            sleep(0.02)
        self.db.insert_multiple(tempjsonreadyarray)
        self.jsonreadyarray = tempjsonreadyarray