from .classSensorReading import SensorReading
from flask import Flask, jsonify
from tinydb import TinyDB
from time import sleep
import datetime 

sensor_data_updating = False
sensorsarray = [] 
jsonreadyarray= []

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

def initiate_sensor_array():
    global sensorsarray
    for s in range(0, 13):
        sensorsarray.append(SensorReading(s))
    print("Sensors array initiatied")

def get_json_ready_data():
    """
    Relies on boolean jsonreadydata and spinlock
    """
    global jsonreadyarray
    global sensor_data_updating
    while(sensor_data_updating):
        sleep(0.02)
        print("Waiting for sensor array to update...")
    return jsonreadyarray

def update_sensor_readings():
    global sensorsarray
    global jsonreadyarray
    global sensor_data_updating
    sensor_data_updating = True
    jsonreadyarray = []
    for sensor in sensorsarray:
        sensor.update()
        jsonready = {
            'id' : sensor.id,
            'sensorName' : sensor.sensor,
            'sensorUnit' : sensor.unit,
            'sensorValue' : sensor.value,
            'time' : sensor.time
            }
        jsonreadyarray.append(jsonready)
        sleep(0.02)
    db.insert_multiple(jsonreadyarray)
    sensor_data_updating = False
    #print("New Sensor Data Avaliable")