from .classSensorReading import SensorReading
from flask import Flask, jsonify
from tinydb import TinyDB
from time import sleep

# Include in flask context

# Initiate tinydb database
db = TinyDB('SensorMotorManagement/SensorMotorLogs/db.json')

sensorsarray = []
jsonreadyarray = []

def initiate_sensor_array():
    for s in range(0, 16):
        sensorsarray.append(SensorReading(s))
    print("Sensors array initiatied")

def get_sensor_data():
    return jsonreadyarray
    sensordata.append(jsonify(sensorid=sensors_array[sensor].id,
                            sensorname=sensors_array[sensor].sensor,
                            sensorunit=sensors_array[sensor].unit,
                            sensorvalue=sensors_array[sensor].value
                        )
                    )
    db.insert(sensordata)
    return sensordata

def update_sensor_readings():
    global sensorsarray
    global jsonreadyarray
    for sensor in sensorsarray:
        sensor.update_reading()
        jsonready = {
            'sensorid' : sensor.id,
            'sensorname' : sensor.sensor,
            'sensorunit' : sensor.unit,
            'sensorvalue' : sensor.value
            }
        jsonreadyarray.append(jsonready)
        sleep(0.02)
    db.insert_multiple(jsonreadyarray)
    print("New Sensor Data Avaliable")
