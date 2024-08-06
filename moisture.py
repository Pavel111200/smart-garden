from gpiozero import MCP3008

class Moisture():
    def __init__(self, water_value = 38, air_value = 78):
        self.water_value = water_value
        self.air_value = air_value
        self.intervals = (air_value - water_value) / 3
        self.sensor = MCP3008(0)

    def get_sensor_value(self):
        return self.sensor.value * 100