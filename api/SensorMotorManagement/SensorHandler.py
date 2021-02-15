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

sensorsarray = []
jsonreadyarray = []

def initiate_sensor_array():
    global sensorsarray
    for s in range(0, 16):
        sensorsarray.append(SensorReading(s))
    print("Sensors array initiatied")

def get_json_ready_data():
    global jsonreadyarray
    return jsonreadyarray

def update_sensor_readings():
    global sensorsarray
    global jsonreadyarray
    for sensor in sensorsarray:
        sensor.update()
        jsonready = {
            'sensorid' : sensor.id,
            'sensorname' : sensor.sensor,
            'sensorunit' : sensor.unit,
            'sensorvalue' : sensor.value,
            'time' : sensor.time
            }
        jsonreadyarray.append(jsonready)
        sleep(0.02)
    db.insert_multiple(jsonreadyarray)
    print("New Sensor Data Avaliable")