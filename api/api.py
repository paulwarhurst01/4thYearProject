from flask import Flask, Response, request, jsonify
from VideoStreaming.Camera import Camera
from LidarControl.Lidar import Lidar
from WebDecoder import WebDecoder
from SensorMotorManagement.classSensorHandler import SensorHandler
from time import sleep
import threading
import logging

app = Flask(__name__)

sensorHandler = SensorHandler()
log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)

# Get Camera online
def gen(Camera):
    """Video Streaming generator function."""
    while True:
        frame = Camera.get_frame()
        yield (b'--frame\r\n'
                b'Content-Type: image/jpeg\r\n\r\n' + frame + b'r\n')

# Define route for Video Feed and return video stream
@app.route('/videoFeed')
def video_feed():
    """Video streaming route."""
    return Response(gen(Camera()),
            mimetype='multipart/x-mixed-replace; boundary=frame')
    
# Define route for listening out for controls
@app.route('/control_listen', methods=['POST'])
def control_listen():
    keyValue = request.get_data()            # Flask request for data, returns data as byte
    WebDecoder(keyValue)
    return 'Done', 202

@app.route('/display_lidar_data')
def display_lidar_data():
    """Fetches data from Lidar Contols"""
    lidar_data = []                                 # empty array made to hold lidar data

@app.route('/sensor_readings',methods=['GET'])
def sensor_readings():
    return jsonify(sensorHandler.jsonreadyarray)

def sensors_thread():
    while(True):
        sensorHandler.update()
        sleep(1)

sleep(2)
print("Starting sensors thread...")
x = threading.Thread(target=sensors_thread, daemon=True)
x.start()