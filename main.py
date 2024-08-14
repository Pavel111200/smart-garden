from moisture import Moisture
from light import Light
from DFRobot_AHT20 import *
from air_quality import Air_quality
import time
from server import PORT, HOST, SmartGardenHTTPHandler
from http.server import HTTPServer
import threading
from gpiozero import LED, DigitalOutputDevice

def water_plant():
    water_pump.on()
    time.sleep(30)
    water_pump.off()

moisture_sensor = Moisture()
light_sensor = Light()
aht20_sensor = DFRobot_AHT20()
air_quality_sensor = Air_quality()

led = LED(17)
fan = DigitalOutputDevice(27, active_high=False)
water_pump = DigitalOutputDevice(22, active_high=False)

server = HTTPServer((HOST,PORT),SmartGardenHTTPHandler)
server.moisture_sensor = moisture_sensor
server.light_sensor = light_sensor
server.aht20_sensor = aht20_sensor
server.air_quality_sensor = air_quality_sensor
server_thread = threading.Thread(target=server.serve_forever)
server_thread.start()

while (True):
    if moisture_sensor.should_water() and water_pump.value == 0:
        pump_thread = threading.Thread(target=water_plant)
        pump_thread.start()

    if light_sensor.should_turn_on_lights() and not led.is_lit:
        led.on()
    elif led.is_lit and not light_sensor.should_turn_on_lights():
        led.off()

    time.sleep(1)

    if aht20_sensor.should_turn_on_ventilation() and fan.value == 0:
        fan.on()
    elif not aht20_sensor.should_turn_on_ventilation() and fan.value == 1:
        fan.off()

    # if air_quality_sensor.should_turn_on_ventilation() and fan.value == 0:
    #     fan.on()
    # elif fan.value == 1:
    #     fan.off()

    # print(moisture_sensor.get_sensor_value())
    # print(light_sensor.get_sensor_value())
    if aht20_sensor.start_measurement_ready():
        print(aht20_sensor.get_sensor_value())
    # print(air_quality_sensor.get_sensor_value())

    # print("Should water " + str(moisture_sensor.should_water()))
    # print("Turn lights on " + str(light_sensor.should_turn_on_lights()))
    # print("AHT20 should turn on " + str(aht20_sensor.should_turn_on_ventilation()))
    # print("Air quality should turn on " + str(air_quality_sensor.should_turn_on_ventilation()))

    time.sleep(2)