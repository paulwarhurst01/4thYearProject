from flask import Flask, Response, request, jsonify, send_from_directory
from VideoStreaming.Camera import Camera
from LidarControl.Lidar import Lidar
from classWebDecoder import WebDecoder
from SensorMotorManagement.classSensorHandler import SensorHandler
from time import sleep
import threading
import logging

app = Flask(__name__)
#suppress logging of every ping
log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)

# initiate sensorHandler
sensorHandler = SensorHandler()

# initiate WebDecoder instance
webDecoder = WebDecoder(motor_addr=9)

# latest scan str
latestScan = "LatestScan.xyz" # initialised as empty string

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
    logging.debug("Key pressed: " + str(keyValue))
    webDecoder.decode(keyValue)
    return 'Done', 202

@app.route('/start_new_lidar_scan', methods=['GET'])
def start_new_lidar_scan():
    print("New Lidar scan started")
    return 'Done', 202

@app.route('/get_lidar_scan')
def display_lidar_data():
    #global latestScan
    """Fetches data from Lidar Contols"""
    return send_from_directory('/LidarControl/Scanfiles', latestScan, as_attachment=True)

@app.route('/perfrom_lidar_scan', methods=['GET'])
def perfrom_lidar_scan():
    print("Lidar Scan requested")
    return 'Done', 202


@app.route('/sensor_readings',methods=['GET'])
def sensor_readings():
    return jsonify(sensorHandler.jsonreadyarray)

def sensors_thread():
    """
    Periodically updates the sensor class
    """
    while(True):
        sensorHandler.update()
        sleep(1)

# Give time for set up to complete before starting thread that updates SensorHandler
sleep(2)
print("Starting sensors thread...")
x = threading.Thread(target=sensors_thread, daemon=True)
x.start()