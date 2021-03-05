from .classSensorReading import SensorReading
from flask import Flask, jsonify
from tinydb import TinyDB
from time import sleep
import datetime 

def update_database_name() -> str:
    """
    Creates file name for database
    """
    dateTime = datetime.datetime.now()
    date = str(dateTime.year) + "-" + str(dateTime.month) + "-" + str(dateTime.day)
    time = str(dateTime.hour) + "h" + str(dateTime.minute) 
    databasename = date + "-" + time + ".json"
    return databasename

# Initiate tinydb database
db = TinyDB("SensorMotorManagement/SensorMotorLogs/" + update_database_name())

sensor_data_updating = False
#sensorsarray = []
jsonreadyarray = []

def initiate_sensor_array():
    global sensorsarray
    for s in range(0, 16):
        sensorsarray.append(SensorReading(s))
    print("Sensors array initiatied")

def get_json_ready_data():
    """
    Relies on boolean jsonreadydata and spinlock
    """
    global jsonreadyarray
    global sensor_data_updating
    #while(sensor_data_updating):
    #    print("Waiting for sensor data to update")
    return jsonreadyarray

def update_sensor_readings():
    global sensor_data_updating
    #global sensorsarray
    global jsonreadyarray
    jsonreadyarray = []
    #sensor_data_updating = True
    for sensor_id in range(0, 16):
        sensor = SensorReading(sensor_id)
        jsonready = {
            'id' : sensor.id,
            'sensorName' : sensor.sensor,
            'sensorUnit' : sensor.unit,
            'sensorValue' : sensor.value,
            'time' : sensor.time
            }
        jsonreadyarray.append(jsonready)
        sleep(0.05)
    db.insert_multiple(jsonreadyarray)
    #sensor_data_updating = False
    #print("New Sensor Data Avaliable")