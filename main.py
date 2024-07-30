from moisture import Moisture
from light import Light
from DFRobot_AHT20 import *
from air_quality import Air_quality
import time

moisture_sensor = Moisture()
light_sensor = Light()
aht20 = DFRobot_AHT20()
air_quality = Air_quality()
while (True):
    moisture_sensor.get_sensor_value()
    light_sensor.get_sensor_value()
    if aht20.start_measurement_ready():
        aht20.get_sensor_value()
    air_quality.get_sensor_value()
    time.sleep(3)