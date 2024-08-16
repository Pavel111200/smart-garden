from gpiozero import MCP3008
from sensor import Sensor

class Moisture(Sensor):
    def __init__(self, water_value = 38, air_value = 82):
        self.water_value = water_value
        self.air_value = air_value
        self.intervals = (air_value - water_value) / 3
        # self.turn_on_value = air_value
        self.sensor = MCP3008(0)
        super().__init__(air_value)

    def get_sensor_value(self):
        return self.sensor.value * 100
    
    def should_turn_on_actuator(self):
        should_turn_on = False
        if self.sensor.value * 100 > self.air_value - self.intervals or self.sensor.value * 100 > self.turn_on_value:
            should_turn_on = True
        return should_turn_on