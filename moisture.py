from gpiozero import MCP3008

class Moisture():
    def __init__(self, water_value = 38, air_value = 82):
        self.water_value = water_value
        self.air_value = air_value
        self.intervals = (air_value - water_value) / 3
        self.watering_value = air_value
        self.sensor = MCP3008(0)

    def get_sensor_value(self):
        return self.sensor.value * 100
    
    def should_water(self):
        should_water = False
        if self.sensor.value * 100 > self.air_value - self.intervals or self.sensor.value * 100 > self.watering_value:
            should_water = True
        return should_water