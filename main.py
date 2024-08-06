from moisture import Moisture
from light import Light
from DFRobot_AHT20 import *
from air_quality import Air_quality
import time
from server import PORT, HOST, SmartGardenHTTPHandler
from http.server import HTTPServer
import threading

moisture_sensor = Moisture()
light_sensor = Light()
aht20_sensor = DFRobot_AHT20()
air_quality_sensor = Air_quality()

server = HTTPServer((HOST,PORT),SmartGardenHTTPHandler)
server.moisture_sensor = moisture_sensor
server.light_sensor = light_sensor
server.aht20_sensor = aht20_sensor
server.air_quality_sensor = air_quality_sensor
server_thread = threading.Thread(target=server.serve_forever)
server_thread.start()

while (True):
    print(moisture_sensor.get_sensor_value())
    print(light_sensor.get_sensor_value())
    if aht20_sensor.start_measurement_ready():
        print(aht20_sensor.get_sensor_value())
    print(air_quality_sensor.get_sensor_value())

    time.sleep(3)